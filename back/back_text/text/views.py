from django.shortcuts import render, get_object_or_404

# from django.conf.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .analysis.analysis import TextAnalysis
from .models import Post, Emotion
# from .models import User
from .serializers import *

from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

@swagger_auto_schema()
@api_view(['POST'])
def statistics(request):
    user = int(request.data['user'])
    text = request.data['text']
    date = request.data['date']
    post_id = request.data['post_id']

    post = get_object_or_404(Post, pk=post_id)

    ta = TextAnalysis(text)

    result = ta.text_analysis()
    
    for lis in result['word_count']:
        data = {
            'user': get_object_or_404(User, pk=user),
            'date': date,
            'word': lis[0],
            'count': lis[1],
            'emotion': lis[2],
        }
        print(data)
        wordcloud_serializer = WordCloudReportSerializer(data=data)
        print(wordcloud_serializer.initial_data)
        # if wordcloud_serializer.is_valid(raise_exception=True):
            # wordcloud_serializer.save()
        if wordcloud_serializer.is_valid():
            print(1)
            wordcloud_serializer.save(date=date, user=get_object_or_404(User, pk=user))
        else:
            print(2)
            print(wordcloud_serializer.errors)
        print(3)

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
    result['feel'].sort(key=lambda x:x[1])
    emotion = get_object_or_404(Emotion, name=result['feel'][0][0])

    data = {
        'user': user,
        'date': date,
        'emotions': str(result['feel']),
        'score': result['score'],
        'emotion': emotion,
        'post': post.id,
    }

    daily_report_serializer = DailyReportSerializer(data=data)

    if daily_report_serializer.is_valid(raise_exception=True):
        daily_report_serializer.save(user=get_object_or_404(User, pk=user) ,score=score, post=post)
    result = {
        **daily_report_serializer.data
    }
    result['emotion'] = EmotionSerializer(instance=emotion).data
    return Response(result, status=status.HTTP_201_CREATED)

# @api_view(['PATCH'])
# def select_emotion(request):
#     pass

@swagger_auto_schema(methods=['get'], query_serializer=WeeklyDateSerializer)
@api_view(['GET'])
def weekly(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    daily_report = DailyReport.objects.filter(date__range=[start, end], user_id=request.user.id)
    wordcloud = WordCloudReport.objects.filter(date__range=[start, end], user_id=request.user.id)

    daily_report_serializer = DailyReportSerializer(instance=daily_report, many=True)
    wordcloud_serializer = WordCloudReportSerializer(instance=wordcloud, many=True)

    temp = {}
    lis = []

    for i in wordcloud_serializer.data:
        if i['word'] not in temp:
            temp[i['word']] = [i['count'], i['emotion']]
        else:
            temp[i['word']][0] += i['count']
    
    for key, value in temp.items():
        lis.append([key, value[0], value[1]])
    
    return Response({'score':daily_report_serializer.data, 'wordcloud': lis})

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
    lis = []

    for i in wordcloud_serializer.data:
        if i['word'] not in temp:
            temp[i['word']] = [i['count'], i['emotion']]
        else:
            temp[i['word']][0] += i['count']
    
    for key, value in temp.items():
        lis.append([key, value[0], value[1]])

    return Response({'score':daily_report_serializer.data, 'wordcloud': lis})

@swagger_auto_schema()
@api_view(['GET'])
def total(request):
    daily_report = DailyReport.objects.filter(user_id=request.user.id)
    wordcloud = WordCloudReport.objects.filter(user_id=request.user.id)

    daily_report_serializer = DailyReportSerializer(instance=daily_report, many=True)
    wordcloud_serializer = WordCloudReportSerializer(instance=wordcloud, many=True)

    temp = {}
    lis = []
    for i in wordcloud_serializer.data:
        if i['word'] not in temp:
            temp[i['word']] = [i['count'], i['emotion']]
        else:
            temp[i['word']][0] += i['count']
    
    for key, value in temp.items():
        lis.append([key, value[0], value[1]])

    return Response({'score':daily_report_serializer.data, 'wordcloud': lis})