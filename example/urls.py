#-*- encoding:UTF-8 -*-


from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('',
    url(r'^download/', include('download.urls')),
)
