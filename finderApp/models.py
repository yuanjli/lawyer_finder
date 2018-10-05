from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.
class Todo(models.Model):
	text = models.CharField(max_length=512)
	is_complete = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

	def __str__(self):
		return self.text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.short_description = 'Published in last 24 hours?'
    was_published_recently.boolean = True

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=False)  

    my_answer = models.ForeignKey(Choice, on_delete=models.CASCADE, blank=False, null=False) 
    my_points = models.IntegerField(default=-1)
    their_points = models.IntegerField(default=-1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.my_answer.text[:10]

class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    specialties = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    stories = models.CharField(max_length=100)
    photo_url = models.TextField()
    numbers = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
    # check if it's the last 24 hours

    was_published_recently.short_description = 'Published in last 24 hours?'
    was_published_recently.boolean = True

class Specialties(models.Model):
    name = models.CharField(max_length=100)
    specialties = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    stories = models.CharField(max_length=100)
    photo_url = models.TextField()
    numbers = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    











