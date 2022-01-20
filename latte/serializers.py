from rest_framework import serializers
from .models import Quest, School, Category, Done



# class Quest(object):
#     def __init__(self, dictionary):
#         self.dict = dictionary


class QuestSerializer(serializers.ModelSerializer) :
    # dictionary = serializers.DictField(
    #   child = serializers.CharField())

    class Meta :
      model = Quest # quest 모델 사용
      fields = '__all__'

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

    
