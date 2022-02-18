#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
from ssh import device_ssh
from ping import device_ping
import re
import pprint

def router_get_if(*ips,username='admin',password='Cisco123'):
    device_if_dict = {}
    for ip in ips:
        #device_ping(*ips)
        device_if_dict={ip:dict(re.findall('(Ethernet\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', device_ssh(*ips,username,password,cmd='show ip int bri ')))}
        return device_if_dict

if __name__ == "__main__":
    pprint.pprint(router_get_if('192.168.19.201',username='cisco', password='cisco123'), indent=4)
    pprint.pprint(router_get_if('192.168.19.202',username='cisco', password='cisco123'), indent=4)
    pprint.pprint(router_get_if('192.168.19.203',username='cisco', password='cisco123'), indent=4)