
from django.urls import path
from django.urls.conf import include
from accounts import views
from rest_framework import routers
from accounts.views import ProfileAPIView, CreateRandomIdAPIView
from django.contrib.auth.models import User


app_name = 'accounts'

urlpatterns = [    
  path('profile/<int:id>/', ProfileAPIView.as_view(), name= "user_profile_update"),
  path('create-random-id/', CreateRandomIdAPIView.as_view(), name =  "random_id_create")
]