#!/usr/bin/env python
import os
import sys
import getopt

if __name__ == "__main__":
    settings = os.environ.get("DJANGO_SETTINGS_MODULE")
    args = sys.argv

    if not settings:
        for i in range(0, len(args)):
            param = args[i].split('=')
            if len(param) == 2 and param[0] in ['--settings', '-s']:
                settings = param[1]
                if settings and len(settings.split('.')) == 1:
                    settings = '{{ project_name }}.settings.%s' % settings

                sys.argv[i] = '--settings=%s' % settings
                break;

    if settings:
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
    else:
        print 'No settings found. You need to specify the settings file by passing  --settings=development or set a global "DJANGO_SETTINGS_MODULE" variable with the name of your settings file, eg. {{ project_name }}.settings.development'

