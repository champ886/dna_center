import json
from pprint import pprint

json_dict = {'interface': {'name': 'GigabitEthernet1', 'description':
'Router Uplink', 'enabled': True, 'ipv4': {'address':
[{'ip': '192.168.0.2', 'netmask': '255.255.255.0'}]}}}

pprint(json_dict["interface"])
pprint(json_dict ["interface"] ["ipv4"])