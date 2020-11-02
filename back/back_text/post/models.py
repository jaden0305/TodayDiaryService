from uuid import uuid4
import datetime

from django.db import models
from django.conf import settings


def upload_location(instance, filename):
    name, ext = filename.split('.')
    now = datetime.datetime.now()
    return f"{now.year}/{now.month}/{now.day}/{uuid4()}.{ext}"


class PostColor(models.Model):
    value = models.CharField(max_length=100)
    class Meta:
        db_table = 'post_postcolor'


class PostFont(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    class Meta:
        db_table = 'post_postfont'


class Pattern(models.Model):
    path = models.CharField(max_length=100)
    class Meta:
        db_table = 'post_pattern'


class Emotion(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    class Meta:
        db_table = 'post_emotion'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'post_tag'


class Sticker(models.Model):
    path = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name="stickers")
    class Meta:
        db_table = 'post_sticker'


class RecommendMusic(models.Model):
    music_name = models.TextField()
    music_artist = models.TextField()
    path = models.TextField()
    class Meta:
        db_table = 'post_recommendmusic'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    postcolor = models.ForeignKey(PostColor, on_delete=models.CASCADE)
    font = models.ForeignKey(PostFont, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE, blank=True, null=True)
    fontsize = models.IntegerField()
    upload_music = models.FileField(blank=True, null=True, upload_to=upload_location)
    recommend_music = models.ForeignKey(RecommendMusic, on_delete=models.CASCADE, null=True)
    created = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_location)
    class Meta:
        db_table = 'post_post'


class PostSticker(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='stickers')
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    width = models.IntegerField()
    deg = models.IntegerField()
    top = models.IntegerField()
    left = models.IntegerField()
    class Meta:
        db_table = 'post_poststicker'