#!/usr/bin/python3
'''This tool will grab the hostname of the target machine.
Usage: ./sys_info.py <IP>
Sample: ./sys_info.py 127.0.0.1
'''
import socket
import argparse
from datetime import datetime
import sys

if len(sys.argv) > 2:
    sys.exit("too many or not enough arguments")

start = datetime.now()
output = ""

parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool to convert IP to host"
    )

parser.add_argument('ip', help="mandatory IP address")
args = parser.parse_args()

try:
    socket.inet_aton(args.ip)
    ip_info = socket.gethostbyaddr(args.ip)
except OSError:
    print("valid IP please")
else:
    output += f"The hostname is: {ip_info[0]} for IP: {ip_info[2][0]}"
finally:
    end = datetime.now()
    duration = end - start
    output += f"\nduration of task: {duration}"
    print(output)