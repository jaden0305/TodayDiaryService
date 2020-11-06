from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('fonts/', views.get_fonts),
    path('papers/', views.get_patterns),
    path('colors/', views.get_colors),

    path('<int:post_id>/', views.diary.as_view(), name='diary'),
    path('', views.CreateDiary.as_view(), name='create_diary'), 
    
    path('maketest/', views.make_test),
]