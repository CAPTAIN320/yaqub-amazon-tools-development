import urllib.request
import urllib.parse
import shutil
import tempfile
import requests
import json

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass



""" 
r = requests.get('https://www.amazon.com/shops/HAPPYSASHIMI')
print(r)
print(r.url) # https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be
 """
""" 
a = requests.get('https://www.amazon.com/gp/shops/HAPPYSASHIMI?ie=UTF8&%2AVersion%2A=1&%2Aentries%2A=0')
print(a)
print(a.url)
 """
""" 
b = requests.get('https://www.amazon.com/shops/HAPPYSASHIMI?&marketplaceID=ATVPDKIKX0DER')
print(b)
print(b.url)
 """

# set up the request parameters
params = {
  'api_key': 'BDA72F7899D94417B5ABB1B78E5E59C9',
  'type': 'seller_profile',
  'amazon_domain': 'amazon.com',
  'output': 'json',
  'seller_id': 'A02211013Q5HP3OMSZC7W'
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# print the JSON response from Rainforest API
print(json.dumps(api_result.json()))