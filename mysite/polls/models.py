# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Model fields are what you keep in your database.
#These are visible to only the developer
#(it answers how you want your data organized)

#Serializer fields are what you expose to your clients.
#(it answers how you want your data represented)
#while Serializer fields are used to when exposing the api to the client, visible to client also.

class Question(models.Model):
	question_text= models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	def __str__(self):
		return self.choice_text


