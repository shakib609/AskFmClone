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
    # Login/Logout
    url(r'^login/$',
        'askfmclone.user.views.login_view',
        name='login_view'),
    url(r'^logout/$',
        'askfmclone.user.views.logout_view',
        name='logout_view'),
    url(r'^register/$',
        'askfmclone.user.views.registration_view',
        name='registration_view'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
]
