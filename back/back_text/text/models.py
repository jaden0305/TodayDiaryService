from django.db import models
from django.conf import settings

from post.models import Post, Emotion


class WordCloudReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField()
    emotion = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'text_wordcloudreport'


class DailyReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
    score = models.FloatField()
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, null=True)
    user_emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, blank=True, null=True, related_name='daily_report')
    date = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        db_table = 'text_dailyreport'