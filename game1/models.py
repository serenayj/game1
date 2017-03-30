from django.db import models
from django.contrib.auth import login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User

# Create your models here.
# users and items are for single 

class HID(models.Model):
	hitid = models.CharField(max_length=128, unique=True)
	turkid = models.CharField(max_length=128, unique=True,primary_key=True)
	assid = models.CharField(max_length=128, unique=False)
	provisional = models.BooleanField(default = True)  
	username = models.CharField(max_length=128, unique=True,default="someone")
	def _unicode_(self):
		return self.name

"""
class UserProfile(models.Model):
	username = models.CharField(max_length=140,default="someone")
	userid = models.ForeignKey(HID)
	#userid = models.ForeignKey(HID, db_column='turkid')
	channelid = models.CharField(max_length=128, unique=True)
	pairid = models.CharField(max_length=128, unique=True)
	
	def __unicode__(self):
		return self.user.username
"""


class Pairs(models.Model):
	# auto-increment
	pairid = models.AutoField(primary_key=True)
	user1id = models.ForeignKey(HID,related_name = 'userid1')
	user2id = models.ForeignKey(HID,related_name = 'userid2')
	channelid = models.CharField(max_length=128, unique=True,default = "something")
	url1 = models.URLField(default = "test1")
	url2 = models.URLField(default = "test2")

	
	def __unicode__(self):
		return self.pairid
"""		
class Pairs(models.Model):
	# auto-increment
	pairid = models.AutoField(primary_key=True)
	user1id = models.ForeignKey(UserProfile,related_name = 'userid1')
	user2id = models.ForeignKey(UserProfile,related_name = 'userid2')
	channelid = models.CharField(max_length=128, unique=True)
	url = models.URLField()
	
	def __unicode__(self):
		return self.pairid


class Channels(models.Model):
    channelid = models.CharField(max_length=128, primary_key=True, unique=True)
    pairid = models.ForeignKey(Pairs)
    url = models.URLField()

class Pairs(models.Model):
	pairid = models.CharField(max_length=128, unique=True)
	user1id = models.ForeignKey(UserProfile,related_name = 'userid')
	user2id = models.ForeignKey(UserProfile,related_name = 'userid')
	channelid = models.CharField(max_length=128, unique=True)
	url = models.URLField()
	
	def __unicode__(self):
		return self.pairid
"""
"""
class User(models.Model):
	userid = models.CharField(max_length=30,primary_key=True)
	username = models.CharField(max_length=30)
	#password = models.CharField(max_length=30)
	#email = models.CharField(max_length=50)

	#it is for printing out with normal words
	def _unicode_(self):
		return self.name
"""

