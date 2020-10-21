from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:post_id>/', views.diary.as_view(), name='diary'),
    path('', views.CreateDiary.as_view(), name='create_diary'), 

]