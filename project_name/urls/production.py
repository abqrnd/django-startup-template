# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from . import urlpatterns

# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns += patterns('',
    # memcached
    url(r'^cache/', include('django_memcached.urls')),
)
