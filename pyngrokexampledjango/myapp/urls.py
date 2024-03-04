__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

from django.urls import re_path
from django.contrib import admin

from pyngrokexampledjango.myapp.views import healthcheck

urlpatterns = [
    re_path('admin/', admin.site.urls, name='admin'),

    re_path('healthcheck/', healthcheck, name='healthcheck'),
]
