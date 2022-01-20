
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .models import Quest, School, Category
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import QuestSerializer
from latte import serializers


def index(request):
    return render(request, 'latte/index.html')

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
    
    