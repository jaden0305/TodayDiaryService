from rest_framework import serializers

# from accounts.serializers import UserSerializer
from .models import *

class WordCloudReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCloudReport
        fields = ('word', 'count', 'emotion')

class MultipleEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('emotions', 'date')

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('score', 'emotion', 'date')

class WeeklyDateSerializer(serializers.Serializer):
    start = serializers.DateField()
    end = serializers.DateField()

class MonthlyDateSerializer(serializers.Serializer):
    year = serializers.CharField()
    month = serializers.CharField()
