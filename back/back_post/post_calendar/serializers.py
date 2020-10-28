from rest_framework import serializers


class CalendarQuerySerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()