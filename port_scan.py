#!/usr/bin/python3
'''This tool will scan for open ports on any domain or IP and return a report
when completed.
Usage:  ./port_scan.py -ip <IP>
        ./port_scan.py -host <HOST>
Sample: ./port_scan.py -ip 192.168.0.1
        ./port_scan.py -host devleague.com
'''
import socket
import argparse
import sys

def scan_ip(ip):
    print(f"begin scan {ip}")


if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit("too many or not enough arguments")

parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool to scan ports of an IP or host"
)

parser.add_argument('-ip', help="IP must be valid")
parser.add_argument('-host', help="Tool will attempt host name")

args = parser.parse_args()

try:
    if sys.argv[1]=='-ip' and args.ip:
        socket.inet_aton(args.ip)
        host_data = socket.gethostbyaddr(args.ip)
        ip_data = host_data[2][0]
    elif sys.argv[1]=='-host' and args.host:
        ip_data = socket.gethostbyname(args.host)
except OSError:
    print("Unable to obtain information with that IP or host")
else:
    if sys.argv[1]=='-ip':
        print(f"The hostname is: {host_data[0]} for IP: {ip_data}")
    elif sys.argv[1]=='-host':
        print(f"The IP address of {sys.argv[2]} is: {ip_data}")
    scan_ip(ip_data)


