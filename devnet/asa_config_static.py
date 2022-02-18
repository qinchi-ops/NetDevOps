#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from asa_login_info import asa_server, asa_username, asa_password, http_headers
from asa_get_token import get_token
import pprint
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_path = "/api/routing/static"
url = asa_server + api_path


# 配置静态路由, 传入令牌
def post_static_route_token(nameif, dst_net, next_hop, access_token):
    if dst_net == 'default':
        dst_kind = "AnyIPAddress"
        dst_value = "any4"
    else:
        dst_kind = "IPv4Network"
        dst_value = dst_net
    post_data = {
                  "kind": "object#IPv4Route",
                  "gateway": {
                                "kind": "IPv4Address",
                                "value": next_hop
                              },
                  "distanceMetric": 1,
                  "network": {
                                "kind": dst_kind,
                                "value": dst_value
                              },
                  "tracked": False,
                  "tunneled": False,
                  "interface": {
                                "kind": "objectRef#Interface",
                                "name": nameif
                              }
                }

    request_result = requests.post(url, headers=access_token, json=post_data, verify=False)

    if request_result.text:
        return request_result.json()


if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=4)

    access_token = get_token()
    post_static_route_token('Inside', '2.2.2.0/24', '10.1.1.1', access_token)
    post_static_route_token('3.3.3.0/24', '4.4.4.0/24', '172.16.1.1', access_token)
