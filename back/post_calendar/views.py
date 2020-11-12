import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from .common import date_to_dict
from .serializers import CalendarQuerySerializer
from post.models import Post
from post.serializers import ReadPostSerializer
from text.serializers import DailyReportSerializer
from text.models import DailyReport



User = get_user_model()

class CalendarView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def get_date_range(self, calendar_info=None, now=None):
        if now is None:
            now = datetime.datetime.now()
        if calendar_info is None:
            calendar_info = date_to_dict(now.year, now.month)
        pre = (now - relativedelta(months=1))
        nex = (now + relativedelta(months=1))
        
        has_before = calendar_info[pre.month]
        if  has_before:
            start_year = pre.year
            start_month = pre.month
            start_day = has_before[0]['day']
        else:
            start_year = now.year
            start_month = now.month
            start_day = 1
        
        has_next = calendar_info[nex.month]
        if has_next:
            end_year = nex.year
            end_month = nex.month
            end_day = has_next[-1]['day']
        else:
            end_year = now.year
            end_month = now.month
            end_day = has_next[-1]['day']

        start = datetime.date(start_year, start_month, start_day)
        end = datetime.date(end_year, end_month, end_day)

        return start, end

    @swagger_auto_schema(query_serializer=CalendarQuerySerializer)
    def get(self, request):

        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))
        
        print(year, month)
        calendar_info = date_to_dict(year, month)

        if year and month:

            now = datetime.date(year, month, 1)
            start, end = self.get_date_range(calendar_info=calendar_info, now=now)
            
            posts = User.objects.filter(pk=request.user.pk)\
                    .prefetch_related('posts')[0]\
                    .posts.filter(created__lte=end, created__gte=start)\
                    .values()
            print(posts)
            for post in posts:
                report = DailyReportSerializer(instance=get_object_or_404(DailyReport, pk=post['report_id'])).data
                created = post['created']
                calendar_info[created.month][created.day-1]['post'] = {
                    'emotion': report['emotion'],
                    'user_emotion': post['user_emotion_id'],
                    'id': post['id']
                }
            
            return Response(calendar_info, status=status.HTTP_200_OK)
            
        message = {
            'deatail': '년도 또는 월 정보가 누락되었습니다.'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
