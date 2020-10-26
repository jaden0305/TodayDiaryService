from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
<<<<<<< Updated upstream
    
=======
    path('', include('rest_auth.urls')),
    path('check/email/', views.check_email),
>>>>>>> Stashed changes
]