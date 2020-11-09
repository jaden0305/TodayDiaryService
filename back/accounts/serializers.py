from django.contrib.auth import get_user_model
from rest_framework import serializers

from post.models import RecommendMusic

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )
    

class CheckEmailSerializer(serializers.Serializer):
    email = serializers.CharField()


class LikeSerializer(serializers.Serializer):
    music_id = serializers.IntegerField()

class LikeMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendMusic
        fields = '__all__'
