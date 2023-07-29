#!/bin/bash
# Creates a crontab which runs the script once every 6 hours and appends it to the existing 
# crontab list while also removing duplicates
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

echo "Installing dependencies..."
pip3 install python-dotenv
pip3 install domeneshop

printf "$(crontab -l)\n0 */6 * * * python3 $parent_path/dns_update.py\n" | sort -u | crontab -
echo "Added cronjob"
