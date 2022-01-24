from rest_framework import serializers
from .models import Quest, School, Category, Done
from django.contrib.auth.models import User



# class Quest(object):
#     def __init__(self, dictionary):
#         self.dict = dictionary

class QuestSerializer(serializers.ModelSerializer) :
    def getUsername(self, quest):
      return quest.author.username
    author_name = serializers.SerializerMethodField("getUsername")
    class Meta :
      model = Quest # quest 모델 사용
      fields = '__all__'
      # fields = ('todo_quest', 'user', 'author', 'school')
      
      def get_username(self, obj):
        return obj.owner.username


class DoneSerializer(serializers.ModelSerializer) :               
    class Meta :
      model = Done
      fields = '__all__'

class HottestSerializer(serializers.ModelSerializer) :
    # dictionary = serializers.DictField(
    #   child = serializers.CharField())

    class Meta :
      model = Quest # quest 모델 사용
      fields = '__all__'

    
