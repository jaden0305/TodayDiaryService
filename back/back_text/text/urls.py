from django.urls import path
from . import views

app_name = 'text'

urlpatterns = [
    path('', views.statistics, name='statistics'),
    path('emotion/', views.select_emotion, name='emotion')
]