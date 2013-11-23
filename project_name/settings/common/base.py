from os.path import abspath, basename, dirname, join, normpath
from sys import path

# Project name:
PROJECT_NAME = '{{ project_name }}'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Name', 'email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__ + '/../')))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Europe/London'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-gb'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = '9q@6x%7hacshwtlkqm!13=unfv2*hv9+h3a-+m#3y42z0$0yzm'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#append-slash
APPEND_SLASH = True
