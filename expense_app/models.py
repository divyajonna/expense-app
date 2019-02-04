from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Expense(models.Model):
	client = models.ForeignKey(Client,null=True,on_delete=models.CASCADE)
	title = models.CharField(max_length=100,null=True)
	currency = models.CharField(max_length=100,null=True,blank=True)
	amount = models.CharField(max_length=100,null=True,blank=True)
	timestampOfExpense = models.DateTimeField(default=datetime.now,null=True)
	description = models.TextField(max_length=300,null=True,blank=True)

	def __unicode__(self):
		return self.title