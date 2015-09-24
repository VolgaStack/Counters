from django.db import models
from django.utils import timezone

class CountersInfo(models.Model):
	period = models.DateTimeField()
	counter_id = models.IntegerField()
	name = models.CharField(max_length=200)
	site = models.URLField()
	status = models.CharField(max_length=200)
	views = models.IntegerField()
	timestamp = models.DateTimeField(default=timezone.now)