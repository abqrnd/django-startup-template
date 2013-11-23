########## APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers:
    'south',

    # Static file management:
    'compressor',

    # Thumbnails
    'sorl.thumbnail',
)

LOCAL_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION
