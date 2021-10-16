# DNSUpdater
Updates a given Linode DNS record

# Dependencies
[python-dotenv](https://pypi.org/project/python-dotenv/)

requests

# How to use
1. Install python-dotenv.

2. Create a .env file in the same dir as dns_update.py with the following values:
    - DOMAIN_ID - The id of the domain
    - RECORD_ID - The id of the DNS record you wish to update
    - TOKEN - A valid Linode API token with domain read/write permissons

3. Run the script


# References
[Linode API docs](https://www.linode.com/docs/api/domains/#domain-record-update__request-samples)
