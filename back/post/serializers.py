from rest_framework import serializers

from accounts.serializers import UserSerializer
from text.serializers import DailyReportSerializer
from .models import *


class RecommandMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendMusic
        fields = '__all__'

        
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


class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = '__all__'
        depth = 2


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagStickerSerializer(serializers.ModelSerializer):
    stickers = StickerSerializer(many=True)
    class Meta:
        model = Tag
        fields = ('id', 'name', 'stickers')
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
    image = serializers.ImageField(required=False, allow_null=True)
    sticker_image = serializers.ImageField(required=False, allow_null=True)
    search_music = serializers.CharField(required=False, allow_null=True)
    recommend_music = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model = Post
        exclude = ('id', 'user',)


class ReadPostSerializer(serializers.ModelSerializer):
    stickers = PostStickerReadSerializer(many=True)
    report = DailyReportSerializer()
    class Meta:
        model = Post
        exclude = ('user', 'created')
        depth = 1

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', 'user', 'created', 'report', 'recommend_music',)
    

class SearchMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchMusic
        fields = '__all__'