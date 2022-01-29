
from cgitb import reset
from unicodedata import category
from venv import create
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .models import Done, Quest, School, Category
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import QuestSerializer, DoneSerializer, HottestSerializer, SchoolSerializer, CategorySerializer, HotSchoolSerializer
from latte import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Quest, School, Category
from rest_framework.generics import GenericAPIView




class QuestViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    # Response({"uielements": result})

    def list(self, request) :
        get_quest_num_index = 10
        queryset = Quest.objects.all().order_by('-id')[:get_quest_num_index]
        serializer = QuestSerializer(queryset, many=True) 
        # print('queryset.count:', queryset.count)
        result = { 'Quests' : serializer.data}
        return Response(result)
    
    def create(self, request) :
        serializer = QuestSerializer(data=request.data)
        school = School.objects.get(id = request.data['school'])
        category = Category.objects.get(id = request.data['category'])
        if serializer.is_valid() :
            serializer.save()
            school.count_quests()
            school.save()
            category.count_quests()
            category.save()
            return Response(serializer.data, status=201)
            
        else :
            return Response(serializer.errors, status=400)
            
        
            
# @csrf_exempt
class QuestDoneAPIView(APIView) :
    def post(self, request, id) :
        user = request.user
        quest = Quest.objects.get(id = id)
        done_list = quest.done_set.filter(user_id = user.id)
        if len(done_list) > 0: 
            done_list.delete()
            quest.count_done_user()
            quest.save()
            result = {'quest status changed'}
            return Response(result)
        else:
            new_done_quest_user = Done()
            new_done_quest_user.user = user
            new_done_quest_user.quest = quest
            new_done_quest_user.save()
            quest.count_done_user()
            quest.save()
            result = {'quest status changed'}
            return Response(result)


class HottestAPIView(APIView):
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
    
    