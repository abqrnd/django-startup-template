#!/usr/bin/env python
import os
import sys
import getopt

if __name__ == "__main__":
    settings = os.environ.get("DJANGO_SETTINGS_MODULE")

    if not settings:
        for arg in sys.argv:
            settings, args = getopt.getopt([arg], '', 'settings=')
            if settings:
                break
        if not settings:
            print 'No settings found. You need to specify the settings file by passing  --settings={{ project_name }}.settings.development or set a global "DJANGO_SETTINGS_MODULE" variable with the name of your settings file, eg. {{ project_name }}.settings.development'

    if settings:
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
