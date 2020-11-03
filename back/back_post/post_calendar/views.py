import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from .common import date_to_dict
from .serializers import CalendarQuerySerializer
from post.models import Post


class CalendarView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(query_serializer=CalendarQuerySerializer)
    def get(self, request):

        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))

        if year and month:
            calendar_info = date_to_dict(year, month)

            now = datetime.date(year, month, 1)
            pre = (now - relativedelta(months=1))
            nex = (now + relativedelta(months=1))
            
            has_before = calendar_info[pre.month][0]
            if  has_before:
                start_year = pre.year
                start_month = pre.month
                start_day = has_before[0]['day']
            else:
                start_year = now.year
                start_month = now.month
                start_day = 1
            
            has_next = calendar_info[nex.month][-1]
            if has_next:
                end_year = nex.year
                end_month = nex.month
                end_day = has_next[-1]['day']
            else:
                end_year = now.year
                end_month = now.month
                end_day = has_next[-1]['day']

            print('start', start_year, start_month, start_day)
            print('end', end_yaer, end_month, end_day)
            # posts = request.user.posts.filter(date__lte==f'')
            

            return Response(calendar_info, status=status.HTTP_200_OK)
        message = {
            'deatail': '년도 또는 월 정보가 누락되었습니다.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
