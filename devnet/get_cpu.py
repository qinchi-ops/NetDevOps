#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from ncclient import manager
from ncclient.operations import RPCError
import lxml.etree as ET
import xmltodict
from jinja2 import Template
tem_path = './'

def csr_monitor_cpu(device_ip, username, password, monitor_type='5s'):
    if monitor_type == '1m':
        monitor_type_use = 'one-minute'
    elif monitor_type == '5m':
        monitor_type_use = 'five-minutes'
    else:
        monitor_type_use = 'five-seconds'
    result_xml = csr_netconf_monitor(device_ip, username, password, netconf_monitor_cpu(monitor_type_use), port='830')
    xmldict = xmltodict.parse(result_xml)
    return xmldict['rpc-reply']['data']['cpu-usage']['cpu-utilization'][monitor_type_use]



def netconf_monitor_cpu(monitor_type):
    with open(tem_path + 'fivecpu.xml', encoding='utf-8') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(monitor_type_use=monitor_type)
    return netconf_payload


def csr_netconf_monitor(ip, username, password, payload_xml, port='830'):
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            response = m.get(payload_xml).xml
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        return ET.tostring(data).decode()



def netconf_config_syslog(severity, host_ip):
    with open(tem_path + 'syslog.xml', encoding='utf-8') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(severity=severity, host_ip=host_ip)
    return netconf_payload


def csr_netconf_config(ip, username, password, payload_xml, port='830'):
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            response = m.edit_config(target='running', config=payload_xml).xml

            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        return ET.tostring(data).decode()


if __name__ == '__main__':
    # print(csr_monitor_cpu('192.168.19.206', 'cisco', 'cisco123', '5s'))
    print(csr_netconf_config('192.168.19.206', 'cisco', 'cisco123', netconf_config_syslog('7', '192.168.19.3'), port='830'))
