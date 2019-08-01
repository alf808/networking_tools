#!/usr/bin/python3
'''This tool will act as your client browswer to pull html from any domain.
Usage: ./sys_info.py <URL>
Sample: ./sys_info.py https://github.com
'''
import socket
import sys
import argparse
import urllib.request

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
    output = f'''
URL: {url}
Status-code: {code}
{info}
{html}
    '''
    print(output)
    # print(f"URL: {url}")
    # print(f"Status-code: {code}")
    # print(info)
    # print(html)