# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # make sure you delete this entry
    url(r'^/?$', 'apps.hello_world.views.hello'),
)

# Make /media work on local machine
if hasattr(settings, 'DJANGO_ENVIRONMENT') \
    and settings.DJANGO_ENVIRONMENT == 'development':
        urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$',
                'django.views.static.serve',
                {
                    'document_root': settings.MEDIA_ROOT
                }
            ),
        )
