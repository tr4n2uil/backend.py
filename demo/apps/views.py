from django.conf import settings
from django.db import models
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from util.views import render, find


def home( request, username, id, **kwargs ):
	tmpl = 'home.jade'
	data = { 'username': username, 'id': id }

	if not request.user.is_authenticated():
		return HttpResponseRedirect( '/login/facebook/?next=' + request.path )

	return render( request, data = data, tmpl = tmpl )	

