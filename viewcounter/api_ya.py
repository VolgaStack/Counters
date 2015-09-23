import requests

AUTH = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' 
COUNTERS = 'https://api-metrika.yandex.ru/management/v1/counters?oauth_token='
SUMMARY = 'https://api-metrika.yandex.ru/stat/traffic/summary.json?id=%s&oauth_token=%s'
API = 'https://api-metrika.yandex.ru/'

class Metrica:
	"""
		
	"""
	
	def __init__(self, client_id):
		self.client_id = client_id
		self.token = ''
		self.counters_dict={}
	
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
		""" (Metrica) -> NoneType
		Get and Put all availiable counters from Yandex Metrica API
		into self.counters_dict
		"""			
		req = requests.get(COUNTERS+self.token)
		if req.status_code == 200:
			response = req.json()
			self.ReadCountersInfo(response)

			while 'next' in response:
				req = requests.get(response['next'])
				if req.status_code == 200:
					response = req.json()
					self.ReadCountersInfo(response)
				
			
	def ReadCountersInfo(self, dictionary):
		""" (Metrica, dict) -> NoneType
		Reads id, name, site, status and views from dictionary into self.counters_dict
		"""
		dict_len = len(dictionary['counters'])
		for i in range(dict_len):
			counter_id = dictionary['counter'][i]['id']
			name = dictionary['counter'][i]['name']
			site = dictionary['counter'][i]['site']
			status = dictionary['counter'][i]['code_status']
			views = self.GetCounterStats(counter_id)
			self.counters_dict[id] = {'name':name,'site':site, 'code_status':status, 'views':views }
				
				
	def GetCounterStats(self, counter_id):
		""" (Metrica, int) -> NoneType
		Creates GET HTTP request to Yandex Metrica API
		returns total views in period on counter_id
		"""
		views = 0
		req = requests.get(SUMMARY % (counter_id,self.token))
		if req.status_code == 200:
			response = req.json()
			views = responce['totals']['visits']
			
		return views
	
	
