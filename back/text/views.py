from django.shortcuts import render, get_object_or_404

# from django.conf.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .analysis.analysis import TextAnalysis
from post.models import Post, Emotion
# from .models import User
from .serializers import *

from drf_yasg.utils import swagger_auto_schema

import pandas, calendar

User = get_user_model()

@swagger_auto_schema()
@api_view(['POST'])
def statistics(request):
    print(request.data)
    user = int(request.data['user'])
    text = request.data['text']
    date = request.data['date']
    post_id = request.data['post_id']
    post = get_object_or_404(Post, pk=post_id)

    ta = TextAnalysis(text)

    result = ta.text_analysis()
    print(result)
    for lis in result['word_count']:
        data = {
            'user': get_object_or_404(User, pk=user),
            'date': date,
            'word': lis[0],
            'count': lis[1],
            'emotion': lis[2],
        }

        wordcloud_serializer = WordCloudReportSerializer(data=data)

        # if wordcloud_serializer.is_valid(raise_exception=True):
            # wordcloud_serializer.save()
        if wordcloud_serializer.is_valid(raise_exception=True):
            wordcloud_serializer.save(date=date, user=get_object_or_404(User, pk=user))

    score = round(result['score'],3)

    # if len(result['feel']) >= 2:
    #     data = {
    #         'user': user,
    #         'score': score,
    #         'emotions': str(result['feel']),
    #         'date': date,
    #         'post': post.id,
    #     }

    #     multiple_emotion_serializer = MultipleEmotionSerializer(data=data)

    #     if multiple_emotion_serializer.is_valid(raise_exception=True):
    #         multiple_emotion_serializer.save(user=get_object_or_404(User, pk=user) ,score=score, post=post)
    #     return Response(multiple_emotion_serializer.data, status=status.HTTP_201_CREATED)
    # print(result)
    # print(result['feel'])
    result['feel'].sort(key=lambda x:x[1])
    # print(result['feel'][0][0])
    # print(result['feel'])

    emotion = get_object_or_404(Emotion, name=result['feel'][0][0])
    print(emotion)
    data = {
        'user': user,
        'date': date,
        'user_emotion': emotion.id,
        'score': result['score'],
        'emotion': emotion.id,
        'post': post.id,
    }

    daily_report_serializer = DailyReportSerializer(data=data)
    if daily_report_serializer.is_valid():
        daily_report_serializer.save(
            user=get_object_or_404(User, pk=user),
            score=score,
            post=post,
            emotion=emotion,
            user_emotion=emotion)
    else:
        print(daily_report_serializer.errors)

    result = {
        **daily_report_serializer.data
    }
    result['emotion'] = EmotionSerializer(instance=emotion).data
    return Response(result, status=status.HTTP_201_CREATED)

@swagger_auto_schema(methods=['patch'], query_serializer=SelectEmotionSerializer)
@api_view(['PATCH'])
def select(request):
    # print(request.GET)
    post_id = request.GET.get('post_id')
    emotion = request.GET.get('emotion')
    report = get_object_or_404(DailyReport, post_id=post_id)
    # report.user_emotion = get_object_or_404(Emotion, pk=emotion)
    data = {
        'user_emotion': emotion
    }
    serializer = UserSelectEmotionSerializer(instance=report, data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # print(serializer.data)
    return Response(serializer.data)

@swagger_auto_schema(methods=['get'], query_serializer=WeeklyDateSerializer)
@api_view(['GET'])
def weekly(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    dt_index = pandas.date_range(start=start, end=end)

    # type(dt_index) => DatetimeIndex
    # DatetimeIndex => list(str)
    dt_list = dt_index.strftime("%Y-%m-%d").tolist()

    daily_report = DailyReport.objects.filter(date__range=[start, end], user_id=request.user.id).order_by('date')
    wordcloud = WordCloudReport.objects.filter(date__range=[start, end], user_id=request.user.id)

    daily_report_serializer = DailyReportSerializer(instance=daily_report, many=True)
    wordcloud_serializer = WordCloudReportSerializer(instance=wordcloud, many=True)

    # print(daily_report_serializer.data)
    # print(wordcloud_serializer.data)

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
    
    # score data
    for date in dt_list:
        for qdate in daily_report_serializer.data:
            if date == qdate['date']:
                # lis.append([])
                graph_list.append(qdate)
                break
        else:
            graph_list.append({})
        # print(daily_report_serializer.data)
    #     if idx in daily_report_serializer.data['date']:
    #         list
    
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
    # print(days)
    print(daily_report_serializer.data)

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