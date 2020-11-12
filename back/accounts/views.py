
import random

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from post.models import RecommendMusic, SearchMusic

from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from post.serializers import RecommandMusicSerializer, SearchMusicSerializer


User = get_user_model()


class UserDetailView(APIView):
    
    def get_object(self, user_id):
        return get_object_or_404(User, pk=user_id)
    
    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
    def delete(self, request, user_id):
        user = self.get_object(user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(methods=['post'], request_body=CheckEmailSerializer)
@api_view(['POST'])
def check_email(request):
    email = request.data.get('email', None)
    exist = User.objects.filter(email=email).exists()
    if exist:
        state = status.HTTP_200_OK
    else:
        state = status.HTTP_204_NO_CONTENT
    
    return Response(status=state)


class MusicView(APIView):

    @swagger_auto_schema()
    def get(self, request):
        recommend_music = request.user.recommend_like.all()
        search_music = request.user.search_like.all()

        result = []

        recommend_music_serializer = LikeMusicSerializer(instance=recommend_music, many=True)
        search_music_serializer = LikeMusicSerializer(instance=search_music, many=True)
        
        for music in recommend_music_serializer.data:
            music = dict(music)
            music['liked'] = True
            result.append(music)
        
        for music in search_music_serializer.data:
            music = dict(music)
            music['liked'] = True
            result.append(music)

        random.shuffle(result)

        return Response(result, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=LikeSerializer)
    def post(self, request):
        pk = request.data['music_id']
        recommend = request.data['favorited']
        
        if recommend:
            music = get_object_or_404(RecommendMusic, pk=pk)
            if request.user in music.recommend_like_music.all():
                music.recommend_like_music.remove(request.user)
                msg = {
                    'detail' : '좋아요 취소' 
                }
                return Response(msg, status=status.HTTP_200_OK)
            else:
                music.recommend_like_music.add(request.user)
                msg = {
                    'detail' : '좋아요' 
                }
                return Response(msg, status=status.HTTP_200_OK)
        else:
            music = get_object_or_404(SearchMusic, pk=pk)

            if request.user in music.search_like_music.all():
                music.search_like_music.remove(request.user)
                msg = {
                    'detail' : '좋아요 취소' 
                }
                return Response(msg, status=status.HTTP_200_OK)
            else:
                music.search_like_music.add(request.user)
                msg = {
                    'detail' : '좋아요' 
                }
                return Response(msg, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def likes_music(request):
#     recommend_music = request.user.recommend_like.all()
#     search_music = request.user.search_like.all()

#     result = []

#     recommend_music_serializer = LikeMusicSerializer(instance=recommend_music, many=True)
#     search_music_serializer = LikeMusicSerializer(instance=search_music, many=True)
    
#     for music in recommend_music_serializer.data:
#         music = dict(music)
#         music['liked'] = True
#         result.append(music)
    
#     for music in search_music_serializer.data:
#         music = dict(music)
#         music['liked'] = True
#         result.append(music)

#     random.shuffle(result)

#     return Response(result, status=status.HTTP_200_OK)

@swagger_auto_schema()
@api_view(['GET'])
def my_music(request):
    posts = request.user.posts.all()
    search_music = SearchMusic.objects.filter(user=request.user).all()

    result = []
    for post in posts:
        music= post.recommend_music
        if music:
            music_data = RecommandMusicSerializer(instance=music).data
            music_data['liked'] = request.user.recommend_like.filter(pk=music.id).exists()
            result.append(music_data)
    
    for music in search_music:
        print(music)
        music_data = SearchMusicSerializer(instance=music).data
        music_data['liked'] = request.user.search_like.filter(video_id=music.video_id).exists()
        result.append(music_data)
    
    return Response(result, status=status.HTTP_200_OK)

# @swagger_auto_schema(methods=['post'], request_body=LikeSerializer)
# @api_view(['POST'])
# def like(request):
#     pk = request.data['music_id']
#     recommend = request.data['favorited']
    
#     if recommend:
#         music = get_object_or_404(RecommendMusic, pk=pk)
#         if request.user in music.recommend_like_music.all():
#             music.recommend_like_music.remove(request.user)
#             msg = {
#                 'detail' : '좋아요 취소' 
#             }
#             return Response(msg, status=status.HTTP_200_OK)
#         else:
#             music.recommend_like_music.add(request.user)
#             msg = {
#                 'detail' : '좋아요' 
#             }
#             return Response(msg, status=status.HTTP_200_OK)
#     else:
#         music = get_object_or_404(SearchMusic, pk=pk)

#         if request.user in music.search_like_music.all():
#             music.search_like_music.remove(request.user)
#             msg = {
#                 'detail' : '좋아요 취소' 
#             }
#             return Response(msg, status=status.HTTP_200_OK)
#         else:
#             music.search_like_music.add(request.user)
#             msg = {
#                 'detail' : '좋아요' 
#             }
#             return Response(msg, status=status.HTTP_200_OK)