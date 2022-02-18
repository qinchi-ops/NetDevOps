#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
event manager applet ospf_rpc

    event syslog pattern "OSPF-5-ADJCHG"

    action 1.0 regexp "from [A-Z]+ to [A-Z]+" "$_syslog_msg" ospf_status

    action 2.0 regexp "GigabitEthernet[0-9/]+" "$_syslog_msg" ifname

    action 3.0 cli command "enable"

    action 4.0 cli command "guestshell run python3 /home/guestshell/eem_json_rpc_client.py $ospf_status $ifname"
'''

import requests
from cli import cli
import sys


r = requests.post('http://192.168.19.3:8080/eem', json={'event': 'ospf', 'event_detail': sys.argv[4], 'interface': sys.argv[5]})
result_cmd = r.json().get('cmd')
output = cli(result_cmd)

print(output)