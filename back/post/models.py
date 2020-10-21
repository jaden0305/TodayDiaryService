from django.db import models
from django.conf import settings


class PostColor(models.Model):
    value = models.CharField(max_length=100)

class PostFont(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

class Pattern(models.Model):
    path = models.CharField(max_length=100)

class Emotion(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

class Sticker(models.Model):
    path = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class StickerTag(models.Model):
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    postcolor = models.ForeignKey(PostColor, on_delete=models.CASCADE)
    font = models.ForeignKey(PostFont, on_delete=models.CASCADE)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    fontsize = models.IntegerField()
    music = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)

class PostImage(models.Model):
    path = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostSticker(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    width = models.IntegerField()
    deg = models.IntegerField()
    top = models.IntegerField()
    left = models.IntegerField()