#!/usr/bin/env python
import os
import sys

def main():
    # هذا السطر هو الأهم، يربط المشروع بمجلد الإعدادات الخاص بك
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courses_mohamed.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()