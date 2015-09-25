from django.db import models
from django.utils import timezone

class Summary(models.Model):
	counter_id = models.ForeignKey(Counter, to_field='counter_id')
	name = models.ForeignKey(Counter, to_field='name')
	start_date = models.DateField()
	end_date = models.DateField()
	denial = models.DecimalField(decimal_places=2)
	visits = models.IntegerField()
	visitors = models.IntegerField()
	page_views = models.IntegerField()
	depth = models.DecimalField(decimal_places=4)
	visit_time = models.IntegerField()	
	new_visitors = models.IntegerField()
	timestamp = models.DateTimeField(default=timezone.now)
	
class Counter(models.Model):	
	counter_id = models.IntegerField(primary_key=True)
	code_status = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	site = models.URLField()
	type = models.models.CharField(max_length=50)