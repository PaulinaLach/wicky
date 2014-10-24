from django.conf.urls import patterns, url
from .views import PhotographIndex

urlpatterns = patterns('',
    url(r'^photographs/$', PhotographIndex.as_view(), name='picture_index'),
)