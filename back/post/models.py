from uuid import uuid4
import datetime

from django.db import models
from django.conf import settings

from text.models import DailyReport


def upload_location(instance, filename):
    name, ext = filename.split('.')
    now = datetime.datetime.now()
    return f"{now.year}/{now.month}/{now.day}/{uuid4()}.{ext}"

def upload_sticker_location(instance, filename):
    return 'sticker_' + upload_location(instance, filename)


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
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=30, blank=True, null=True)
    video_id = models.CharField(max_length=20)
    cover = models.TextField(blank=True, null=True)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name='musics')


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    search_music = models.ForeignKey('SearchMusic', on_delete=models.CASCADE, null=True, related_name='search_music')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    font = models.ForeignKey(PostFont, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    report = models.ForeignKey('text.DailyReport', on_delete=models.CASCADE, blank=True, null=True, related_name='posts')
    recommend_music = models.ForeignKey(RecommendMusic, on_delete=models.CASCADE, null=True, related_name='recommend_music')
    created = models.DateField()
    user_emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(blank=True, null=True, upload_to=upload_location)
    sticker_image = models.ImageField(blank=True, null=True, upload_to=upload_sticker_location, default=None)


class SearchMusic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='search_music')
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=30, blank=True, null=True)
    video_id = models.CharField(max_length=20)
    cover = models.TextField(blank=True, null=True)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, related_name='search_musics')
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='post')


class PostSticker(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='stickers')
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    width = models.CharField(max_length=20)
    rotation = models.CharField(max_length=20)
    y = models.CharField(max_length=20)
    x = models.CharField(max_length=20)
