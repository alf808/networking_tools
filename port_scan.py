#!/usr/bin/python3
'''This tool will scan for open ports on any domain or IP and return a report
when completed.
Usage:  
        ./port_scan.py -ip <IP> -start <PORT_START> -end <PORT_END>
        ./port_scan.py -host <HOST> -start <PORT_START> -end <PORT_END>

Sample:
        ./port_scan.py -ip 192.168.0.1 -port 50 -end 200
        ./port_scan.py -host devleague.com -port 3000 -end 5000
'''
import socket
import argparse
import sys

def scan_ip(ip, start_port, end_port):
    print(f"begin scan {ip} from {start_port} to {end_port}")


def range_type(astr, min=0, max=65535):
    '''verify if port is within range of 0 to 65535'''
    value = int(astr)
    if min<= value <= max:
        return value
    else:
        raise argparse.ArgumentTypeError('value not in range %s-%s'%(min,max))


if len(sys.argv) < 2 or len(sys.argv) > 7:
    sys.exit("too many or not enough arguments")

parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool to scan ports of an IP or host"
)

group = parser.add_mutually_exclusive_group()
group.add_argument('-ip', help="IP must be valid")
group.add_argument('-host', help="Tool will attempt host name")

parser.add_argument('-start', type=range_type, metavar="[0-65535]", help="starting port to scan")
parser.add_argument('-end', type=range_type, metavar='[0-65535]', help="last port to scan")
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
    scan_ip(ip_data, args.start, args.end)


