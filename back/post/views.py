import json
import requests
import copy
import datetime
from pprint import pprint

from django.shortcuts import render, get_object_or_404
from django.core.cache import cache

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
from text.views import redis_check


class DiaryMixin:
    def create_sticker(self, stickers, post_id):
        for sticker in stickers:
            sticker['post'] = post_id
            sticker_serializer = PostStickerSerializer(data=sticker)
            sticker_serializer.is_valid(raise_exception=True)
            sticker_serializer.save()
        post = get_object_or_404(Post, pk=post_id)
        return post

def get_date(today):
    return map(int, today.split('-'))

def get_start_day(today):
    year, month, day = map(int, today.split('-'))
    today = datetime.date(year, month, day)
    for delta in range(7):
        date = today - datetime.timedelta(days=delta)
        if date.weekday() == 6:
            break
    return date

def delete_week_cache(today, user_id):
    startday = get_start_day(f'{today.year}-{today.month}-{today.day}')
    if redis_check():
        cache.delete(f'w-u{user_id}-s{startday.year}-{startday.month}-{startday.day}')

def delete_month_cache(today, user_id):
    year = today.year
    month = today.month
    if redis_check():
        cache.delete(f'm-u{user_id}-{year}-{month}')
    
class CreateDiary(APIView, DiaryMixin):

    parser_classes = (FormParser, MultiPartParser, )
    permission_classes = (IsAuthenticated, )

    TEXT_ANALYZER_PORT = 9002
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
        print(f'<post request : user {request.user} | title {request.data.get("title")}>')
        date = request.data['created']
        stickers = json.loads(request.data.get('stickers', '[]'))
        if Post.objects.filter(created=date, user=request.user).exists():
            msg = {
                'detail': '해당 날짜에 쓴 글이 존재합니다.'
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.dict()

        image = request.data.get('image')
        sticker_image = request.data.get('sticker_image')
        if request.data.get('search_music'):
            search_music = json.loads(request.data.get('search_music'))
            if search_music == {}:
                search_music = None
                data['search_music'] = None
            else:
                data['search_music'] = search_music
        else:
            search_music = None
        print('test1')
        recommend_music = request.data.get('recommend_music')
        if not (search_music or recommend_music):
            msg = {
                'detail': '음악 정보가 존재하지 않습니다.'
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        if image:
            del data['image']
        if sticker_image:
            del data['sticker_image']
        if search_music:
            del data['search_music']
        if recommend_music:
            del data['recommend_music']
        print('test')
        serializer = CreatePostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(user=request.user)

        self.create_sticker(stickers, post.id)
        response = self.analyze(request.user, data, post.id)
        response = json.loads(response.text)
        print(response)        

        data['image'] = image
        data['sticker_image'] = sticker_image
        data['report_id'] = response['id']
        if search_music:
            search_music_data = search_music
            search_music_data['post'] = post.id
            search_music_data['user'] = request.user.id
            search_music_serializer = SearchMusicSerializer(data=search_music_data)
            search_music_serializer.is_valid(raise_exception=True)
            search_music = search_music_serializer.save()
        else:
            recommend_music = get_object_or_404(RecommendMusic, pk=int(recommend_music))

        serializer = CreatePostSerializer(instance=post, data=data)
        serializer.is_valid(raise_exception=True)
        report = get_object_or_404(DailyReport, pk=response['id'])
        post = serializer.save(report=report, search_music=search_music, recommend_music=recommend_music)
        
        year, month, day = get_date(date)
        date = datetime.date(year, month, day)
        delete_week_cache(date, request.user.id)
        delete_month_cache(date, request.user.id)
        msg = {
            'id': post.id,
            'detail': '작성이 완료되었습니다.'
        }
        return Response(msg, status=status.HTTP_201_CREATED)


class diary(APIView, DiaryMixin):

    parser_classes = (FormParser, MultiPartParser, )
    permission_classes = (IsAuthenticated, )

    def get_object(self, post_id):
        return get_object_or_404(Post, pk=post_id)
        
    def get(self, request, post_id):
        mypost = self.get_object(post_id)
        if mypost.user.id == request.user.id:
            serializer = ReadPostSerializer(instance=mypost)
            result = serializer.data
            if result.get('search_music', None):
                result['search_music']['liked'] = request.user.search_like.filter(video_id=result['search_music']['video_id']).exists()
            else:
                music = result['recommend_music']
                result['recommend_music']['liked'] = request.user.recommend_like.filter(pk=music['id']).exists()
            return Response(result, status=status.HTTP_200_OK)
        msg = {
            'detail': '유효하지 않은 사용자입니다.'
        }
        return Response(msg, status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, post_id):
        mypost = self.get_object(post_id)
        if request.user.id == mypost.user.id:
            print(f'<delete request : user {request.user} post {mypost}')
            date = mypost.created
            mypost.delete()
            delete_month_cache(date, request.user.id)
            msg = {
                'detail': '삭제되었습니다.'
            }
            return Response(msg, status=status.HTTP_200_OK)
        msg = {
            'detail': '권한이 없습니다.'
        }
        return Response(msg, status=status.HTTP_403_FORBIDDEN)


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
    for path, preview in [(None, 'images/paper/1_preview.png'),('images/paper/2.png', 'images/paper/2_preview.png'), ('images/paper/3.png', 'images/paper/3_preview.png'), ('images/paper/4.png', 'images/paper/4.png'), ('images/paper/5.png', 'images/paper/5.png'), ('images/paper/6.png', 'images/paper/6.png')]:
        Pattern.objects.create(path=path, preview_path=preview)

    return Response({
        'message': 'success'
    }, status=status.HTTP_201_CREATED)

        
