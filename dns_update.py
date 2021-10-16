import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

baseUrl: str  = 'https://api.linode.com/v4/domains'
domainId: str = os.environ['DOMAIN_ID']
recordId: str = os.environ['RECORD_ID']

url: str = f'{baseUrl}/{domainId}/records/{recordId}'

auth: str = f"Bearer {os.environ['TOKEN']}"
contentType: str = 'application/json'

headers = {'Authorization': auth, 'Content-Type': contentType}

target = requests.get('https://api.ipify.org/').text

print(target)

if target == '':
    target = requests.get('https://ipv4.icanhazip.com/').text
    print(target)

body = {'target': target}

response = requests.put(url, data=json.dumps(body), headers=headers)

print(response.content)
