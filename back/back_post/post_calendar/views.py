import datetime

from dateutil.relativedelta import relativedelta

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from .common import date_to_dict
from .serializers import CalendarQuerySerializer


class CalendarView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(query_serializer=CalendarQuerySerializer)
    def get(self, request):

        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))

        if year and month:
            calendar_info = date_to_dict(year, month)

            now = datetime.date(year, month, 1)
            pre = (now - relativedelta(months=1)).month
            nex = (now + relativedelta(months=1)).month
            
            has_before = calendar_info[pre][0]
            if  has_before:
                start_month = pre
                start_day = has_before[0]['day']
            else:
                start_month = now.month
                start_day = 1
            
            has_next = calendar_info[nex][-1]
            if has_next:
                end_month = nex
                end_day = has_next[-1]['day']
            else:
                end_month = now.month
                end_day = has_next[-1]['day']

            print('start', start_month, start_day)
            print('end', end_month, end_day)
            

            return Response(calendar_info, status=status.HTTP_200_OK)
        message = {
            'deatail': '년도 또는 월 정보가 누락되었습니다.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
