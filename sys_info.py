#!/usr/bin/python3
'''This tool will grab the hostname of the target machine.
Usage: ./sys_info.py <IP>
Sample: ./sys_info.py 127.0.0.1
To see how long the task completes, use the --verbose flag.
        ./sys_info.py 127.0.0.1 --verbose
'''
import socket
import sys
import argparse
import net_report


def getinfo(ip):
    output = ""
    net_report.scan_begin()
    try:
        # inet_aton tests whether IP is valid otherwise oserror
        socket.inet_aton(ip)
        ip_info = socket.gethostbyaddr(ip)
    except OSError:
        print("invalid or non-existent IP")
    else:
        output += f"The hostname is: {ip_info[0]} for IP: {ip_info[2][0]}"
    finally:
        net_report.scan_end()
        duration = net_report.show_duration()
        duration_txt = f"\nduration of task: {duration}"
        net_report.collect(output)
        return output, duration_txt


if __name__ == "__main__":

    if len(sys.argv) > 3:
        sys.exit("too many or not enough arguments")

    parser = argparse.ArgumentParser(description="command line tool to convert IP to host")

    parser.add_argument('ip', help="mandatory IP address")
    parser.add_argument('--verbose', help='output duration', action='store_true')
    args = parser.parse_args()
    ip_data = args.ip
    out, dur = getinfo(ip_data)
    print(out)
    if args.verbose:
        print(dur)
