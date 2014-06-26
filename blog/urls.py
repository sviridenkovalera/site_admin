from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns ('',
		url(r'^$', views.index, name='index'),
		url(r'^(?P<page_id>\d+)/$', views.page, name='page'),
		url(r'^details/(?P<blog_id>\d+)/$', views.detalis, name='detalis'),
)
