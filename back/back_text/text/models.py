from django.db import models
from django.conf import settings

from post.models import Post, Emotion


class WordCloudReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField()
    emotion = models.IntegerField()
    date = models.DateField()


class DailyReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
    score = models.FloatField()
    emotions = models.TextField()
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# class WeeklyReport(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
#     score = models.FloatField()
#     emotions = models.TextField()
#     emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
#     date = models.DateField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

# class MonthlyReport(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
#     score = models.FloatField()
#     emotions = models.TextField()
#     emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
#     date = models.DateField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

# class TotalReport(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
#     score = models.FloatField()
#     emotions = models.TextField()
#     emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
#     date = models.DateField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)