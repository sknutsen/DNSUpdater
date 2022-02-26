#!/bin/bash
# Creates a crontab which runs the script once every 6 hours and appends it to the existing 
# crontab list while also removing duplicates
(crontab -l, echo "0 */6 * * * python3 ./dns_update.py") | sort -u | crontab -
