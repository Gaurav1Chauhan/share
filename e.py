import urllib


auth_token='6225e5fc-22fc-429d-9fd4-b36484bbcc7a'
hed = {'Authorization': 'Bearer ' + auth_token}
data = {'app' : 'aaaaa'}

urllib2("https://18.219.209.143:8446/sepm/api/v1/command-queue/15EC94A1BDB94BF6AA94B152304D821A")
response = requests.get(urllib2, json=data, headers=hed)
print(response)
print(response.json())