#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from requests.auth import HTTPBasicAuth
from asa_login_info import asa_server, asa_username, asa_password, http_headers
from asa_get_token import get_token
import pprint
import time

api_path = "/api/interfaces/physical"
url = asa_server + api_path


# 获取所有接口信息, 新令牌
def get_ifs():
    request_result = requests.get(url, headers=get_token(), verify=False)
    if request_result.ok:
        return request_result.json().get('items')


# 获取所有接口信息, 传入令牌
def get_ifs_token(access_token):
    request_result = requests.get(url, headers=access_token, verify=False)
    if request_result.ok:
        return request_result.json().get('items')


# 获取特定接口信息, 新令牌
def get_spec_if(if_name):
    for if_info in get_ifs():
        if if_info.get('hardwareID') == if_name:
            return if_info


# 获取特定接口信息, 传入令牌
def get_spec_if_token(if_name, access_token):
    for if_info in get_ifs_token(access_token):
        if if_info.get('hardwareID') == if_name:
            return if_info


# 配置特定接口, 新令牌
def post_spec_if(if_name, nameif, security_level, ipadd, netmask, shutdown=False):
    post_data = {
                 "interfaceDesc": "Update description in PATCH",
                 "name": nameif,
                 "securityLevel": security_level,
                 "shutdown": shutdown,
                 "ipAddress": {
                                "kind": "StaticIP",
                                "ip": {
                                        "kind": "IPv4Address",
                                        "value": ipadd
                                        },
                                "netMask": {
                                        "kind": "IPv4NetMask",
                                        "value": netmask
                                            }
                                }
                }
    url = asa_server + api_path + '/' + get_spec_if(if_name).get('objectId')

    request_result = requests.patch(url, headers=get_token(), json=post_data, verify=False)

    if request_result.text:
        return request_result.json()


# 配置特定接口, 传入令牌
def post_spec_if_token(if_name, nameif, security_level, ipadd, netmask, access_token, shutdown=False):
    post_data = {
                 "interfaceDesc": "Update description in PATCH",
                 "name": nameif,
                 "securityLevel": security_level,
                 "shutdown": shutdown,
                 "ipAddress": {
                                "kind": "StaticIP",
                                "ip": {
                                        "kind": "IPv4Address",
                                        "value": ipadd
                                        },
                                "netMask": {
                                        "kind": "IPv4NetMask",
                                        "value": netmask
                                            }
                                }
                }
    url = asa_server + api_path + '/' + get_spec_if_token(if_name, access_token=access_token).get('objectId')

    request_result = requests.patch(url, headers=access_token, json=post_data, verify=False)

    if request_result.text:
        return request_result.json()


if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    # 获取令牌
    access_token = get_token()

    # 配置接口, 传入令牌
    post_spec_if_token('GigabitEthernet0/1', 'Inside', 100, '10.1.1.254', '255.255.255.0', access_token=access_token)
    post_spec_if_token('GigabitEthernet0/2', 'DMZ', 50, '172.16.1.254', '255.255.255.0', access_token=access_token)

    # 查看接口, 传入令牌
    pp.pprint(get_spec_if_token('GigabitEthernet0/1', access_token=access_token))
    # pp.pprint(get_ifs_token(access_token=access_token))
