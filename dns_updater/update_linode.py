import json
import os
import requests

def create_linode_request(target: str):
    baseUrl: str  = 'https://api.linode.com/v4/domains'
    auth: str = f"Bearer {os.environ['TOKEN']}"
    domainId: str = os.environ['DOMAIN_ID']
    recordId: str = os.environ['RECORD_ID']

    print("Creating linode request...")

    url: str = f'{baseUrl}/{domainId}/records/{recordId}'
    contentType: str = 'application/json'
    headers = {'Authorization': auth, 'Content-Type': contentType}
    body = {'target': target}

    response = requests.put(url, data=json.dumps(body), headers=headers)
    
    return response
