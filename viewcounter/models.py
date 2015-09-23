from django.db import models
from django.utils import timezone

class CountersInfo(models.Model):
	period = models.DatetimeField()
	counter_id = models.IntegerField()
	counter_name = models.CharField(max_length=200)
	counter_site = models.URLField()
	counter_status = models.CharField(max_length=200)
	counter_views = models.IntegerField()
	timestamp = models.DatetimeField(default=timezone.now())
	
