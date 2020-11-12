from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from post.models import RecommendMusic, SearchMusic


class User(AbstractUser):
    recommend_like = models.ManyToManyField(RecommendMusic, related_name='recommend_like_music')
    search_like = models.ManyToManyField(SearchMusic, related_name='search_like_music')