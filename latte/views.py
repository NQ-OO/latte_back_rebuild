
from builtins import print
from cgitb import reset
import imp
from unicodedata import category
from venv import create
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .models import Done, Quest, School, Category
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import QuestSerializer, DoneSerializer, HottestSerializer, SchoolSerializer, CategorySerializer, HotSchoolSerializer, MyQuestsSerializer, MyDoneQuestsSerializer, MyQuestsSerializer
from latte import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Quest, School, Category, Like
from rest_framework.generics import GenericAPIView
from accounts.models import Profile

class QuestViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    # Response({"uielements": result})

    def list(self, request) :
        get_quest_num_index = 10
        queryset = Quest.objects.all().order_by('-id')#[:get_quest_num_index]
        serializer = QuestSerializer(queryset, many=True) 
        # print('queryset.count:', queryset.count)
        result = { 'Quests' : serializer.data}
        return Response(result)
    
    # 웹에서 익명으로 만드는 사람들을 위한 
    def create(self, request) :
        serializer = QuestSerializer(data=request.data)
        print(request.data)
        user = request.user
        profile = Profile.objects.get(user_id = user.id) 
        if serializer.is_valid() :
            # print("serializer :", serializer.data)
            serializer.save()
            quest = Quest.objects.get(id = serializer.data['id'])
            # print("quest : ", quest.)
            school = School.objects.get(id = quest.school_id)
            category = Category.objects.get(id = quest.category_id)
            school.count_quests()
            school.save()
            category.count_quests()
            category.save()
            profile.my_quests.add(quest)
            # print(profile.quests.)
            profile.my_quests_count = len(profile.my_quests.all())
            profile.save()
            return Response(serializer.data, status=201)
            
        else :
            return Response(serializer.errors, status=400)
            
        
            
# @csrf_exempt
class QuestDoneAPIView(APIView) :
    def post(self, request, id) :
        user = request.user
        profile = Profile.objects.get(user_id = user.id)
        quest = Quest.objects.get(id = id)
        done_list = quest.done_set.filter(user_id = user.id)
        if len(done_list) > 0: 
            done_list.delete()
            quest.count_done_user()
            quest.save()
            profile.done_quests.remove(quest)
            print(len(profile.done_quests.all()))
            profile.done_quests_count = len(profile.done_quests.all())
            profile.save()
            result = {'quest status changed'}
            return Response(result)
        else:
            new_done_quest_user = Done()
            new_done_quest_user.user = user
            new_done_quest_user.quest = quest
            new_done_quest_user.save()
            quest.count_done_user()
            quest.save()
            profile.done_quests.add(quest)
            profile.done_quests_count = len(profile.done_quests.all())
            profile.save()
            result = {'quest status changed'}
            return Response(result)
        
class QuestLikeAPIView(APIView) :
    def post(self, request, id) :
        user = request.user
        profile = Profile.objects.get(user_id = user.id)
        quest = Quest.objects.get(id = id)
        like_list = quest.like_set.filter(user_id = user.id)
        
        if len(like_list) > 0: 
            like_list.delete()
            quest.count_like_user()
            quest.save()
            result = {'quest status changed'}
            return Response(result)
        else:
            new_like_quest_user = Like()
            new_like_quest_user.user = user
            new_like_quest_user.quest = quest
            new_like_quest_user.save()
            quest.count_like_user()
            quest.save()
            # profile.my_quests.remove(quest)
            # profile.save()
            result = {'quest status changed'}
            return Response(result)


class WebHottestAPIView(APIView):
    queryset = Quest.objects.all().order_by('-like_count')
    serializer_class = HottestSerializer
    # Response({"uielements": result})

    def get(self, request) :
        get_quest_num_index = 10
        queryset = Quest.objects.all().order_by('-like_count')#[:get_quest_num_index]
        serializer = QuestSerializer(queryset, many=True) 
        # print('queryset.count:', queryset.count)
        result = { 'HottestQuests' : serializer.data}
        return Response(result)    

class AppHottestAPIView(APIView):
    queryset = Quest.objects.all().order_by('-done_count')
    serializer_class = HottestSerializer
    # Response({"uielements": result})

    def get(self, request) :
        get_quest_num_index = 10
        queryset = Quest.objects.all().order_by('-done_count')#[:get_quest_num_index]
        serializer = QuestSerializer(queryset, many=True) 
        # print('queryset.count:', queryset.count)
        result = { 'HottestQuests' : serializer.data}
        return Response(result)    
    
    
class SchoolViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
    def create(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        else :
            return Response(serializer.errors, status=400)


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=201)
        else :
            return Response(serializer.errors, status=400)


class HotSchoolAPIView(APIView):
    queryset = School.objects.all()
    serializer_class = HotSchoolSerializer
    # Response({"uielements": result})
    def get(self, request) :
        queryset = School.objects.all().order_by('-quest_count')
        serializer = HotSchoolSerializer(queryset, many=True)
        return Response(serializer.data, status=201)
    

#나의 퀘스트 일 경우에만 RUD기능 - 추후에 보안기능 넣을 계획
class MyQuestsAPIView(APIView):
    queryset = Quest.objects.all()
    serializer_class = MyQuestsSerializer
    # Response({"uielements": result})
    def get(self, request) :
        author_id = request.user.id
        queryset = Quest.objects.filter(author = author_id)
        queryset = queryset.order_by('-id')
        serializer = MyQuestsSerializer(queryset, many=True)
        return Response(serializer.data, status=201)
    
    def put(self, request, id) :
        if id is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else :
            quest = Quest.objects.get(id = id)
            quest_update_serializer = MyQuestsSerializer(quest, data = request.data)
            if quest_update_serializer.is_valid():
                quest_update_serializer.save()
                return Response(quest_update_serializer.data, status=status.HTTP_200_OK)
            else :
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        

class MyDoneQuestsAPIView(APIView):
    queryset = Quest.objects.all()
    serializer_class = MyDoneQuestsSerializer
    def get(self, request) :
        author_id = request.user.id
        done_querysets = Done.objects.filter(user = author_id)
        done_querysets_id_list = list(map(lambda x: x.quest_id , done_querysets ))
        quest_querysets = Quest.objects.filter(id__in = done_querysets_id_list)
        queryset = quest_querysets.order_by('-id')
        print(queryset)
        serializer = MyDoneQuestsSerializer(queryset, many=True)
        return Response(serializer.data, status=201)
    