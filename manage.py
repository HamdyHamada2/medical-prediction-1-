#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import logging


def main():
    """Run administrative tasks."""
    os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "Baymax.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError (
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line (sys.argv)


if __name__ == '__main__':
    logging.basicConfig (
        filename='logs/debug.log',  # اسم ملف السجلات
        level=logging.WARNING,  # مستوى السجلات لتسجيل التحذيرات فقط
        format='%(asctime)s - %(levelname)s - %(message)s'  # تنسيق السجل
    )

    logging.warning ('This is a warning message.')  # مثال على رسالة تحذير
    logging.error ('This is an error message.')  # مثال على رسالة خطأ

if __name__ == "__main__":
    main ()
