from django.conf.urls import patterns, url
from comment import views

urlpatterns = patterns ('',
		#url(r'^$', views.index, name='index'),
		url(r'^(?P<comment_id>\d+)/$', views.comment, name='comment'), 
		url(r'^(?P<comment_id>\d+)/add/$', views.add_comment, name='add_comment'), 
)
