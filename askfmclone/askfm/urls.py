from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^my/$',
        views.my_profile_view,
        name='my_profile_view'),
    url(r'^(?P<username>([.\-_a-zA-Z0-9]){4,})/$',
        views.user_profile_view,
        name='user_profile_view'),
    url(r'^q/answer/$',
        views.answer_view,
        name='answer_view'),
]
