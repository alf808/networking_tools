import sys_info
import ip_map
import client_browse
import mac_lookup

print(sys_info.getinfo('8.8.8.8'))
print(ip_map.getinfo('devleague.com'))
print(client_browse.getinfo('https://www.python.org'))
print(mac_lookup.getinfo('08:00:27:6f:41:e0'))