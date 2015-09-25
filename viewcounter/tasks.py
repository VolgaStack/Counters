from celery import task
import requests

@task()
def PopulateDB():
	req = requests.get('http://127.0.0.1:801/views/ASKYA')
    return req.status_code