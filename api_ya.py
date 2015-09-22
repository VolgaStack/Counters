import requests

AUTH = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' 
METRIC = 'https://api-metrika.yandex.ru/management/v1/counters?oauth_token='
VIEWS = 'https://api-metrika.yandex.ru/stat/v1/data?'

class Metrica(client_id):
	counters_list=[]
	
	def __init__(self, client_id):
		self.client_id = client_id
		#self.client_pass = client_pass
		self.token = ""
		self.counters_dic={}
	
	def auth(self):
		req = requests.get(AUTH+self.client_id)
		if req.status_code == 200:
			url = req.url	
			token = url[url.find('#access_token='):url.find('&token_type=')]
			token = token[token.find('#access_token='):token.find('&expires_in=')]
			self.token = token[token.find('=')+1:]
			
	
	def get_counters(self, arg):
		req = requests.get(METRIC+self.token)
		if req.status_code == 200:
			response = req.json()
			json_len = range(len(response['counters']))
			for i in json_len:
				id = responce['counter'][i]['id']
				name = responce['counter'][i]['name']
				site = responce['counter'][i]['site']
				counters_dic[id] = {'name':name,'site':site, 'views':0 }
				
				
	def get_counter_views(self):
	
	def write_to_db(self):	
	
	