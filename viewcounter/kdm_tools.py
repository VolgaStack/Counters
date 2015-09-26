import os
from .models import Summary, Counter
from django.utils import timezone

__all__ = ["ReadFile", "WriteToDbCounters", "WriteToDbSummary",

]

class KdmToolSet:
    
    def ReadFile(self, filename):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, filename)
        string_list = []
        with open(file_path, 'r') as f:
            for line in f:
                if line.find('id:') != -1 or line.find('token:') != -1:
                    string_list.append(line.rstrip('\n').replace(' ', ''))
                    
        for i in range(len(string_list)):
            if string_list[i].find('id:') == 0:
                file_id = string_list[0].lstrip('id:')
            if string_list[i].find('token:') == 0:
                file_token = string_list[1].lstrip('token:')

        return (file_id, file_token)
        
    def WriteToDbCounters(self, dictionary):
        d = {}
        counters_list = list(Counter.objects.values_list('counter_id', flat=True))
        d = self.parse_json_dict(dictionary, counters_list)
        for key in dic:
            new_counter = Counter(
                counter_id = key, 
                code_status = dic[key]['code_status'],
                name = dic[key]['name'],
                site = dic[key]['site'],
                type = dic[key]['type'],
            )   
            new_counter.save()

    def parse_json_dict(self, dictionary, list):
        #not sure about this.. counters ATM gor static data, 
        #maybe just delete all rows and then insert all counters that API returned to us.
        #my POV: INSERT = constant time. DELETE = N?
        #       search for x in not sorted massive => N
        #       search for list of x in not sorted massive => len(list) * N
        #       len(list) * N + costant > N + constant on big enough N, and on small N we dont care..
        dict_len = len(dictionary['counters'])
        for i in range(dict_len):
            counter_id = dictionary['counters'][i]['id']
            if counter_id not in list:
                counters_dict = {
                    [counter_id] : {
                        'name':dictionary['counters'][i]['name'],
                        'site':dictionary['counters'][i]['site'], 
                        'code_status':dictionary['counters'][i]['code_status'], 
                        'type':dictionary['counters'][i]['type'],
                    }
                }
        return counters_dict
        
    def WriteToDbSummary(self, report, counters_list):
        """ (dict, list ) -> NoneType 
        Writes or updates
        """
        i = 0   
        for item in report['query']['ids']:         
            if item in counters_list:
                Summary.objects.update(
                    visits=report['totals'][i], 
                    timestamp=timezone.now(),
                ).filter(counter_id=item)
                i += 1
            else:
                name = Counter.objects.values_list('counter_id', 
                        flat=True).filter(counter_id=item)
                name = name[0]
                info = Summary(
                    counter_id=item,
                    name = name,
                    start_date = report['query']['date1'],
                    end_date = report['query']['date2'],
                    visits = report['totals'][i],
                )
                info.save()
                i += 1        
