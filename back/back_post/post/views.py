import json
import requests

from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class CreateDiary(APIView):

    parser_classes = (FormParser, MultiPartParser, )
    permission_classes = (AllowAny, )

    TEXT_ANALYZER_PORT = 8002
    TEXT_ANALYZER_REQUEST_PATH = '/text/'

    def analyze(self, user, text, date, post_id):
        payload = {
            'user': user,
            'text': text,
            'date': date,
            'post_id': post_id,
        }
        url = f'http://127.0.0.1:{self.TEXT_ANALYZER_PORT}{self.TEXT_ANALYZER_REQUEST_PATH}'
        response = requests.post(url, data=payload)

        return json.loads(response.text)


        
    # [{"post":1,"sticker":1,"width":0,"deg":0,"top":0,"left":99},{"post":1,"sticker":1,"width":1,"deg":0,"top":0,"left":0}]
    @swagger_auto_schema(request_body=CreatePostSerializer)
    def post(self, request, format=None):
        serializer = CreatePostSerializer(data=request.data)
        response = None
        if serializer.is_valid(raise_exception=True):
            # emotion = AI 분석
            # music = emotion 통한 추천
            p = serializer.save(user=request.user)

            text = request.data['content']
            date = request.data['created']

            try:
                response = self.analyze(request.user.id, text, date, p.id)
                print(response)
                emotion = 0
            except:
                emotion = None
                print('error')

            stickers = json.loads(request.data.get('stickers','[]'))
            for sticker in stickers:
                sticker['post'] = p.id
                sticker_serializer = PostStickerSerializer(data=sticker)
                if sticker_serializer.is_valid(raise_exception=True):
                    sticker_serializer.save()
            post = get_object_or_404(Post, pk=p.id)
            return Response(ReadPostSerializer(instance=post).data, status=status.HTTP_201_CREATED)


class diary(APIView):
    
    def get_object(self, post_id):
        return get_object_or_404(Post, pk=post_id)
        
    def get(self, request, post_id):
        mypost = self.get_object(post_id)
        serializer = ReadPostSerializer(instance=mypost)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # [{"id":1,"post":1,"sticker":1,"width":0,"deg":0,"top":0,"left":22},{"id":2, "post":1,"sticker":1,"width":23,"deg":0,"top":0,"left":0}]
    @swagger_auto_schema(request_body=UpdatePostSerializer)
    def put(self, request, post_id):
        mypost = self.get_object(post_id)
        serializer = UpdatePostSerializer(instance=mypost,data=request.data)
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