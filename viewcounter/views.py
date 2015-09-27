import json
from datetime import datetime
from django.views.generic import View
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import redirect
from .models import Counter,Summary, MetricaSettings
from .yandex_api import Metrica
from .kdm_tools import KdmToolSet


class ViewsCounterGet(View):
    
    def get(self, request):
        today = datetime.date(timezone.now())
        query_set = list(Summary.objects.values_list('name', 'visits',
        ).filter(start_date=today,end_date=today).order_by('-timestamp')[:1])
        
        json_data = json.dumps(query_set)
        return HttpResponse(json_data, content_type='application/json')
                
class ViewsCounterMain(View):
        
    def get(self, request):
        
        settings = MetricaSettings.objects.get(pk=1)
            
        m = Metrica(settings.client_id, 
                    client_pass=settings.client_pass,
                    token = settings.token,         
        )
            
        if 'code' in request.GET:
            m._code = request.GET['code']
            m.OAuth()
            
            settings.token = m._token
            settings.save()
			
            counters_dict = m.GetCounters()
            #if Counters_dict is not empty -> select all counters -> compare -> add only new counters
            if bool(counters_dict):
                t.WriteToDbCounters(counters_dict)
            
            #Requesting all counters in db => we could have added new ones
            counters_list = list(Counter.objects.values_list('counter', flat=True))
            #setting report parametrs to period = day, metrics = visits
            args = {'date1':'today', 'date2':'today', 'metrics':'ym:s:visits', }
            report = m.GetReport(counters_list,args)
            if bool(report):
                counters_list = list(Summary.objects.values_list('counter', flat=True).filter(
                    start_date=timezone.now(),end_date=timezone.now()
                ))
                t.WriteToDbSummary(report, counters_list)
            
            return HttpResponse(status=200)
    
        else:
            req = m.OAuth()
            return redirect(req)
            
        
            
        
