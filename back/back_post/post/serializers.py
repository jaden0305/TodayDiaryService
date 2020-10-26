from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import *


class PostColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostColor
        fields = '__all__'


class PostFontSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFont
        fields = '__all__'


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = '__all__'


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = '__all__'
        depth = 2


class PostStickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSticker
        fields = '__all__'


class PostStickerReadSerializer(serializers.ModelSerializer):
    sticker = StickerSerializer()
    class Meta:
        model = PostSticker
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    # stickers = serializers.ListField(required=False)
    class Meta:
        model = Post
        exclude = ('id', 'user')


class ReadPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    postcolor = PostColorSerializer()
    font = PostFontSerializer()
    pattern = PatternSerializer()
    emotion = EmotionSerializer()
    stickers = PostStickerReadSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', 'user', 'created',)