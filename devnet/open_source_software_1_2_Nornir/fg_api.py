#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
import json
url_login = "https://192.168.16.1/fpc/api/login"

client = requests.session()

# Login request

payload = {
    'user': 'username',
    'password': 'password'}

r = client.post(url_login, json=payload, verify=False)

print(r.status_code)
# # Retrieve session id. Add to HTTP header for future messages
#
# parsed_json = json.loads(r.text)
#
# sid = parsed_json['fpc-sid']
#
# headers = {'fpc-sid': sid}
#
# url_cust_req="https://192.168.16.1/fpc/api/customers/1/users"

# r = client.get(url_cust_req, headers=headers, verify=False)
if __name__ == '__main__':
    pass
