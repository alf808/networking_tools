#!/usr/bin/python3
'''This tool will return the corresponding IP address of any domain entered.
Usage: ./ip_map.py <hostname>
Sample: ./ip_map.py devleague.com
'''
import socket
import sys
import argparse
import net_report


def getinfo(hn):
    net_report.scan_begin()
    output = ""
    try:
        temp_ip = socket.gethostbyname(hn)
    except OSError:
        print("Unable to obtain IP with that hostname")
    else:
        output += f"The IP address of {hn} is: {temp_ip}"
    finally:
        net_report.scan_end()
        duration = net_report.show_duration()
        output += f"\nduration of task: {duration}"
        net_report.collect(output)
        return output


if __name__ == "__main__":

    if len(sys.argv) > 2:
        sys.exit("too many or not enough arguments")

    parser = argparse.ArgumentParser(description="command line tool to obtain IP from host")

    parser.add_argument('host', help="mandatory host name")
    args = parser.parse_args()
    arg_host = args.host
    temp_host = sys.argv[1]

    print(getinfo(arg_host))
