from django.db import models
from django.utils import timezone
	
class Counter(models.Model):	
	counter_id = models.IntegerField(primary_key=True)
	code_status = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	site = models.URLField()
	type = models.CharField(max_length=50)
	
class Summary(models.Model):
	counter_id = models.ForeignKey(Counter, to_field='counter_id')
	name = models.CharField(max_length=200, default='')
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	visits = models.IntegerField()
	timestamp = models.DateTimeField(default=timezone.now)