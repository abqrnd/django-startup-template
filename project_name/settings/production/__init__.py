# -*- coding: utf-8 -*-
"""Production settings."""
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# Django defaults
from .common import *
from base import *

# Libs
from caches import *
from debug import *
