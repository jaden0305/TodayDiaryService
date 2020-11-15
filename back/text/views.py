import pandas
import calendar
import datetime
import json

from redis import Redis
from redis.exceptions import ConnectionError

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema

from .analysis.analysis import TextAnalysis
from post.models import Post, Emotion, RecommendMusic
from .serializers import *
from post.serializers import RecommandMusicSerializer, EmotionSerializer


User = get_user_model()


def redis_check():
    try:
        redis_host = Redis('127.0.0.1', socket_connect_timeout=1)
        return redis_host.ping()
    except ConnectionError:
        return False

@swagger_auto_schema(methods=['post'], request_body=DiaryAnalysisSerializer)
@api_view(['POST'])
def analyze(request):
    date = request.data.get('date')
    if Post.objects.filter(created=date, user=request.user).exists():
        msg = {
            'detail': '해당 날짜에 이미 작성된 일기가 있습니다.',
            'exist': True
        }
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    need_music = not request.data.get('search')
    title = request.data.get('title')
    text = request.data.get('content')
    stickers = request.data.get('stickers', [])
    if not text.strip():
        msg = {
            'detail': '"content" 내용이 없습니다.'
        }
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    data = {
        'title': title,
        'text': text,
        'stickers': stickers
    }
    ta = TextAnalysis(data)
    result = ta.text_analysis()

    feels = result['feel']
    for idx, feel in enumerate(feels):
        if feel[0] == 'no_emotion':
            feels.pop(idx)
            break
    feels.sort(key=lambda x: -x[1])

    if feels:
        emotion_id = feels[0][0]
    else:
        result['feel'] = [(4, 0)]
        emotion_id = 4
    emotion = get_object_or_404(Emotion, pk=emotion_id)

    if need_music:
        music = emotion.musics.order_by('?')[0]
        result['music'] = RecommandMusicSerializer(instance=music).data
    else:
        music = None
        result['music'] = music
    return Response(result, status=status.HTTP_200_OK)

@api_view(['POST'])
def statistics(request):
    user = int(request.data['user'])
    text = request.data['text']
    date = request.data['date']
    post_id = request.data['post']

    ta = TextAnalysis(request.data)

    result = ta.text_analysis()

    for lis in result['word_count']:
        word, count, emotion = lis
        data = {
            'user': get_object_or_404(User, pk=user),
            'date': date,
            'word': word,
            'count': count,
            'emotion': emotion,
        }

        wordcloud_serializer = WordCloudReportSerializer(data=data)

        wordcloud_serializer.is_valid(raise_exception=True)
        wordcloud_serializer.save(date=date, user=get_object_or_404(User, pk=user), post=get_object_or_404(Post, pk=post_id))

    score = round(result['score'],3)

    result['feel'].sort(key=lambda x:-x[1])

    emotion = get_object_or_404(Emotion, pk=result['feel'][0][0])

    data = {
        'user': user,
        'date': date,
        'score': result['score'],
        'emotion': emotion.id,
        'post': post_id,
    }

    daily_report_serializer = DailyReportSerializer(data=data)
    daily_report_serializer.is_valid(raise_exception=True)
    daily_report_serializer.save(
        user=get_object_or_404(User, pk=user),
        score=score,
        post=get_object_or_404(Post, pk=post_id),
        emotion=emotion)

    result = {
        **daily_report_serializer.data
    }
    result['emotion'] = EmotionSerializer(instance=emotion).data
    return Response(result, status=status.HTTP_201_CREATED)

@swagger_auto_schema(methods=['get'], query_serializer=SelectEmotionSerializer)
@api_view(['GET'])
def select(request):
    emotion = request.GET.get('emotion')
    emotion = get_object_or_404(Emotion, pk=emotion)
    recommend_music = emotion.musics.order_by('?')[0]
    
    data = {
        'emotion': emotion.id,
        'recommend_music': RecommandMusicSerializer(instance=recommend_music).data
    }

    return Response(data, status=status.HTTP_200_OK)

@swagger_auto_schema(methods=['get'], query_serializer=WeeklyDateSerializer)
@api_view(['GET'])
def weekly(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    cache_key = f'w-u{request.user.id}-s{start}'
    
    # redis_check() 연결 되는지 확인
    # is_before_week 요청 결과가 이번주 전 인가??
    if redis_check():
        try:
            cached_data = cache.get(cache_key)
        except ConnectionError:
            cached_data = None
        if cached_data:
            print('cache gotten')
            return Response(cached_data, status=status.HTTP_200_OK)

    dt_index = pandas.date_range(start=start, end=end)

    dt_list = dt_index.strftime("%Y-%m-%d").tolist()

    daily_report = DailyReport.objects.filter(date__range=[start, end], user_id=request.user.id).order_by('date')
    wordcloud = WordCloudReport.objects.filter(date__range=[start, end], user_id=request.user.id)

    daily_report_serializer = DailyReportSerializer(instance=daily_report, many=True)
    wordcloud_serializer = WordCloudReportSerializer(instance=wordcloud, many=True)

    temp = {}
    wc_list = []
    graph_list = []
    # wordcloud data
    for i in wordcloud_serializer.data:
        if i['word'] not in temp:
            temp[i['word']] = [i['count'], i['emotion']]
        else:
            temp[i['word']][0] += i['count']
    for key, value in temp.items():
        wc_list.append([key, value[0], value[1]])
    
    # score data`
    for date in dt_list:
        for qdate in daily_report_serializer.data:
            if date == qdate['date']:
                graph_list.append(qdate)
                break
        else:
            graph_list.append({})
        
    result = {'score': graph_list, 'wordcloud': wc_list}
    if redis_check():
        cache.set(cache_key, result, 3600)
        print('cache_set')
    
    return Response({'score': graph_list, 'wordcloud': wc_list})

@swagger_auto_schema(methods=['get'], query_serializer=MonthlyDateSerializer)
@api_view(['GET'])
def monthly(request):
    year = request.GET.get('year')
    month = request.GET.get('month')

    cache_key = f'm-u{request.user.id}-{year}-{month}'
    
    # redis_check() 연결 되는지 확인
    # is_before_week 요청 결과가 이번주 전 인가??
    if redis_check():
        try:
            cached_data = cache.get(cache_key)
        except ConnectionError:
            cached_data = None
        if cached_data:
            print('cache gotten')
            return Response(cached_data, status=status.HTTP_200_OK)

    daily_report = DailyReport.objects.filter(date__year=year, date__month=month, user_id=request.user.id)
    wordcloud = WordCloudReport.objects.filter(date__year=year, date__month=month, user_id=request.user.id)

    daily_report_serializer = DailyReportSerializer(instance=daily_report, many=True)
    wordcloud_serializer = WordCloudReportSerializer(instance=wordcloud, many=True)

    temp = {}
    wc_list = []
    graph_list = []
    year, days = calendar.monthrange(int(year), int(month))

    for i in wordcloud_serializer.data:
        if i['word'] not in temp:
            temp[i['word']] = [i['count'], i['emotion']]
        else:
            temp[i['word']][0] += i['count']
    for key, value in temp.items():
        wc_list.append([key, value[0], value[1]])
    
    for day in range(1, days + 1):
        for qdate in daily_report_serializer.data:
            if day == int(qdate['date'][-2:]):
                graph_list.append(qdate)
                break
        else:
            graph_list.append({})
    
    result = {'score':graph_list, 'wordcloud': wc_list}
    if redis_check():
        cache.set(cache_key, result, 3600)
        print('cache_set')

    return Response(result, status=status.HTTP_200_OK)

@swagger_auto_schema()
@api_view(['GET'])
def total(request):
    daily_report = DailyReport.objects.filter(user_id=request.user.id)
    wordcloud = WordCloudReport.objects.filter(user_id=request.user.id)

    daily_report_serializer = DailyReportSerializer(instance=daily_report, many=True)
    wordcloud_serializer = WordCloudReportSerializer(instance=wordcloud, many=True)

    temp = {}
    wc_list = []
    for i in wordcloud_serializer.data:
        if i['word'] not in temp:
            temp[i['word']] = [i['count'], i['emotion']]
        else:
            temp[i['word']][0] += i['count']
    
    for key, value in temp.items():
        wc_list.append([key, value[0], value[1]])

    return Response({'score':daily_report_serializer.data, 'wordcloud': wc_list})


@swagger_auto_schema()
@api_view(['GET'])
def redistest(request):
    print(redis_host.ping())
    print(cache.get('asdfasdf'))
    cache.set('test', {'test': 1})
    print(cache.get('test'), type(cache.get('test')))
    cache.set('test2', 2)
    print(cache.get('test2'))
