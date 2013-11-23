# -*- coding: utf-8 -*-
from . import INSTALLED_APPS

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' %
        (AWS_EXPIREY, AWS_EXPIREY)
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

INSTALLED_APPS += (
    'storages',
)
