#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings = os.environ.get("DJANGO_SETTINGS_MODULE")

    if not DJANGO_SETTINGS_MODULE:
        print 'No settings found'


    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
