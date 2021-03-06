from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=256)
    quest_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    def count_quests(self):
        category_filtered_quest= Quest.objects.filter(category_id = self.id)
        self.quest_count = category_filtered_quest.count()
        self.save()

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class School(models.Model):
    title = models.CharField(max_length=256)
    quest_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    def count_quests(self):
        school_filtered_quest= Quest.objects.filter(school_id = self.id)
        self.quest_count = school_filtered_quest.count()
        self.save()

    def update_date(self): 
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
DEFAULT = 0
class Quest(models.Model): 
    
    todo_quest = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=CASCADE, default=1)
    # author_name = models.CharField(max_length=256, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    done_users = models.ManyToManyField(User, blank=True, related_name='done_user', through='Done') 
    done_count = models.IntegerField(default=0)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_user', through='Like') 
    like_count = models.IntegerField(default=0)
    active = models.BooleanField(default=1)
    # content = models.TextField()
    # like = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    

    def update_date(self): # ????????? ????????? ??? ??????
        self.updated_at = timezone.now()
        self.save()
    
    def count_done_user(self):
        self.done_count = self.done_users.count()
        self.save()
        # return self.done_user.count()
    
    def count_like_user(self):
        self.like_count = self.like_users.count()
        self.save()
        # return self.done_user.count()

    def __str__(self):
        return self.todo_quest
      
class Done(models.Model) :
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    quest = models.ForeignKey(Quest, null=True, on_delete=CASCADE)
    active = models.BooleanField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    
class Like(models.Model) :
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    quest = models.ForeignKey(Quest, null=True, on_delete=CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
   
   
# class Hottest(models.Model) :
#     quest = models.ForeignKey(Quest, null=True, on_delete=CASCADE)
#     created_at = models.DateTimeField(default=timezone.now)
     