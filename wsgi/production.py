import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      '{{ project_name }}.settings.production')

activate_path = '/home/WF_USERNAME/.virtualenvs/WF_ENVNAME/bin/activate_this.py'
execfile(activate_path, dict(__file__=activate_path))

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
