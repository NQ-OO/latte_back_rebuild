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
from latte.views import QuestViewSet, QuestDoneAPIView, QuestLikeAPIView, WebHottestAPIView, AppHottestAPIView, SchoolViewSet, CategoryViewSet, HotSchoolAPIView, MyQuestsAPIView, MyDoneQuestsAPIView
# from accounts.views import ProfileViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
#  import views
from .models import Quest, School, Category
# api documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v1',
        description="latte description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="latte.forserver@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('quests',QuestViewSet)
router.register('schools',SchoolViewSet)
router.register('category',CategoryViewSet)
# router.register('profiles',ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup/', include('rest_auth.registration.urls')),
    # path('latte/', include('latte.urls')),
    # path('', latte.views.index, name='index'),
    path('', include(router.urls)),
    path('<int:id>/done/', QuestDoneAPIView.as_view(), name= "done_quest"),
    path('<int:id>/like/', QuestLikeAPIView.as_view(), name= "like_quest"),
    path('web-hottest/', WebHottestAPIView.as_view(), name= "hottest_quest"),
    path('app-hottest/', AppHottestAPIView.as_view(), name= "hottest_quest"),
    path('hot-school-list/', HotSchoolAPIView.as_view(), name= "hottest_quest"),
    path('my-quests/', MyQuestsAPIView.as_view(), name= "my-quests-list"),
    path('my-quests/<int:id>/', MyQuestsAPIView.as_view(), name= "my-quests-update"),
    path('my-done-quests/', MyDoneQuestsAPIView.as_view(), name= "my-done-quests"),
    path('api/token/', obtain_auth_token, name='obtain_token'),
    #api documentaions
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #accoutns
    path('accounts/', include('accounts.urls')), 

]

