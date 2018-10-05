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