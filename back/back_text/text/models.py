from django.db import models
from django.conf import settings

from post.models import Post


class WordCloudReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField()
    emotion = models.IntegerField()
    date = models.DateField()


class TextReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
    score = models.FloatField()
    emotions = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
