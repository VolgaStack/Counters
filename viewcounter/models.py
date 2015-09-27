from django.db import models
from django.utils import timezone
    
class Counter(models.Model):    
    counter = models.IntegerField(unique=True)
    code_status = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    site = models.URLField()
    type = models.CharField(max_length=50)
    
    def __str__(self):
        return '{0}'.format(self.name)
    
class Summary(models.Model):
    counter = models.ForeignKey(Counter)
    name = models.CharField(max_length=200, default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    visits = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
	
class MetricaSettings(models.Model):
	name = models.CharField(max_length=100, default='')
	client_id = models.CharField(max_length=100)
	client_pass = models.CharField(max_length=100, default='')
	token = models.CharField(max_length=100, blank=True)
	
	def __str__(self):
	    return '{0}'.format(self.name)