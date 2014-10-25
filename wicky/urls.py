from django.conf.urls import patterns, include, url
from wicky.settings import IMAGE_ROOT
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^user/', include('user_account.urls')),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  IMAGE_ROOT}, name="images"),
)
