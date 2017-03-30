from django.db import models
from django.contrib.auth import login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User

# Create your models here.
# users and items are for single 

class HID(models.Model):
	hitid = models.CharField(max_length=128, unique=True)
	turkid = models.CharField(max_length=128, unique=True, primary_key=True)
	assid = models.CharField(max_length=128, unique=True)
	provisional = models.BooleanField(default = True)  
	username = models.CharField(max_length=128, unique=True, default="someone")
	
	def _unicode_(self):
		return self.name

class Pairs(models.Model):
	# auto-increment
	pairid = models.AutoField(primary_key=True)
	user1id = models.ForeignKey(HID)
	user2id = models.ForeignKey(HID)
	
	def __unicode__(self):
		return self.pairid

class Channels(models.Model):
    channelid = models.CharField(max_length=128, primary_key=True, unique=True)
    pairid = models.ForeignKey(Pairs)
    url = models.URLField()
    



class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title