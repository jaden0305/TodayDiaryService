from rest_framework import serializers
from .models import *

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', 'user', 'created',)

class ReadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', 'user',)

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', 'user', 'created',)