# -*- coding: utf-8 -*-
from django.conf import settings

from common import *

if hasattr(settings, 'DJANGO_ENVIRONMENT'):
    if settings.DJANGO_ENVIRONMENT == 'development':
        from development import *
    elif settings.DJANGO_ENVIRONMENT == 'production':
        from production import *
