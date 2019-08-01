#!/usr/bin/python3
'''This tool will act as your client browswer to pull html from any domain.
Usage: ./client_browse.py <URL>
Sample: ./client_browse.py https://github.com
'''
import socket
import sys
import argparse
import urllib.request
from datetime import datetime

if len(sys.argv) > 2:
    sys.exit("too many or not enough arguments")

start = datetime.now()
output = ""

parser = argparse.ArgumentParser(
    prog="Network Survival Kit",
    description="command line tool which runs as a client browser"
    )

parser.add_argument('url', help="mandatory URL")
args = parser.parse_args()

try:
    with urllib.request.urlopen(args.url) as response:
        html = response.read(1000).decode('utf-8')
        url = response.geturl()
        code = response.getcode()
        info = response.info()
except urllib.error.URLError:
    print("URL error. Perhaps the URL is invalid; or URL has no http info")
except ValueError:
    print(r"Perhaps prefixation of 'http://' or 'https://' might help")
else: 
    output += f'''
URL: {url}
Status-code: {code}
{info}
{html}
    '''
finally:
    end = datetime.now()
    duration = end - start
    output += f"\nduration of task: {duration}"
    print(output)
