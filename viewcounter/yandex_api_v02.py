import requests
import json

AUTH = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' 
COUNTERS = 'https://api-metrika.yandex.ru/management/v1/counters?oauth_token='
SUMMARY = 'https://api-metrika.yandex.ru/stat/traffic/summary.json?id=%s&oauth_token=%s'
API = 'https://api-metrika.yandex.ru/'

class Metrica:
    """Metrica class provides methods to work with Yandex Metrica API   
    """

    def OAuth(self):
        """ (Metrica) -> NoneType
        Authorize method. Sets self.token
        """
        req = requests.get(AUTH+self.client_id)
        if req.status_code == 200:
            url = req.url   
            token = url[url.find('#access_token='):url.find('&token_type=')]
            token = token[token.find('#access_token='):token.find('&expires_in=')]
            self.token = token[token.find('=')+1:]
                
    def GetCounters(self):
        """ (Metrica) -> dict of dict
        Gets all availiable counters from Yandex Metrica API
        """     
        req = requests.get(COUNTERS+self.token)
        return self.read_json_from_req(req)
                            
    def GetCounterSummary(self, counter_id):
        """ (Metrica, int) -> dict of dict
        Gets Counter 'populatiry' from Yandex Metrica API
        """
        req = requests.get(SUMMARY % (counter_id,self.token))
        return self.read_json_from_req(req)
        
    def read_json_from_req(self, req):
        """(Metrica, HTTPrequest) -> dict of dict
        
        """
        response = {}
        if req.status_code == 200:
            response = req.json()
            #reading next page if there is one
            while 'next' in response['links']:
                req = requests.get(response['links']['next'])
                if req.status_code == 200:
                    old_response = response
                    response = dict_add_keep_last(old_response, req.json())     
        return response
        
    
    def dict_add_keep_last(self, dict1, dict2): # aka merged() or updated()
        merged_dict = dict1.copy()
        merged_dict.update(dict2)
        return merged_dict
        
    def __init__(self, client_id, token=''):
        self.client_id = client_id
        self.token = token
        self.counters_dict={}
        self.counters_list = ()
        
        if self.token == '':
            self.OAuth();
