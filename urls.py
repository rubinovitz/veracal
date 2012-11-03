from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'PennApps2012.views.home', name='home'),
    url(r'^', include('apps.calendar.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('PennApps2012.api.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^logged-in/', include('apps.calendar.urls')),
    )
    
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)
