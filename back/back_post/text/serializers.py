from rest_framework import serializers

# from accounts.serializers import UserSerializer
from .models import *
from post.serializers import EmotionSerializer

class WordCloudReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCloudReport
        fields = ('word', 'count', 'emotion')

class DailyReportSerializer(serializers.ModelSerializer):
    emotion = EmotionSerializer(read_only=True)
    user_emotion = EmotionSerializer(read_only=True)
    class Meta:
        model = DailyReport
        fields = ('score', 'emotion', 'date', 'user_emotion')

class WeeklyDateSerializer(serializers.Serializer):
    start = serializers.DateField()
    end = serializers.DateField()

class MonthlyDateSerializer(serializers.Serializer):
    year = serializers.CharField()
    month = serializers.CharField()
