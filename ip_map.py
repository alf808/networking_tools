#!/usr/bin/python3
'''This tool will return the corresponding IP address of any domain entered.
Usage: ./ip_map.py <hostname>
Sample: ./ip_map.py devleague.com
'''
import socket
import argparse
import net_report


def getinfo():
    net_report.scan_begin()
    output = ""

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
        output += f"The IP address of {temp_host} is: {temp_ip}"
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