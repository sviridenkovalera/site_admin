from django.shortcuts import render_to_response
from comment.models import Comment

# Create your views here.

def comment (request, comment_id):
	comment_id = int (comment_id)
	comments = Comment.objects.filter (id_blog_id=comment_id)
	return render_to_response ("comment/comment.html", { "comments" : comments } )
