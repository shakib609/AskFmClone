"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # Admin
    url(
        r'^admin/',
        include(admin.site.urls)
    ),

    # Auth
    url(
        r'^auth/',
        include('apps.auth.urls', namespace='auth')
    ),

    # question app
    url(
        r'^question/',
        include('apps.question.urls', namespace='question')
    ),


    # django_pydenticon urls
    url(
        r'^avatar/',
        include('django_pydenticon.urls', namespace='avatar')
    ),

    # askfm app
    url(
        r'^',
        include('apps.askfm.urls', namespace='askfm')
    ),
]
