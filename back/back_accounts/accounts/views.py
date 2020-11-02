from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from .serializers import UserSerializer, CheckEmailSerializer


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


@swagger_auto_schema(methods=['get'], query_serializer=CheckEmailSerializer)
@api_view(['GET'])
def check_email(request):
    email = request.GET.get('email', None)
    if email is None:
        msg = "잘못된 요청입니다."
        return Response({
            'msg': msg
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        is_exist = User.objects.filter(email=email).exists()
        if is_exist:
            return Response({
                'exist': is_exist,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'exist': is_exist
            }, status=status.HTTP_204_NO_CONTENT)