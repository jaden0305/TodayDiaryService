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
        
