from django.shortcuts import render_to_response, HttpResponse
from blog.models import BlogRecord
from django.http import Http404


# Create your views here.

MAX_VIEWS_REC = 10


def page(request, page_id = 0):
	try:
		page_id = int (page_id)
		blog_records = BlogRecord.objects.all ()[ MAX_VIEWS_REC*page_id : MAX_VIEWS_REC*(1 + page_id) + 1]
		len_blog_records = len (blog_records)
		if len_blog_records <= 0:
			raise Http404
	except BlogRecord.DoesNotExist:
		raise Http404
	if page_id > 0:
		preiv_page = page_id - 1
	else:
		preiv_page = 0
	if len_blog_records == MAX_VIEWS_REC + 1:
		next_page = page_id + 1
	else:
		next_page = 0
	
	return render_to_response (u'blog/blog.html', { 'blog_records' : blog_records[0:MAX_VIEWS_REC], u'page_id': page_id, u'preiv_page': preiv_page, u'next_page':next_page})


def detalis(request, blog_id):
	try:
		blog_id = int (blog_id)
		blog_record = BlogRecord.objects.get(id=blog_id)
	except BlogRecord.DoesNotExist:
		raise Http404
	return render_to_response (u'blog/detalis.html', {'blog_record' : blog_record})
