from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from .common import date_to_dict
from .serializers import CalendarQuerySerializer


@swagger_auto_schema(methods=['get'], query_serializer=CalendarQuerySerializer)
@api_view(['GET'])
def get_calendar_info(request):
    year = request.GET.get('year')
    month = request.GET.get('month')

    if year and month:
        calendar_info = date_to_dict(year, month)
        return Response(calendar_info, status=status.HTTP_200_OK)
    message = {
        'deatail': '년도 또는 월 정보가 누락되었습니다.'
    }
    return Response(message, status=status.HTTP_400_BAD_REQUEST)