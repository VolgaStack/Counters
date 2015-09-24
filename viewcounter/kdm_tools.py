import os

class KdmToolSet:
	
    def readfile(self, filename):
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
