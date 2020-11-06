import json
import requests

from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class CreateDiary(APIView):

    parser_classes = (FormParser, MultiPartParser, )
    permission_classes = (IsAuthenticated, )

    TEXT_ANALYZER_PORT = 8002
    TEXT_ANALYZER_REQUEST_PATH = '/text/'
    TEXT_ANALYZER_HOST = 'http://127.0.0.1'

    def analyze(self, user, text, date, post_id):
        payload = {
            'user': user,
            'text': text,
            'date': date,
            'post_id': post_id,
        }
        url = f'{self.TEXT_ANALYZER_HOST}:{self.TEXT_ANALYZER_PORT}{self.TEXT_ANALYZER_REQUEST_PATH}'
        print(url)
        response = requests.post(url, data=payload)
        print(response)
        return json.loads(response.text)
    

    # [{"post":1,"sticker":1,"width":0,"deg":0,"top":0,"left":99},{"post":1,"sticker":1,"width":1,"deg":0,"top":0,"left":0}]
    @swagger_auto_schema(request_body=CreatePostSerializer)
    def post(self, request, format=None):
        print(request.data)
        data = request.data
        if data.get('image'):
            del data['image']
        serializer = CreatePostSerializer(data=request.data)
        response = None

        if serializer.is_valid(raise_exception=True):
            # emotion = AI 분석
            # music = emotion 통한 추천
            p = serializer.save(user=request.user)

            text = request.data['content']
            date = request.data['created']

            response = self.analyze(request.user.id, text, date, p.id)
            
            serializer = CreatePostSerializer(instance=get_object_or_404(Post, pk=p.id), data=request.data)
            serializer.is_valid(raise_exception=True)
            p = serializer.save(report=DailyReport.objects.get(pk=response['id']))

            stickers = json.loads(request.data.get('stickers','[]'))
            for sticker in stickers:
                sticker['post'] = p.id
                sticker_serializer = PostStickerSerializer(data=sticker)
                sticker_serializer.is_valid(raise_exception=True)
                sticker_serializer.save()
            post = get_object_or_404(Post, pk=p.id)
            result = {
                **ReadPostSerializer(instance=post).data
            }
            return Response(result, status=status.HTTP_201_CREATED)


class diary(APIView):
    
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

        data = {}
        for key, value in request.data.items():
            print(key, value)
            res = value
            if key in ['postcolor', 'font', 'pattern']:
                res = int(value)
            data[key] = res

        serializer = UpdatePostSerializer(instance=mypost,data=data)

        stickers = json.loads(request.data.get('stickers', '[]'))

        for sticker in stickers:
            sticker_id = sticker['id']
            post_sticker = PostSticker.objects.get(pk=sticker_id)
            poststicker_serializer = PostStickerSerializer(instance=post_sticker, data=sticker)
            if poststicker_serializer.is_valid(raise_exception=True):
                poststicker_serializer.save()

        if serializer.is_valid(raise_exception=True):
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
    font_list = ['Gaegu', 'Nanum Myeongjo', 'Nanum Pen Script', 'Poor Story', 'Nanum Gothic']
    for font in font_list:
        PostFont.objects.create(name=font, path='')

    # emotion
    for name in ['happy', 'sad', 'delight', 'boring', 'angry', 'surprise', 'horror']:
        Emotion.objects.create(name=name)
    
    # pattern
    for path, preview in [(None, 'media/paper/1_preview.png'),('media/paper/2.png', 'media/paper/2_preview.png'), ('media/paper/3.png', 'media/paper/3_preview.png'), ('media/paper/4.png', 'media/paper/4.png'), ('media/paper/5.png', 'media/paper/5.png'), ('media/paper/6.png', 'media/paper/6.png')]:
        Pattern.objects.create(path=path, preview_path=preview)

    return Response({
        'message': 'success'
    }, status=status.HTTP_201_CREATED)

        