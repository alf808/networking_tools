#!/usr/bin/python3
'''This tool will return information on mac addressses.
Usage: ./mac_lookup.py <mac_address>
Sample: ./mac_lookup.py 00:11:22:33:44:55
'''
import urllib.request
import json
import argparse
import sys
from datetime import datetime

if len(sys.argv) > 2:
    sys.exit("too many or not enough arguments")

start = datetime.now()
output = ""

parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool to obtain MAC address info"
    )

parser.add_argument('mac', help="mandatory MAC")
args = parser.parse_args()

mac_api_url = "http://macvendors.co/api/"

try:
    url_full = mac_api_url + args.mac + '/json'
    with urllib.request.urlopen(url_full) as response:
        result = response.read().decode('utf-8')
    obj = json.loads(result)
except:
    print("dunno what happened")
else:
    try:
        company = obj['result']['company']
        address = obj['result']['address']
    except:
        output += "unrecognizable MAC address"
    else:
        output += f"company: {company}\naddress: {address}"
finally:
    end = datetime.now()
    duration = end - start
    output += f"\nduration of task: {duration}"
    print(output)
