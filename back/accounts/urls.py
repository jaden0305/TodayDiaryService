from django.urls import path, include

from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from . import views


app_name = 'accounts'

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('signup/', RegisterView.as_view()),
    path('check/email/', views.check_email),
]