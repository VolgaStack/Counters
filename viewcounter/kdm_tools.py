import os
from .models import Summary, Counter
from django.utils import timezone

__all__ = ["ReadFile", "WriteToDbCounters", "WriteToDbSummary",

]

class KdmToolSet:
    
    def ReadFile(self, filename):
        READ = ['id:', 'password:', 'ID:', 'PASSWORD:', 'Пароль:',
			    'Токен:', 'Token:', 'token:', 'токен:'
		]
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, filename)
        string_list = []
        with open(file_path, 'r') as f:
            for line in f:
                if any(w in line for word in READ):
                    string_list.append(line.rstrip('\n').replace(' ', '').lstrip(word))

        return (file_id, file_pass)
        
    def WriteToDbCounters(self, dictionary):
        counters_list = list(Counter.objects.values_list('counter', flat=True))
        d = self.parse_json_dict(dictionary, counters_list)
        for key in d:
            new_counter = Counter(
                counter = key, 
                code_status = d[key]['code_status'],
                name = d[key]['name'],
                site = d[key]['site'],
                type = d[key]['type'],
            )   
            new_counter.save()

    def parse_json_dict(self, dictionary, list):
        #not sure about this.. counters ATM gor static data, 
        #maybe just delete all rows and then insert all counters that API returned to us.
        #my POV: INSERT = constant time. DELETE = N?
        #       search for x in not sorted massive => N
        #       search for list of x in not sorted massive => len(list) * N
        #       len(list) * N + costant > N + constant on big enough N, and on small N we dont care..
        counters_dict = {}
        dict_len = len(dictionary['counters'])
        for i in range(dict_len):
            counter_id = dictionary['counters'][i]['id']
            if counter_id not in list:
                counters_dict[counter_id] = { 
                        'name':dictionary['counters'][i]['name'],
                        'site':dictionary['counters'][i]['site'], 
                        'code_status':dictionary['counters'][i]['code_status'], 
                        'type':dictionary['counters'][i]['type'],
                }
        return counters_dict
        
    def WriteToDbSummary(self, report, counters_list):
        """ (dict, list ) -> NoneType 
        Writes or updates
        """
        i = 0   
        for item in report['query']['ids']:         
            if item in counters_list:
                Summary.objects.filter(counter=item).update(
                    visits=report['totals'][i], 
                    timestamp=timezone.now(),
                )
                i += 1
            else:
                counter = Counter.objects.get(counter=item)
                info = Summary(
                    counter = counter,
                    name = counter.name,
                    start_date = report['query']['date1'],
                    end_date = report['query']['date2'],
                    visits = report['totals'][i],
                )
                info.save()
                i += 1        
