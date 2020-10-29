from rest_framework import serializers

# from accounts.serializers import UserSerializer
from .models import *

class WordCloudReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordCloudReport
        fields = '__all__'

class MultipleEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('emotions', 'date')

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ('score', 'emotion', 'date')
