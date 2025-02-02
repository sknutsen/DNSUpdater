import json
import os
import requests
from domeneshop import Client

def create_domeneshop_request(target: str):
    client = Client(os.getenv("TOKEN"), os.getenv("SECRET"))
    
    domainId: int = 0
    recordId: int = 0

    record: dict = None

    if os.getenv("DOMAIN_ID") != "" and os.getenv("DOMAIN_ID") != None:
        domainId = int(os.getenv("DOMAIN_ID"))
    else:
        domain: dict = get_domeneshop_domain(client, os.getenv("DOMAIN_NAME"))

        if domain != None:
            domainId = domain["id"]
        else:
            print("Domain was not found...")
            return None

    if domainId == 0:
        return None

    if os.getenv("RECORD_ID") != "" and os.getenv("RECORD_ID") != None:
        recordId = int(os.getenv("RECORD_ID"))

        if recordId != 0:
            record = client.get_record(domainId, recordId)
    
    else:
        record = get_domeneshop_record(client, domainId, os.getenv("RECORD_NAME"))

        if record != None:
            recordId = record["id"]
        else:
            print("Record was not found...")
            return None

    
    if recordId == 0 or record == None:
        return None
    
    if record["data"] != target:
        record["data"] = target    

        update_domeneshop_record(client, domainId, recordId, record)

    return None

def get_domeneshop_domain(client: Client, domainName: str) -> dict:
    result: dict = None

    print("Getting domeneshop domain {0}...".format(domainName))
    domains: List[dict] = client.get_domains()

    for domain in domains:
        if domain["domain"] == domainName:
            result = domain
            break

    print(result["id"])
    return result

def get_domeneshop_record(client: Client, domainId: int, recordName: str) -> dict:
    result: dict = None

    print("Getting domeneshop record {0}/{1}...".format(domainId, recordName))
    records: List[dict] = client.get_records(domainId)

    for record in records:
        if record["host"] == recordName:
            result = record
            break

    print(result["id"])
    print(result.keys())
    print(result)
    return result

def update_domeneshop_record(client: Client, domainId: int, recordId: int, record: dict):
    newrecord: dict = copy_record(record)  # domainshop record validation does not support "id"
    client.modify_record(domainId, recordId, newrecord)

def copy_record(record: dict) -> dict:
    return {
        "data": record["data"],
        "host": record["host"],
        "ttl" : record["ttl"],
        "type": record["type"],
    }
