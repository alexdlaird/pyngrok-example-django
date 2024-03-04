"""
WSGI config for pyngrokexampledjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyngrokexampledjango.settings')

application = get_wsgi_application()
