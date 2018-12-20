import requests
import ssl
import fpdf

auth_token='cd8e399d-8cdc-4a73-9c07-309f0099c58a'
hed = {'Authorization': 'Bearer ' + auth_token}


url = 'https://18.219.209.143:8446/sepm/api/v1/command-queue/15EC94A1BDB94BF6AA94B152304D821A'
response = requests.get(url,data="", headers=hed , verify=False)
print(response)
print(response.json())