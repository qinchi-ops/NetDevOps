#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

switchuser = 'admin'
switchpassword = 'admin'
url = 'https://192.168.19.207/ins'
myheaders = {'content-type': 'application/json-rpc'}
client = requests.session()

def create_cmd_dict(cli_cmd, cmd_id):
    cmd_dict = {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": cli_cmd,
            "version": 1
        },
        "id": cmd_id
    }
    return cmd_dict

def json_rpc_cmd(cmd_list):
    i = 1
    cmds_list = []
    for cmd in cmd_list:
        cmds_list.append(create_cmd_dict(cmd, i))
        i += 1
    response = client.post(url, json=cmds_list, headers=myheaders, auth=HTTPBasicAuth(switchuser, switchpassword),
                           verify=False)
    return response.json()

if __name__ == '__main__':
    for x in json_rpc_cmd(['show ip route'])['result']['body']['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']:
        # print(x['TABLE_path']['ROW_path'])
        # print(x['TABLE_path']['ROW_path']['clientname'])
        if x['TABLE_path']['ROW_path']['clientname'] == 'static':
            print(x['ipprefix'],x ['TABLE_path']['ROW_path']['ipnexthop'])
