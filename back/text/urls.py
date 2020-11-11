from django.urls import path
from . import views

app_name = 'text'

urlpatterns = [
    path('', views.statistics, name='statistics'),
    path('analysis/', views.analyze),
    path('select/', views.select, name='select'),
    path('weekly/', views.weekly, name='weekly'),
    path('monthly/', views.monthly),
    path('total/', views.total),

    path('redistest/', views.redistest),
]