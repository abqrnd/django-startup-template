########## APP CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = (
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

    # Database migration helpers:
    'south',

    # Static file management:
    'compressor',

    # Thumbnails
    'sorl.thumbnail',
)
########## END APP CONFIGURATION
