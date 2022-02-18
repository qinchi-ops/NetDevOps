#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from  restconf_0_header import client, username, password, csr1_ip, csr2_ip, headers
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def config_logging(ip, username, password, hostip, severity,status=True):
    url = "https://" + ip + "/restconf/data/Cisco-IOS-XE-native:native/logging"
    json_data = {
        "logging": {
            "hostip": hostip,
            "trap": {
                "severity": severity
            }
        }
    }
    r = client.patch(url, headers=headers, auth=HTTPBasicAuth(username, password), json=json_data, verify=False)
    # 返回回显的JSON数据
    if r.ok:
        print('提交成功')
    else:
        print(r.json())


if __name__ == "__main__":
    config_logging('192.168.19.206', 'cisco', 'cisco123', '192.168.19.3',7)
