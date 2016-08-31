from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        views.homepage,
        name='homepage'),
    url(r'^my/$',
        views.my_profile,
        name='my_profile'),
    url(r'^(?P<username>([.\-_a-zA-Z0-9]){4,})/$',
        views.user_profile,
        name='user_profile'),
    url(r'^q/answer/$',
        views.answer,
        name='answer'),
]
