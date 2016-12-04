from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<question_id>\d+)/$',
        views.details,
        name='question_details'
    )
]
