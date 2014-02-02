import math, re, random
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from slugify import slugify
from backend.util.views import unique, unique_repeat, find


# userdata class
class UserData( models.Model ):
	id = models.AutoField( primary_key = True )
	user = models.OneToOneField( User )
	user_type = models.IntegerField( default = 0 )

	corp_email = models.CharField( max_length = 64 )
	is_verified = models.IntegerField( default = 0 )
	is_done = models.IntegerField( default = 0 )


	@staticmethod
	def find( username ):
		return find( UserData, user__username = username, is_done = 1 )
	
	@staticmethod
	def find_or_create( user, *kwargs ):
		try:
			return UserData.objects.get( user = user )
		except UserData.DoesNotExist:
			return UserData.objects.create( user = user )


# register signal handler
def create_person( sender, instance, created, **kwargs ):
	if created:
		ud = UserData.find_or_create( user = instance )

post_save.connect( create_person, sender = User )

