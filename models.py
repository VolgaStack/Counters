from django.db import models

class CountersInfo(models.Model):
	date = models.DateTimeField()
	counter_id = models.IntegerField()
	counter_name = models.CharField(max_length=200)
	counter_site = models.URLField()
	counter_views = models.IntegerField()
	
