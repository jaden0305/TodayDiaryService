from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from post.models import RecommendMusic


class User(AbstractUser):
    likes = models.ManyToManyField(RecommendMusic,related_name='like_user')
