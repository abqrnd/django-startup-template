# -*- coding: utf-8 -*-
"""Common settings and globals."""
from os.path import abspath, basename, dirname, join, normpath
from sys import path

DJANGO_ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT')

# Django defaults
from base import *
from admins import *
from apps import *
from email import *
from fixtures import *
from media import *
from middleware import *
from static import *
from templates import *

# Libs
from compress import *
from thumbs import *
