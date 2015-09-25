import json
from django.views.generic import View
from django.http import HttpResponse
from .models import Summary, Counter
from .yandex_api import Metrica
from .kdm_tools import KdmToolSet 
from django.utils import timezone
from datetime import date


class ViewsCounterGet(View):
	
	def get(self, request):
		query_set = list(CountersInfo.objects.values_list(
			'name', 'visits'
		).order_by('-timestamp')[:1])
		
		json_data = json.dumps(query_set)
		return HttpResponse(json_data, content_type='application/json')
				
class ViewsCounterMain(View):
		
	def get(self, request):
		#getting id and other things from db	
		t = KdmToolSet()
		client_id, client_token = t.ReadFile('settings.txt')
		
		m = Metrica(client_id, client_token)
		#on creation it tries to auth so if token is empty something went wrong
		if m.token =='':
			return HttpResponse(status=500)

		counters_dict = m.GetCounters()
		#checking if Counters_dict is not empty,
		#if not make a db call to check for counters in it -> add only new counters
		if bool(counters_dict):
			t.WriteToDb(counters_dict)
		else:
			return HttpResponse(status=500)
		
		#now we got counters in db we can get some data from API!
		counters_list = list(Counter.objects.values_list('counter_id', flat=True)
		
