from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_admin.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
