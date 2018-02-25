from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/(?P<pk>[0-9]+)$',
        views.get_delete_update_experiment,
        name='get_delete_update_experiment'
    ),
    url(
        r'^api/$',
        views.get_post_experiments,
        name='get_post_experiments'
    )
]
