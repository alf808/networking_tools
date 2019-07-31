#!/usr/bin/python3

import socket
import argparse

print("convert IP to host")
print("example: 127.0.0.1")

parser = argparse.ArgumentParser()

parser.add_argument('ip', help="domain name here")
args = parser.parse_args()

ip_data = args.ip

print(socket.gethostbyaddr(ip_data))
