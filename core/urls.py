from django.conf import settings
from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	# social urls
	url( r'', include( 'social.apps.django_app.urls', namespace = 'social' ) ),

	# core
	url( r'^$', 'django.contrib.auth.views.login', { 'template_name': 'home.jade' }, name='home' ),
	url( r'^drive/(.*)$', 'django.views.static.serve', kwargs = { 'document_root': settings.MEDIA_ROOT } ),
	
	# fs
	url( r'^embed/$', 'fs.views.embed_image', name="embed_image" ),
	#url( r'^preview/(?P<id>\d+)/(?P<name>[\w\W]+)?$', 'fs.views.preview', name='preview' ),
	
	# auth urls
	url( r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/' }, name='logout' ),

	# avatar urls
	url( r'^avatar/', include( 'avatar.urls' ) ),

	# base user urls
	url( r'^verify/(?P<key>[\w]+)?/?$', 'apps.profile.views.verify', name='verify' ),
	url( r'^user/(?P<username>[\w\-]+)/(?P<stream>(dashboard))?/?$', 'apps.profile.views.profile', name= 'profile' ),

	# apps urls
	url( r'^view/(?P<username>[\w\-]+)/(?P<id>[\d]+)/$', 'apps.demo.home', name='home' ),
	
    # tmpl urls
    url( r'^(?P<tmpl>[\w\-\/]+)/$', 'util.views.render', { 'html' : True }, name='tmpl' ),
    
)

