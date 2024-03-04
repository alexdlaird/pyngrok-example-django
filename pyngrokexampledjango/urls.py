"""
URL configuration for pyngrokexampledjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

__copyright__ = "Copyright (c) 2023-2024 Alex Laird"
__license__ = "MIT"

from django.urls import re_path, include

import pyngrokexampledjango.myapp.urls

urlpatterns = [
    re_path('^', include(pyngrokexampledjango.myapp.urls)),
]
