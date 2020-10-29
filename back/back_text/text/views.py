from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework import status

from .analysis.analysis import TextAnalysis
from .models import Post, Emotion
from .serializers import *

from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema()
@api_view(['POST'])
def statistics(request):
    user = request.data['user']
    text = request.data['text']
    date = request.data['date']
    post_id = request.data['post_id']

    post = get_object_or_404(Post, pk=post_id)

    ta = TextAnalysis()
    result = ta.text_analysis(text)

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


    if len(result['feel']) >= 2:
        data = {
            'user': user,
            'date': date,
            'emotions': str(result['feel']),
            'score': result['score'],
            'post': post,
        }
        multiple_emotion_serializer = MultipleEmotionSerializer(data=data)
        if multiple_emotion_serializer.is_valid(raise_exception=True):
            multiple_emotion_serializer.save()
        return Response(multiple_emotion_serializer.data, status=status.HTTP_201_CREATED)

    emotion = get_object_or_404(Emotion, name=result['feel'][0][0])

    data = {
        'user': user,
        'date': date,
        'emotions': str(result['feel']),
        'score': result['score'],
        'emotion': emotion,
        'post': post,
    }

    daily_report_serializer = DailyReportSerializer(data=data)
    if daily_report_serializer.is_valid(raise_exception=True):
        daily_report_serializer.save()

    return Response(daily_report_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
def select_emotion(request):
    pass