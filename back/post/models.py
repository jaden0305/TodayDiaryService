from uuid import uuid4
import datetime

from django.db import models
from django.conf import settings

from text.models import DailyReport


def upload_location(instance, filename):
    name, ext = filename.split('.')
    now = datetime.datetime.now()
    return f"{now.year}/{now.month}/{now.day}/{uuid4()}.{ext}"


class PostColor(models.Model):
    value = models.CharField(max_length=20)


class PostFont(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
        

class Pattern(models.Model):
    path = models.CharField(max_length=100, blank=True, null=True)
    preview_path = models.CharField(max_length=100, blank=True, null=True)


class Emotion(models.Model):
    name = models.CharField(max_length=30)
    path = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Sticker(models.Model):
    path = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="stickers")
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name='stickers', blank=True, null=True)


class RecommendMusic(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=30, blank=True, null=True)
    video_id = models.CharField(max_length=20)
    cover = models.TextField(blank=True, null=True)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name='musics')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    postcolor = models.ForeignKey(PostColor, on_delete=models.CASCADE)
    font = models.ForeignKey(PostFont, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    report = models.ForeignKey('text.DailyReport', on_delete=models.CASCADE, blank=True, null=True, related_name='posts')
    fontsize = models.IntegerField()
    upload_music = models.FileField(blank=True, null=True, upload_to=upload_location)
    recommend_music = models.ForeignKey(RecommendMusic, on_delete=models.CASCADE, null=True)
    created = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_location)


class PostSticker(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='stickers')
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    width = models.CharField(max_length=20)
    deg = models.CharField(max_length=20)
    top = models.CharField(max_length=20)
    left = models.CharField(max_length=20)