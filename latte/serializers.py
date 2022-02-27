
from rest_framework import serializers
from .models import Quest, School, Category, Done, Like
from django.contrib.auth.models import User



# class Quest(object):
#     def __init__(self, dictionary):
#         self.dict = dictionary

class QuestSerializer(serializers.ModelSerializer) :
    def getUsername(self, quest):
      try : 
        username = quest.author.username
        return username
      except :
        return
    def getSchoolname(self, quest):
      try : 
        school = quest.school.title
        return school
      except :
        return
    author_name = serializers.SerializerMethodField("getUsername")
    school_name = serializers.SerializerMethodField("getSchoolname")
    class Meta :
      model = Quest # quest 모델 사용
      fields = '__all__'
      # fields = ('todo_quest', 'user', 'author', 'school')
      
      # def get_username(self, obj):
      #   return obj.owner.username


class DoneSerializer(serializers.ModelSerializer) :               
    class Meta :
      model = Done
      fields = '__all__'

class LikeSerializer(serializers.ModelSerializer) :               
    class Meta :
      model = Like
      fields = '__all__'

class HottestSerializer(serializers.ModelSerializer) :
    # dictionary = serializers.DictField(
    #   child = serializers.CharField())

    class Meta :
      model = Quest # quest 모델 사용
      fields = '__all__'

    
class SchoolSerializer(serializers.ModelSerializer) :               
    class Meta :
      model = School
      fields = '__all__'
      
class CategorySerializer(serializers.ModelSerializer) :               
    class Meta :
      model = Category
      fields = '__all__'
      
      
class HotSchoolSerializer(serializers.ModelSerializer) :               
    class Meta :
      model = School
      fields = ('title', 'quest_count')
      
class MyQuestsSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Quest
    fields = ('todo_quest', 'school', 'category', 'active', 'done_count')
    
class MyDoneQuestsSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Quest
    fields = '__all__'
    
class MyQuestsSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Quest
    fields = '__all__'