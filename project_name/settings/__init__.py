# -*- coding: utf-8 -*-

import os

try:
    import local
    from development import *
except:
    from production import *

