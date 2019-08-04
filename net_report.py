#!/usr/bin/python3
'''This tool will automate transfering of data for all network findings.
Usage: ./net_report.py
Sample: ./net_report.py
'''
import argparse
from datetime import datetime

begin = None
end = None

def scan_begin():
    global begin
    begin = datetime.now()


def scan_end():
    global end
    end = datetime.now()


def show_duration():
    return end - begin


def collect(d):
    with open('network_info.txt', 'a') as fo:
        data = '\n' + str(begin) + '\n'
        data += d
        fo.write(data)

if __name__ == '__main__':
    pass