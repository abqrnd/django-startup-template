from . import AWS_STORAGE_BUCKET_NAME

STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
