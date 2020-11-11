from django.db import models
from django.conf import settings


class WordCloudReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField()
    emotion = models.IntegerField() # 1, 0, -1
    date = models.DateField()


class DailyReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='text_reports')
    score = models.FloatField()
    emotion = models.ForeignKey('post.Emotion', on_delete=models.CASCADE, null=True)
    date = models.DateField()

"""
happy 2 sad 2  -> score에 양수인지 음수인지보고 
happy 2 delight 2 -> 

"""