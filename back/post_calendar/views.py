from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .common import date_to_dict


@api_view(['GET'])
def get_calendar_info(request):
    year = int(request.GET.get('year'), None)
    month = int(request.GET.get('month'), None)

    calendar_info = date_to_dict(year, month)

    if year and month:
        return Response(calendar_info, status=status.HTTP_200_OK)
    message = {
        'deatail': '년도 또는 월 정보가 누락되었습니다.'
    }
    return Response(message, status=status.HTTP_400_BAD_REQUEST)