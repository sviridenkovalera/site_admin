from django.db import models
from blog.models import BlogRecord

# Create your models here.
class Comment(models.Model):
	id_blog = models.ForeignKey(BlogRecord)
	date_create = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=128)
	comment = models.CharField(max_length=256)
