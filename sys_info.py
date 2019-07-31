#!/usr/bin/python3
'''This tool will grab the hostname of the target machine.
Usage: ./sys_info.py <IP>
Sample: ./sys_info.py 127.0.0.1
'''
import socket
import argparse

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
    print(f"The hostname is: {ip_info[0]} for IP: {ip_info[2][0]}")
