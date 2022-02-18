#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from netmiko import ConnectHandler
my_fg = {

    'host':'fg-mct',
    'device_type':'cisco_asa',
    'ip':'192.168.19.211',
    'username':'cisco',
    'password':'cisco',
    'secret': 'Cisc0123'
}

server = {

    'host':'server',
    'device_type':'linux',
    'ip':'192.168.19.5',
    'username':'centos',
    'password':'centos'
}
# net_connect = ConnectHandler(**my_fg)
net_connect = ConnectHandler(**server)

output = net_connect.send_command('ifconfig ens33')

print(output)
# with open ('fgconf.cfg','w') as f:
# 	for line in output:
# 		f.write(line)
