"""InternshipsTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django import views
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.base import TemplateView
from decorator_include import decorator_include
from utils import decorators

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/",
        include("InternshipsApp.urls"),
    ),
    path(
        "studentapplications/",
        decorator_include(
            [login_required],
            "applicant.urls",
        ),
    ),
    path(
        "carrier/",
        decorator_include(
            [login_required],
            "carrier.urls",
        ),
    ),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
