import json
import os
import requests

def create_cloudflare_request(target: str):
    baseUrl: str  = 'https://api.cloudflare.com/client/v4'
    authEmail: str = os.environ["AUTH_EMAIL"]
    authKey: str = os.environ["AUTH_KEY"]
    authMode: str = os.environ["AUTH_MODE"]
    zoneId: str = os.environ["ZONE_ID"]
    recordName: str = os.environ["RECORD_NAME"]
    recordType: str = os.environ["RECORD_TYPE"]

    authHeader: str = ''
    recordId: str = ''

    print("Creating cloudflare request...")

    if authMode.lower() == "global":
        authHeader = "X-Auth-Key"
    elif authMode.lower() == "token":
        authHeader = "Authorization"
        authKey = f'bearer {authKey}'
    else:
        raise Exception(f'authMode \'{authMode}\' is not valid')

    print(f'authHeader: {authHeader}')

    urlGET: str = f'{baseUrl}/zones/{zoneId}/dns_records?type={recordType}&name={recordName}'
    contentType: str = 'application/json'
    headers = {'X-Auth-Email': authEmail, authHeader: authKey, 'Content-Type': contentType}
    body = {'type': recordType, 'name': recordName, 'content': target, 'proxied': True}

    print(f'urlGET: {urlGET}')

    print(f'headers: {headers}')

    recordIdResponse = requests.get(urlGET, headers=headers)

    record = json.loads(recordIdResponse.content)["result"]
    
    recordId = record[0]["id"]

    urlPUT: str = f'{baseUrl}/zones/{zoneId}/dns_records/{recordId}'

    print(urlPUT)

    response = requests.put(urlPUT, data=json.dumps(body), headers=headers)

    return response
