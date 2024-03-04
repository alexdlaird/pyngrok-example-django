"""
ASGI config for pyngrokexampledjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyngrokexampledjango.settings')

application = get_asgi_application()
