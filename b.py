import requests
import urllib2, urllib
import json


auth_token='kbkcmbkcmbkcbc9ic9vixc9vixc9v'
hed = {'Authorization': 'Bearer ' + auth_token}
data = {'app' : 'aaaaa'}

url = 'https://api.xy.com'
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())