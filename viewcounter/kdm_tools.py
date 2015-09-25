import os
from .models import Summary, Counter

class KdmToolSet:
	
    def ReadFile(self, filename):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, filename)
        string_list = []
        with open(file_path, 'r') as f:
            for line in f: 
                string_list.append(line.rstrip('\n').replace(' ', ''))
                    
        for i in range(len(string_list)):
            if string_list[i].find('id:') == 0:
                file_id = string_list[0].lstrip('ID:')
            if string_list[i].find('token:') == 0:
                file_token = string_list[1].lstrip('Token:')

        return (file_id, file_token)
		
	def WriteToDb(self, dictionary):
	counters_dict = dictionary
	counters_list = list(Counter.objects.values_list('counter_id', flat=True)
	counters_dict = self.ParseJsonDict(counters_dict, counters_list)
	for key in counters_dict:
		new_counter = Counter(
			counter_id = key 
			code_status = counters_dict[key]['code_status']
			name = counters_dict[key]['name']
			site = counters_dict[key]['site']
			type = counters_dict[key]['type']
		)	
		new_counter.save()

	def ParseJsonDict(self, dictionary, list):
		dict_len = len(dictionary['counters'])
		for i in range(dict_len):
			counter_id = dictionary['counters'][i]['id']
			if counter_id not in list:
				counters_dict[counter_id] : {
					'name':dictionary['counters'][i]['name'],
					'site':dictionary['counters'][i]['site'], 
					'code_status':dictionary['counters'][i]['code_status'], 
					'type':views:dictionary['counters'][i]['type'],
				}
		return counters_dict
			
		
