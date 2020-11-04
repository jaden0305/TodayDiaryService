from rest_framework import serializers

from post.serializers import EmotionSerializer


class CalendarQuerySerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()

