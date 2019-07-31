#!/usr/bin/python3

import socket
import argparse

print("convert host to IP")
print("example: google.com")

parser = argparse.ArgumentParser()

parser.add_argument('host', help="domain name here")
args = parser.parse_args()

dom = args.host

print(socket.gethostbyname(dom))
