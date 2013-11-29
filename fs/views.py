from django.conf import settings
from django.http import HttpResponse, Http404

from fs.models import File
from util.views import render

def embed_image( request, **kwargs ):
	tmpl = 'fs/image.html'
	data = {}

	if not request.user.is_authenticated():
		return Http404
	
	f = request.FILES.get( 'file', None ) if request.FILES else None
	if not f:
		return Http404

	try:
		o = request.user.get_profile()
		if f and o.maxstg <= o.usedstg:
			return render( request, data = data, tmpl = tmpl, error = 'File Storage Space Exceeded', type = 'json' )
	except: pass

	f = File.create( owner = request.user, f = f, prefix = 'embeds/' )

	if not f:
		return render( request, data = data, tmpl = tmpl, error = 'Error Storing File', type = 'json' )

	data[ 'src' ] = f.path[ len( settings.MEDIA_ROOT ): ] + f.alias + '.' + f.ext
	return render( request, data = data, tmpl = tmpl, type = 'json' )

