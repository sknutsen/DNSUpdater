import os
import requests
from dotenv import load_dotenv

from .update_cloudflare import create_cloudflare_request
from .update_domeneshop import create_domeneshop_request
from .update_linode import create_linode_request

def update():
    result = None
    load_dotenv()

    target = requests.get('https://api.ipify.org/').text

    print(target)

    if target == '':
        target = requests.get('https://ipv4.icanhazip.com/').text
        print(target)

    provider: str = os.environ["PROVIDER"].lower()

    providers = {
        "linode": create_linode_request,
        "cloudflare": create_cloudflare_request,
        "domeneshop": create_domeneshop_request,
    }

    result = providers[provider](target)

    if result != None:
        print(result.content)
