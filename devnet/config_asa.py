#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token_url = 'https://192.168.19.211/api/tokenservices'
object_url = "https://192.168.19.211/api/objects/networkobjects"


username = 'cisco'
password = 'cisco'

#HTTP Basci认证


def get_token():
    r =  requests.post(
        token_url,
        auth=HTTPBasicAuth(username,password),
        verify=False
        )

    token = r.headers.get('X-Auth-Token')
    return token


def create_asa_object(object_name,ip_address,token):
    object_dict = {
        "kind": "object#NetworkObj",
        "name": object_name,
        "host": {
            "kind": "IPv4Address",
            "value": ip_address
        }
    }
    headers_dcit = {
        "Content-Type":"application/json",
        "Accept":"application/json",
        "X-Auth-Token":token
    }
    request_result = requests.post(object_url,
                                   headers=headers_dcit,
                                   verify=False,
                                   json=object_dict
                                   )
    print(request_result.status_code)

if __name__ == '__main__':
    token =get_token()
    create_asa_object('restapi_test1','1.1.1.1',token)
