from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/$', 'user_account.views.user_show', name='user_show'),
)