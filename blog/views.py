from django.shortcuts import render_to_response, HttpResponse
from blog.models import BlogRecord
from django.http import Http404

# Create your views here.

MAX_VIEWS_REC = 10


def page(request, page_id = 1):
	try:
		page_id = int (page_id)
		blog_records = BlogRecord.objects.all ()[ MAX_VIEWS_REC*(page_id - 1): MAX_VIEWS_REC*page_id]
	except BlogRecord.DoesNotExist:
		raise Http404
	return render_to_response (u"blog/blog.html", {'blog_records' : blog_records})


def detalis(request, page_id, blog_id):
	try:
		page_id = int (page_id)
		blog_id = int (blog_id)
		blog_record = BlogRecord.objects.all ()[ MAX_VIEWS_REC*(page_id - 1) + (blog_id - 1) ]
	except BlogRecord.DoesNotExist:
		raise Http404
	return render_to_response (u"blog/detalis.html", {'blog_record' : blog_record})
