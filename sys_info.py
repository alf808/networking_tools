#!/usr/bin/python3
'''This tool will grab the hostname of the target machine.
Usage: ./sys_info.py <IP>
Sample: ./sys_info.py 127.0.0.1
'''
import socket
import argparse
import net_report


def getinfo():
    net_report.scan_begin()
    output = ""

    parser = argparse.ArgumentParser(
        prog="Network Survival Kit",
        description="command line tool to convert IP to host"
        )

    parser.add_argument('ip', help="mandatory IP address")
    args = parser.parse_args()

    try:
        # inet_aton tests whether IP is valid otherwise oserror
        socket.inet_aton(args.ip)
        ip_info = socket.gethostbyaddr(args.ip)
    except OSError:
        print("invalid or non-existent IP")
    else:
        output += f"The hostname is: {ip_info[0]} for IP: {ip_info[2][0]}"
    finally:
        net_report.scan_end()
        duration = net_report.show_duration()
        output += f"\nduration of task: {duration}"
        print(output)
        net_report.collect(output)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        sys.exit("too many or not enough arguments")

    getinfo()