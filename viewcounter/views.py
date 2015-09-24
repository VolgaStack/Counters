import json
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponse
from .models import CountersInfo
from .api_ya import Metrica
from .kdm_tools import KdmToolSet 
from django.utils import timezone


class ViewsCounterGet(View):
	
	def get(self, request):
		query_set = list(CountersInfo.objects.values_list(
			'counter_id', 'name', 'views'
		).order_by('-timestamp')[:1])
		
		json_data = json.dumps(query_set)
		return HttpResponse(json_data, content_type='application/json')
				
class ViewsCounterMain(View):
		
	def get(self, request):
		#getting id and other things from db	
		q = KdmToolSet()
		client_id, client_token = q.readfile('settings.txt')
		
		#getting info from YA metrica	
		m = Metrica(client_id, client_token)
		if m.token == '':
			m.OAuth()
			if m.token =='':
				return HttpResponse(status=500)

		m.GetCounters()
		#checking if Metrica.counters_dict is not empty
		if bool(m.counters_dict):
			counters = m.counters_dict
			for key in counters:
				info = CountersInfo()
				info.counter_id = key 
				info.name = counters[key]['name']
				info.site = counters[key]['site']
				info.status = counters[key]['code_status']
				info.views = counters[key]['views']
				info.period = timezone.now()
				info.save()
			return HttpResponse(status=200)
		return HttpResponse(status=500)
