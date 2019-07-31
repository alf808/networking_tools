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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
open_ports = []

def scan_ip():
    print(f"begin scan {target_ip} from {port_start} to {port_end}")
    for port in range(port_start, port_end+1):
        scan_port(port)


def scan_port(port):
    try:
        status = sock.connect_ex((target_ip, port))
        if status == 0:
            open_ports.append(port)
        # return
    except:
        print("something else happened that cannot be handled")


def port_range(num, min=0, max=65535):
    '''verify if port is within range from 0 to 65535'''
    value = int(num)
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

# ensures that IP and HOST are mutually exclusive
group = parser.add_mutually_exclusive_group()
group.add_argument('-ip', help="IP must be valid")
group.add_argument('-host', help="Tool will attempt host name")

parser.add_argument('-start', type=port_range, metavar="[0-65535]", help="starting port to scan")
parser.add_argument('-end', type=port_range, metavar='[0-65535]', help="last port to scan")
args = parser.parse_args()

try:
    if sys.argv[1]=='-ip' and args.ip:
        socket.inet_aton(args.ip)
        host_data = socket.gethostbyaddr(args.ip)
        target_ip = host_data[2][0]
    elif sys.argv[1]=='-host' and args.host:
        target_ip = socket.gethostbyname(args.host)
except OSError:
    print("Unable to obtain information with that IP or host")
else:
    if sys.argv[1]=='-ip':
        print(f"The hostname is: {host_data[0]} for IP: {target_ip}")
    elif sys.argv[1]=='-host':
        print(f"The IP address of {sys.argv[2]} is: {target_ip}")
    port_start = args.start
    port_end = args.end
    scan_ip()
    if len(open_ports) == 0:
        print("no open ports")
    else:
        print(open_ports)

