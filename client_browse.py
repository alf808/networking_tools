#!/usr/bin/python3
'''This tool will act as your client browswer to pull html from any domain.
Usage: ./client_browse.py <URL>
Sample: ./client_browse.py https://github.com
'''
import argparse
import sys
import urllib.request
import net_report


def getinfo(ur):
    net_report.scan_begin()
    output = ""
    try:
        with urllib.request.urlopen(ur) as response:
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
        net_report.scan_end()
        duration = net_report.show_duration()
        output += f"\nduration of task: {duration}"
        net_report.collect(output)
        return output


if __name__ == "__main__":

    if len(sys.argv) > 2:
        sys.exit("too many or not enough arguments")

    parser = argparse.ArgumentParser(description="command line tool which runs as a client browser")

    parser.add_argument('url', help="mandatory URL")
    args = parser.parse_args()
    
    print(getinfo(args.url))