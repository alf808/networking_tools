# Basic Networking Tools

## Introduction
standard network cli tools and applications

## Modules
There 6 modules in this package:
* **sys_info**: tool to grab hostname of the target machine

        Usage: ./sys_info.py <IP>
        Sample: ./sys_info.py 127.0.0.1

* **ip_map**: tool to return the IP address of any domain

        Usage: ./ip_map.py <hostname>
        Sample: ./ip_map.py devleague.com

* **port_scan**: tool to scan for open ports on any domain or IP

        Usage:  
        ./port_scan.py -ip <IP> -start <PORT_START> -end <PORT_END>
        ./port_scan.py -host <HOST> -start <PORT_START> -end <PORT_END>

        Sample:
        ./port_scan.py -ip 192.168.0.1 -port 50 -end 200
        ./port_scan.py -host devleague.com -port 3000 -end 5000

* **client_browse**: tool to act as a client browswer to pull html

        Usage: ./client_browse.py <URL>
        Sample: ./client_browse.py https://github.com

* **mac_lookup**: tool to return information on mac addressses

        Usage: ./mac_lookup.py <mac_address>
        Sample: ./mac_lookup.py 00:11:22:33:44:55

* **net_report**: tool collect data for network results

        not accessible through CLI


## Resources:

https://stackoverflow.com/questions/25295487/python-argparse-value-range-help-message-appearance

https://docs.python.org/3/library/socket.html

https://docs.python.org/3/howto/argparse.html

https://docs.python.org/3/library/urllib.request.html

https://docs.python.org/2/howto/urllib2.html

https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script

http://macvendors.co/api/