
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from .models import Done, Quest, School, Category
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import QuestSerializer, DoneSerializer
from latte import serializers
from django.views.decorators.csrf import csrf_exempt


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

            
        