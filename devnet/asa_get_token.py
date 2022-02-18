#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from  asa_login_info import asa_server, asa_username, asa_password, http_headers
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_path = "/api/tokenservices"
url = asa_server + api_path


def get_token():
    try:
        # 基本认证的POST HTTPS请求, 添加自定义头部
        resp = requests.post(url,
                             headers=http_headers,
                             auth=HTTPBasicAuth(asa_username, asa_password),
                             verify=False)
        # 注意要copy! 否则原始的字典就被修改了
        final_header = http_headers.copy()
        # 在字典中加入认证后获取的'X-Auth-Token'头部
        final_header['X-Auth-Token'] = resp.headers['X-Auth-Token']
        # 返回插入了'X-Auth-Token'头部的字典
        return final_header
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_token())
