from django.shortcuts import render
# import requests 
from requests import get
import json

# Create your views here.
def index(request):
    # ip = requests.get('https://geo.ipify.org?formate=json')
    # ip_data = json.loads(ip.text)
    ip = get('https://api.ipify.org').text
    res = get('http://ip-api.com/json/'+ip)
    location_data = res.text
    location_data_one = json.loads(location_data)
    return render(request, 'index.html', {'data':location_data_one})