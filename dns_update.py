import os
import requests
from dotenv import load_dotenv, main
from requests.models import Response

from update_cloudflare import create_cloudflare_request
from update_linode import create_linode_request

if __name__ == "__main__":
    result = None
    load_dotenv()

    target = requests.get('https://api.ipify.org/').text

    print(target)

    if target == '':
        target = requests.get('https://ipv4.icanhazip.com/').text
        print(target)

    provider: str = os.environ["PROVIDER"].lower()

    if provider == "linode":
        result = create_linode_request(target)
    elif provider == "cloudflare":
        result = create_cloudflare_request(target)
    else:
        raise Exception(f'Invalid provider: {provider}')

    print(result.content)
