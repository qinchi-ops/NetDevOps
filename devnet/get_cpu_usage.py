#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from  restconf_0_header import client, username, password, csr1_ip, csr2_ip, headers
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def csr_monitor_cpu(device_ip, username, password, monitor_type='5s'):
    monitor_type_use = 'five-seconds'
    if monitor_type == '1m':
        monitor_type_use = 'one-minute'
    elif monitor_type == '5m':
        monitor_type_use = 'five-minutes'
    else:
        monitor_type_use = 'five-seconds'

    url = "https://" + device_ip + "/restconf/data/Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/" + monitor_type_use

    r = client.get(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    # 返回回显的JSON数据
    if r.ok:
        return r.json().get(f'Cisco-IOS-XE-process-cpu-oper:{monitor_type_use}')
    else:
        return '出现故障'


if __name__ == "__main__":
    print(csr_monitor_cpu('192.168.19.206', 'cisco', 'cisco123', '5s'))