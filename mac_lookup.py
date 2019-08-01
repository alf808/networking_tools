#!/usr/bin/python3
'''This tool will return information on mac addressses.
Usage: ./mac_lookup.py <mac_address>
Sample: ./mac_lookup.py 00:11:22:33:44:55
'''
import urllib2
import json
import codecs
import argparse

parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool to convert IP to host"
    )

parser.add_argument('url', help="mandatory url")
args = parser.parse_args()

mac_api_url = "http://macvendors.co/api/"

request = urllib2.Request(mac_api_url + args.url, headers={'User-Agent' : "API Browser"}) 

response = urllib2.urlopen( request )
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))

company =obj['result']['company']
address =obj['result']['address']

print(company.encode("ascii","replace"),address.encode("ascii","replace"))
