import api_ya
import json
from django.views.generic import View
from django.http import JsonResponse
from .models import CountersInfo


class ViewsCounterGet(View):
	model = CountersInfo
	
	def get(self, request):
		result = CountersInfo.objects.values('counter_id', 'counter_name', 'counter_views' ).order_by('-timestamp')[:1]
		#need to make sure that result is dict
		if type(result) is not dict:
			#converting queryset object into dict
			
		return JsonResponse(result)
		
class ViewsCounterMain(View)
	def get(self, request):		 
		return HttpResponse('What do u need?')
		
	def post(self, request):
		#getting info from YA metrica
		
		#saving to db
		
		return result
