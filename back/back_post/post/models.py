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
    value = models.CharField(max_length=100)

    @classmethod
    def make(cls):
        PostColor.objects.create(value='test')


class PostFont(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)
    @classmethod
    def make(cls):
        font_list = ['Gaegu', 'Nanum Gothic', 'Nanum Myeongjo', 'Nanum Pen Script', 'Poor Story']
        for font in font_list:
            PostFont.objects.create(name=font, path='')
        

class Pattern(models.Model):
    path = models.CharField(max_length=100)

    @classmethod
    def make(cls):
        Pattern.objects.create(path='test')


class Emotion(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    @classmethod
    def make(cls):
        for name in ['happy', 'sad', 'delight', 'boring', 'angry', 'surprise', 'horror']:
            Emotion.objects.create(name=name)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Sticker(models.Model):
    path = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name="stickers")
    score = models.FloatField()
    emotion = models.IntegerField()


class RecommendMusic(models.Model):
    music_name = models.TextField()
    music_artist = models.TextField()
    path = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    postcolor = models.ForeignKey(PostColor, on_delete=models.CASCADE)
    font = models.ForeignKey(PostFont, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, blank=True, null=True, related_name='posts')
    fontsize = models.IntegerField()
    upload_music = models.FileField(blank=True, null=True, upload_to=upload_location)
    recommend_music = models.ForeignKey(RecommendMusic, on_delete=models.CASCADE, null=True)
    created = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to=upload_location)


class PostSticker(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='stickers')
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    width = models.IntegerField()
    deg = models.IntegerField()
    top = models.IntegerField()
    left = models.IntegerField()