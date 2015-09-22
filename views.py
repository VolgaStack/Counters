import api_ya
from django.shortcuts import render
from django.views.generic import View
from .models import CountersInfo


class ViewsCounterGet(View):
	model = CountersInfo
	
	def get(self, request):
		#logic
		
		return response
		
class ViewsCounterMain(View)
	def get(self, request):
		#logic
		return HttpResponse('result')
		
	def post(self, request):
		#logic
		return HttpResponse('result')
