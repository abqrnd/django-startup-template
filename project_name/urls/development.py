# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url

from . import urlpatterns

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT
        }
    ),
)
