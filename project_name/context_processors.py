from django.conf import settings

def custom_settings(request):
    return {
        'settings': {
            'PROJECT_NAME': settings.PROJECT_NAME,
            'SITE_NAME': settings.SITE_NAME,
            'LANGUAGE_CODE': settings.LANGUAGE_CODE,
        }
    }
