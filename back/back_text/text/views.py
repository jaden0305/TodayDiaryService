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
            'user': user,
            'date': date,
            'word': lis[0],
            'count': lis[1],
            'emotion': lis[2],
        }

        wordcloud_serializer = WordCloudReportSerializer(data=data)
        if wordcloud_serializer.is_valid(raise_exception=True):
            wordcloud_serializer.save()

    score = round(result['score'],3)

    if len(result['feel']) >= 2:
        data = {
            'user': user,
            'score': score,
            'emotions': str(result['feel']),
            'date': date,
            'post': post.id,
        }

        multiple_emotion_serializer = MultipleEmotionSerializer(data=data)

        if multiple_emotion_serializer.is_valid(raise_exception=True):
            multiple_emotion_serializer.save(user=get_object_or_404(User, pk=user) ,score=score, post=post)
        return Response(multiple_emotion_serializer.data, status=status.HTTP_201_CREATED)
    # print(1231241)

    emotion = get_object_or_404(Emotion, name=result['feel'][0][0])

    data = {
        'user': user,
        'date': date,
        'emotions': str(result['feel']),
        'score': result['score'],
        'emotion': emotion.id,
        'post': post.id,
    }

    daily_report_serializer = DailyReportSerializer(data=data)
    if daily_report_serializer.is_valid(raise_exception=True):
        daily_report_serializer.save(user=get_object_or_404(User, pk=user) ,score=score, post=post)

    return Response(daily_report_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
def select_emotion(request):
    pass