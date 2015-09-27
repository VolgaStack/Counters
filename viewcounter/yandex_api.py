import requests


__all__ = ["OAuth", "GetCounters", "GetReport",

]

AUTH = 'https://oauth.yandex.ru/authorize'
AUTH_TOKEN = 'https://oauth.yandex.ru/token'
COUNTERS = 'management/v1/counters?oauth_token=%s'
REPORT = 'stat/v1/data?ids=%s&oauth_token=%s'
API = 'https://api-metrika.yandex.ru/'

class Metrica:
    """Metrica class provides methods to work with Yandex Metrica API   
    """

    def OAuth(self):
        """ (Metrica) -> NoneType
        Authorize method. Sets self._token
        """
        params = {'client_id':self._client_id}
        if self._code:
            params['grant_type'] = 'authorization_code'
            params['client_secret'] = self._client_pass
            response = requests.post(AUTH_TOKEN, params=params)
            result = response.json()
            self._token = result['access_token']       
        else:       
            params['response_type'] = 'code'
            params['display'] = 'popup'
            req = requests.Request('GET', url=AUTH, params=params)
            req = req.prepare()
            return req.url
             
    def GetCounters(self):
        """ (Metrica) -> dict of dict
        Gets all availiable counters from Yandex Metrica API
        """     
        req = requests.get(API + COUNTERS % (self._token))
        return self.read_json_from_req(req)
                            
    def GetReport(self, counter_list, args={}):
        """ (Metrica, list, dic) -> dict of dict
        Gets Report from Yandex Metrica API
        """
        add_counter = ''
        add_string = ''
        
        for item in counter_list:
            add_counter += str(item) + ','
        add_counter=add_counter[0:-1]   
            
        
        for key in args:
            add_string += '&' + key + '=' + args[key]
        
        req = requests.get(API + REPORT % (add_counter,self._token) + add_string)
        return self.read_json_from_req(req)
        
        
    def read_json_from_req(self, req):
        """(Metrica, HTTPrequest) -> dict of dict
        Reads JSON repsonse from Yandex Metrica API, 
        merges it into one dict if there is key 'next' in JSON['links']
        """
        response = {}
        if req.status_code == 200:
            response = req.json()
            #reading next page if there is one
            if 'links' in response: 
                while 'next' in response['links']:
                    req = requests.get(response['links']['next'])
                    if req.status_code == 200:
                        old_response = response
                        response = dict_add(old_response, req.json())     
        return response
        
    
    def dict_add(self, dict1, dict2): # aka merged() or updated()
        if 'counters' in dict1:
            for counter_list in dict2['counters']:
                dict1['counters'].append(counter_list)
            dict1['rows'] += dict2['rows']
        elif 'ids' in dict1['query']:
            dict2_len = len(dict2['query']['ids'])
            for i in range(dict2_len):
                dict1['query']['ids'].append(dict2['query']['ids'][i])
                dict1['totals'].append(dict2['totals'][i])
            dict1['total_rows'] += dict2['total_rows']          
        return dict1
    
    def __init__(self, client_id, client_pass='', token='', code=''):
        self._client_id = client_id
        self._client_pass = client_pass
        self._token = token
        self._code = code
