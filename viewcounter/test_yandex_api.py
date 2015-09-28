from django.test import TestCase
from .yandex_api import Metrica
import requests 

AUTH = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' 
COUNTERS = 'management/v1/counters?oauth_token=%s'
REPORT = 'stat/v1/data?ids=%s&oauth_token=%s'
API = 'https://api-metrika.yandex.ru/'

class MetricaMethodTests(TestCase):
        
    def test_get_counters_url_creation(self):
        """ m.OAuth should set self.token to token if authorize was sucsessfull
        """
        token = '7f56b1a9d80648c7b87ae588a905a9be'
        http = 'https://api-metrika.yandex.ru/management/v1/counters?oauth_token=%s'
        req1 = requests.get(http % token)
        req2 = requests.get(API + COUNTERS % (token))
        self.assertEqual(req1.url, req2.url)
        
    def test_get_report_url_creation(self):
        token = '7f56b1a9d80648c7b87ae588a905a9be'
        counter_list= [1,2,3]
        args = {'arg1':'value1', 'arg2':'value2',}
        add_counter = ''
        add_string = ''
        
        for item in counter_list:
            add_counter += str(item) + ','
        add_counter=add_counter[0:-1]
		
        for key in args:
            add_string += '&' + key + '=' + args[key]
        
        req2 = requests.get(API + REPORT % (add_counter,token) + add_string)
        req1 = 'https://api-metrika.yandex.ru/stat/v1/data?ids=1,2,3&oauth_token=7f56b1a9d80648c7b87ae588a905a9be&arg1=value1&arg2=value2'
        self.assertEqual(req1, req2.url)        
    
    def test_links_next_in_JSON(self):
        a = {'content':{'type':'JSON'},'links':{'next':'go_here','prev':'go_there'}}
        req = 'wrong_rec'
        if 'next' in a['links']:
            req = a['links']['next']
 
        self.assertEqual('go_here', req)
    
    def test_dictionary_merge_report_data(self):
        client_id = 'c9aff383ddfc4f7693637c984bfc064a'
        a = {"query":{"ids":[2138128],},"total_rows":1,"totals":[11.0],}
        b = {"query":{"ids":[1234567],},"total_rows":1,"totals":[15.0],}
        c = {"query":{"ids":[2138128,1234567],},"total_rows":2,"totals":[11.0,15.0]}
        
        m = Metrica(client_id)
        c_func = m.dict_add(a,b)
        c_req = c
        self.assertEqual(c_req, c_func)

    def test_dictionary_merge_counters_data(self):
        client_id = 'c9aff383ddfc4f7693637c984bfc064a'
        a = {"rows":1,"counters":[{"id":2215810,}]}
        b = {"rows":1,"counters":[{"id":1234567,}]}
        c = {"rows":2,"counters":[{"id":2215810,},{"id":1234567,},]}
        
        m = Metrica(client_id)
        c_func = m.dict_add(a,b)
        c_req = c
        self.assertEqual(c_req, c_func)
            
