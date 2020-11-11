import json
import requests
import copy
from pprint import pprint

from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import QueryDict
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class DiaryMixin:
    def create_sticker(self, stickers, post_id):
        for sticker in stickers:
            sticker['post'] = post_id
            sticker_serializer = PostStickerSerializer(data=sticker)
            sticker_serializer.is_valid(raise_exception=True)
            sticker_serializer.save()
        post = get_object_or_404(Post, pk=post_id)
        return post


class CreateDiary(APIView, DiaryMixin):

    parser_classes = (FormParser, MultiPartParser, )
    permission_classes = (IsAuthenticated, )

    TEXT_ANALYZER_PORT = 8002
    TEXT_ANALYZER_REQUEST_PATH = '/text/'
    TEXT_ANALYZER_HOST = 'http://127.0.0.1'

    POST_EXCLUDES = ('image', 'stickers')

    def analyze(self, user, data, post_id):
        payload = {
            'title': data.get('title'),
            'user': user.id,
            'text': data.get('content'),
            'date': data.get('created'),
            'post': post_id,
        }
        url = f'{self.TEXT_ANALYZER_HOST}:{self.TEXT_ANALYZER_PORT}{self.TEXT_ANALYZER_REQUEST_PATH}'

        response = requests.post(url, data=payload)
        return response

    # [{"sticker":1,"width":0,"deg":0,"top":0,"left":99},{"sticker":1,"width":1,"deg":0,"top":0,"left":0}]
    @swagger_auto_schema(request_body=CreatePostSerializer)
    def post(self, request, format=None):
        date = request.data['created']
        stickers = json.loads(request.data.get('stickers', '[]'))
        if Post.objects.filter(created=date, user=request.user).exists():
            msg = {
                'detail': '해당 날짜에 쓴 글이 존재합니다.'
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.dict()
        exclude_data = {}
        image = request.data.get('image')
        search_music = request.data.get('search_music')
        recommend_music = request.data.get('recommend_music')
        if not (search_music or recommend_music):
            msg = {
                'detail': '음악 정보가 존재하지 않습니다.'
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            
        if image:
            del data['image']
            exclude_data['image'] = image
        if search_music:
            del data['search_music']
            exclude_data['search_music'] = search_music
        if recommend_music:
            del data['recommend_music']
            exclude_data['recommend_music'] = recommend_music

        serializer = CreatePostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(user=request.user)

        self.create_sticker(stickers, post.id)
        response = self.analyze(request.user, data, post.id)
        response = json.loads(response.text)

        data['image'] = image
        data['report_id'] = response['id']
        if search_music:
            search_music_data = json.loads(search_music)
            search_music_data['post'] = post.id
            search_music_data['emotion'] = response['emotion']['id']
            search_music_serializer = SearchMusicSerializer(data=search_music_data)
            search_music_serializer.is_valid(raise_exception=True)
            search_music = search_music_serializer.save()
        else:
            recommend_music = get_object_or_404(RecommendMusic, pk=int(recommend_music))

        serializer = CreatePostSerializer(instance=post, data=data)
        serializer.is_valid(raise_exception=True)
        report = get_object_or_404(DailyReport, pk=response['id'])
        post = serializer.save(report=report, search_music=search_music, recommend_music=recommend_music)


class diary(APIView, DiaryMixin):

    parser_classes = (FormParser, MultiPartParser, )
    permission_classes = (IsAuthenticated, )

    def get_object(self, post_id):
        return get_object_or_404(Post, pk=post_id)
        
    def get(self, request, post_id):
        mypost = self.get_object(post_id)
        if mypost.user.id == request.user.id:
            serializer = ReadPostSerializer(instance=mypost)
            return Response(serializer.data, status=status.HTTP_200_OK)
        msg = {
            'detail': '유효하지 않은 사용자입니다.'
        }
        return Response(msg, status=status.HTTP_403_FORBIDDEN)

    # [{"id":1,"post":1,"sticker":1,"width":0,"deg":0,"top":0,"left":22},{"id":2, "post":1,"sticker":1,"width":23,"deg":0,"top":0,"left":0}]
    @swagger_auto_schema(request_body=UpdatePostSerializer)
    def put(self, request, post_id):
        mypost = self.get_object(post_id)

        serializer = UpdatePostSerializer(instance=mypost,data=request.data)
        serializer.is_valid(raise_exception=True)

        # 기존 스티커 삭제
        my_stickers = mypost.stickers.all()
        for sticker in my_stickers:
            sticker.delete()

        stickers = json.loads(request.data.get('stickers', '[]'))
        self.create_sticker(stickers, mypost.id)

        p = serializer.save()
        return Response(ReadPostSerializer(instance=p).data, status=status.HTTP_200_OK)
    
    def delete(self, request, post_id):
        mypost = self.get_object(post_id)
        mypost.delete()
        
        msg = {
            "detail": "오늘 하루가 사라졌습니다."
        }

        return Response(msg, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(['GET'])
def get_fonts(request):
    fonts = PostFont.objects.all()
    serializer = PostFontSerializer(instance=fonts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(['GET'])
def get_patterns(request):
    patterns = Pattern.objects.all()
    serializer = PatternSerializer(instance=patterns, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema()
@api_view(['GET'])
def get_colors(request):
    colors = PostColor.objects.all()
    serializer = PostColorSerializer(instance=colors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

@swagger_auto_schema()
@api_view(['GET'])
def get_all_sticker(request):
    tags = Tag.objects.all()
    serializer = TagStickerSerializer(instance=tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema()
@api_view(['GET'])
def written(request):
    post = Post.objects.filter(user=request.user).exists()
    if post:
        return Response(True, status=status.HTTP_200_OK)
    else:
        return Response(False, status=status.HTTP_200_OK)    

@api_view(['POST'])
def make_test(request):
    
    if PostColor.objects.filter(id=1).exists():
        return Response({
            'message': '이미 존재합니다.'
        }, status=status.HTTP_400_BAD_REQUEST)
    # color
    color_list = ['#fff5f5', '#fff0f6', '#f8f0fc', '#f3f0ff', '#edf2ff', '#e7f5ff', '#e6fcf5', '#ebfbee', '#fff9db', '#fff4e6']
    for color in color_list:
        PostColor.objects.create(value=color)
    
    # font
    font_list = ['Poor Story', 'Nanum Myeongjo', 'Nanum Pen Script', 'Gaegu', 'Nanum Gothic']
    for font in font_list:
        PostFont.objects.create(name=font, path='')

    # emotion
    for name in ['happy', 'sad', 'delight', 'boring', 'angry', 'surprise', 'horror', 'no_emotion']:
        Emotion.objects.create(name=name)
    
    # pattern
    for path, preview in [(None, 'media/paper/1_preview.png'),('media/paper/2.png', 'media/paper/2_preview.png'), ('media/paper/3.png', 'media/paper/3_preview.png'), ('media/paper/4.png', 'media/paper/4.png'), ('media/paper/5.png', 'media/paper/5.png'), ('media/paper/6.png', 'media/paper/6.png')]:
        Pattern.objects.create(path=path, preview_path=preview)
    
    for i in range(1, 8):
        RecommendMusic.objects.create(title='test', artist='test', video_id='test', cover='test', emotion_id=i)

    return Response({
        'message': 'success'
    }, status=status.HTTP_201_CREATED)

        