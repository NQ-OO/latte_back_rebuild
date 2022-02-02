
from django.urls import path
from django.urls.conf import include
from accounts import views
from rest_framework import routers
from accounts.views import ProfileAPIView


app_name = 'profile'

urlpatterns = [    
  path('profile/<int:id>/', ProfileAPIView.as_view(), name= "user_profile_update"),
]