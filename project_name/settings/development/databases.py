from os.path import normpath, join

from . import DJANGO_ROOT
from . import DATABASES

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
}
