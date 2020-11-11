import pandas
import calendar
import datetime
import json

from redis import Redis

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
from post.serializers import RecommandMusicSerializer


User = get_user_model()

redis_host = Redis('127.0.0.1', socket_connect_timeout=1)

def redis_check():
    return redis_host.ping()

@swagger_auto_schema(methods=['post'], request_body=DiaryAnalysisSerializer)
@api_view(['POST'])
def analyze(request):
    need_music = not request.data.get('search')
    title = request.data.get('title')
    text = request.data.get('content')
    stickers = json.loads(request.data.get('stickers', '[]'))
    data = {
        'title': title,
        'text': text,
        'stickers': stickers
    }
    ta = TextAnalysis(data)
    result = ta.text_analysis()
    emotion = get_object_or_404(Emotion, name=result['feel'][0][0])
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
        wordcloud_serializer.save(date=date, user=get_object_or_404(User, pk=user))

    score = round(result['score'],3)

    result['feel'].sort(key=lambda x:x[1])

    emotion = get_object_or_404(Emotion, name=result['feel'][0][0])

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
    recommend_music = RecommendMusic.objects.filter(emotion=emotion.id).order_by('?')[:1]
    
    data = {
        'emotion': emotion.id,
        'recommend_music': recommend_music[0].id
    }

    return Response(data, status=status.HTTP_200_OK)

@swagger_auto_schema(methods=['get'], query_serializer=WeeklyDateSerializer)
@api_view(['GET'])
def weekly(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    today = request.GET.get('today')

    start_year, start_month, start_day = map(int, start.split('-'))
    today_year, today_month, today_day = map(int, today.split('-'))
    
    today_date = datetime.date(today_year, today_month, today_day)
    start_date = datetime.date(start_year, start_month, start_day)
    date_delta = today_date - start_date
    is_before_week = date_delta > datetime.timedelta(days=6)
    cache_key = f'w-u{request.user.id}-s{start_year}{start_month}{start_day}'
    
    # redis_check() 연결 되는지 확인
    # is_before_week 요청 결과가 이번주 전 인가??
    if redis_check() and is_before_week:
        cached_data = cache.get(cache_key)
        if cached_data:
            print('cache gotten')
            return Response(cached_data, status=status.HTTP_200_OK)
        
    cache.delete(cache_key)

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
    cache.set(cache_key, result, 3600)
    print('cache_set')
    
    return Response({'score': graph_list, 'wordcloud': wc_list})

@swagger_auto_schema(methods=['get'], query_serializer=MonthlyDateSerializer)
@api_view(['GET'])
def monthly(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
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

    return Response({'score':graph_list, 'wordcloud': wc_list})

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