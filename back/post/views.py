from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

class diary(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=post_id)

    def post(self, request, format=None):
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # emotion = AI 분석
            # music = emotion 통한 추천
            serializer.save()
            return Response(serializer.data)
        
    def get(self, request, post_id):
        mypost = self.get_object(post_id)
        serializer = ReadPostSr(instance = mypost)
        return Response(serializer.data)

    def put(self, request):
        serializer = UpdatePostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, post_id):
        mypost = self.get_object(post_id)
        mypost.delete()
        
        msg = {
            "detail": "오늘 하루가 사라졌습니다."
        }

        return Response(msg, status=status.HTTP_200_OK)
