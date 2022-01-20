"""latte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import latte.views
from latte.views import QuestViewSet
# from accounts.views import ProfileViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
#  import views
from .models import Quest, School, Category


router = routers.DefaultRouter()
router.register('quests',QuestViewSet)
# router.register('profiles',ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/signup/', include('rest_auth.registration.urls')),
    # path('latte/', include('latte.urls')),
    # path('', latte.views.index, name='index'),
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token, name='obtain-token'),
]

