from django.conf.urls import patterns, url
from .views import PhotographIndex, PhotographCreate, PhotographShow, PhotographUpdate, PhotographDelete

urlpatterns = patterns('',
    url(r'^photographs/$', PhotographIndex.as_view(), name='photograph_index'),
    url(r'^photographs/create/$', PhotographCreate.as_view(), name='photograph_create'),
    url(r'^photographs/(?P<pk>\d+)/$', PhotographShow.as_view(), name='photograph_show'),
    url(r'^photographs/(?P<pk>\d+)/update$', PhotographUpdate.as_view(), name='photograph_update'),
    url(r'^photographs/(?P<pk>\d+)/delete', PhotographDelete.as_view(), name='photograph_delete'),
)