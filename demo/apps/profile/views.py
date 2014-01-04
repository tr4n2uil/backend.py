import json, hashlib, random
from django.conf import settings
from django.db import models
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from util.views import render, find
from apps.profile.models import UserData


def profile( request, username, stream = None, **kwargs ):
	tmpl = 'user/profile.html'
	data = {}

	data[ 'stream' ] = 'user/' + ( stream if stream else 'dashboard' ) + '.html'

	if not request.user.is_authenticated():
		return HttpResponseRedirect( '/?next=' + request.path )

	data[ 'viewer' ] = o = UserData.find( request.user.username )
	if not o:
		return HttpResponseRedirect( '/verify/' )

	data[ 'person' ] = u = UserData.find( username )
	if not u:
		return render( request, data = data, tmpl = tmpl, error = 'User Not Found' )

	data[ 'admin' ] = admin = u.id == request.user.id

	if request.POST:
		action = request.POST.get( 'action' )

		if not admin:
			return render( request, data = data, tmpl = tmpl, error = 'Not Authorized' )

		if action == 'basic':
			tmpl = 'user/basic.html'

			name = request.POST.get( 'name', u.user.first_name )

			u.user.first_name = name
			u.user.save()

			data[ 'person' ] = u = UserData.find( username )
			return render( request, data = data, tmpl = tmpl, type = 'json' )

	return render( request, data = data, tmpl = tmpl )


def verify( request, key = None, **kwargs ):
	tmpl = 'user/verify.html'
	data = {}

	p = request.user.get_profile()

	if key:
		if p.user.check_password( key ):
			p.is_verified = 1
			p.is_done = 1
			p.save()

			salt = hashlib.sha1( str( random.random() ) ).hexdigest()[ :5 ]
			password = hashlib.sha1( salt + request.user.username ).hexdigest()[ :8 ]
			request.user.set_password( password )
			request.user.save()

			data[ 'success' ] = True
		else:
			return render( request, data = data, tmpl = tmpl, error = 'Invalid Verification Link' )

	elif request.POST:
		p.corp_email = request.POST.get( 'corp_email' )
		if not p.corp_email:
			return render( request, data = data, tmpl = tmpl, error = 'Invalid Email' )

		p.save()

		salt = hashlib.sha1( str( random.random() ) ).hexdigest()[ :5 ]
		password = hashlib.sha1( salt + request.user.username ).hexdigest()[ :8 ]
		request.user.set_password( password )
		request.user.save()

		email = EmailMessage( 
			settings.PERSON_RESET_SUBJECT,
			settings.PERSON_RESET_BODY % { 'name': request.user.first_name, 'username' : request.user.username, 'password' : password }, 
			to = [ p.corp_email ],
			from_email = settings.DEFAULT_FROM_EMAIL
		)
		email.send()

		data[ 'reset' ] = True

	return render( request, data = data, tmpl = tmpl )

