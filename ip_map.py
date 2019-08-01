#!/usr/bin/python3
'''This tool will return the corresponding IP address of any domain entered.
Usage: ./ip_map.py <hostname>
Sample: ./ip_map.py devleague.com
'''
import socket
import argparse
import sys

if len(sys.argv) != 2:
    sys.exit("too many or not enough arguments")
    
parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool to obtain IP from host"
)

parser.add_argument('host', help="mandatory host name")
args = parser.parse_args()

temp_host = sys.argv[1]

try:
    temp_ip = socket.gethostbyname(args.host)
except OSError:
    print("Unable to obtain IP with that hostname")
else:
    print(f"The IP address of {temp_host} is: {temp_ip}")