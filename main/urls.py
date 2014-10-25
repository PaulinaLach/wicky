from django.conf.urls import patterns, url
from .views import CategoryIndex, CategoryCreate, CategoryShow, CategoryUpdate, CategoryDelete, AlbumIndex, AlbumCreate, AlbumShow, AlbumUpdate, AlbumDelete, PhotographIndex, PhotographCreate, PhotographShow, PhotographUpdate, PhotographDelete

urlpatterns = patterns('',
    url(r'^categories/$', CategoryIndex.as_view(), name='category_index'),
    url(r'^categories/create/$', CategoryCreate.as_view(), name='category_create'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryShow.as_view(), name='category_show'),
    url(r'^categories/(?P<pk>\d+)/update$', CategoryUpdate.as_view(), name='category_update'),
    url(r'^categories/(?P<pk>\d+)/delete', CategoryDelete.as_view(), name='category_delete'),


    url(r'^albums/$', AlbumIndex.as_view(), name='album_index'),
    url(r'^albums/create/$', AlbumCreate.as_view(), name='album_create'),
    url(r'^albums/(?P<pk>\d+)/$', AlbumShow.as_view(), name='album_show'),
    url(r'^albums/(?P<pk>\d+)/update$', AlbumUpdate.as_view(), name='album_update'),
    url(r'^albums/(?P<pk>\d+)/delete', AlbumDelete.as_view(), name='album_delete'),


    url(r'^photographs/$', PhotographIndex.as_view(), name='photograph_index'),
    url(r'^photographs/create/$', PhotographCreate.as_view(), name='photograph_create'),
    url(r'^photographs/(?P<pk>\d+)/$', PhotographShow.as_view(), name='photograph_show'),
    url(r'^photographs/(?P<pk>\d+)/update$', PhotographUpdate.as_view(), name='photograph_update'),
    url(r'^photographs/(?P<pk>\d+)/delete', PhotographDelete.as_view(), name='photograph_delete'),


)

