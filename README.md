# DNSUpdater

Updates a given Cloudflare or Linode DNS record

# Dependencies

- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [domeneshop](https://github.com/domeneshop/python-domeneshop)

# How to use

1. Install python-dotenv and domeneshop.

   ```
   pip3 install python-dotenv
   ```

   ```
   pip3 install domeneshop
   ```

2. Create a .env file in the same directory as dns_update.py with the following values depending on the provider:

   - All:

     - PROVIDER - Name of the provider (linode or cloudflare or domeneshop)

   - Cloudflare:

     - AUTH_MODE - global for global auth key, or token for auth token

     - AUTH_EMAIL - Cloudflare account email

     - AUTH_KEY - Global auth key if global, or auth token if token

     - ZONE_ID - Zone identifier

     - RECORD_NAME - Record name

     - RECORD_TYPE - Record type of A, AAAA etc

   - Domeneshop: (Use either ID or NAME)

     - DOMAIN_ID - The id of the domain

     - RECORD_ID - The id of the DNS record you wish to update

     - DOMAIN_NAME - The name of the domain

     - RECORD_NAME - The name of the DNS record you wish to update

     - TOKEN - A Domeneshop API token

     - SECRET - A Domeneshop API secret

   - Linode:

     - DOMAIN_ID - The id of the domain

     - RECORD_ID - The id of the DNS record you wish to update

     - TOKEN - A valid Linode API token with domain read/write permissons

3. Run the [script](dns_update.py)

   ```
   python3 dns_update.py
   ```

4. (Optional) Run the [auto update setup script](auto_update_setup.sh) to set up a cronjob that runs the script once every 6 hours
   ```
   ./auto_update_setup.sh
   ```

# References used

- [Cloudflare API docs](https://api.cloudflare.com)
- [Domeneshop API docs](https://api.domeneshop.no/docs/#section/Overview)
- [K0p1-Git's cloudflare-dns-updater](https://github.com/K0p1-Git/cloudflare-ddns-updater)
- [Linode API docs](https://www.linode.com/docs/api/domains/#domain-record-update__request-samples)
