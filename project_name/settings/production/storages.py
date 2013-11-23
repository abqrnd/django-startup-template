# -*- coding: utf-8 -*-
from . import INSTALLED_APPS

########## STORAGE CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'storages',
)

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
STATICFILES_STORAGE = STORAGES_STORAGE ='storages.backends.s3boto.S3BotoStorage'

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' %
        (AWS_EXPIREY, AWS_EXPIREY)
}

STORAGES_STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
########## END STORAGE CONFIGURATION

STATIC_URL = STORAGES_STATIC_URL
DEFAULT_FILE_STORAGE = STATICFILES_STORAGE
