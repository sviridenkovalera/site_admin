from django.db import models

# Create your models here.
class BlogRecord(models.Model):
	title = models.CharField(max_length=256)
	content = models.CharField(max_length=2048)
	date_create = models.DateTimeField('date published')

