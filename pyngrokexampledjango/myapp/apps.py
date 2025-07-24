__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

import os
import sys
from urllib.parse import urlparse

from django.apps import AppConfig
from django.conf import settings


class MyAppConfig(AppConfig):
    name = "pyngrokexampledjango.myapp"
    verbose_name = "My App"

    def ready(self):
        if settings.USE_NGROK:
            # Only import pyngrok and install if we're actually going to use it
            from pyngrok import ngrok

            # Get the dev server port (defaults to 8000 for Django, can be overridden with the
            # last arg when calling `runserver`)
            addrport = urlparse(f"http://{sys.argv[-1]}")
            port = addrport.port if addrport.netloc and addrport.port else "8000"

            # Open a ngrok tunnel to the dev server
            public_url = ngrok.connect(port).public_url
            print(f"ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

            # Update any base URLs or webhooks to use the public ngrok URL
            settings.BASE_URL = public_url
            MyAppConfig.init_webhooks(public_url)

    @staticmethod
    def init_webhooks(base_url):
        # ... Implement updates necessary so webhooks use `public_url` from ngrok
        pass
