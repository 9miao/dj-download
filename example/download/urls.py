#-*- encoding:UTF-8 -*-


from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('download.views',
	url(r'^(?P<release>.*)/tarball/$', 'tarball', name='download-tarball'),
)
