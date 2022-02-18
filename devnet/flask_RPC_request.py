#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import requests

# 请求GET动态路由RPC, 动态参数为datetime
# request_result = requests.get('http://192.168.1.100:8080/rpc/datetime')
request_result = requests.get('http://192.168.19.3:8080/rpc/datetime')

# 打印文本
print(request_result.text)
# 打印文本数据类型
print(type(request_result.text))
# 打印把文本通过json转换后的字典
print(request_result.json())
# 打印转换后的数据类型
print(type(request_result.json()))

# 请求GET动态路由RPC, 动态参数为date
# request_result = requests.get('http://192.168.1.100:8080/rpc/date')
request_result = requests.get('http://192.168.19.3:8080/rpc/date')

print(request_result.json())

# 请求GET动态路由RPC, 动态参数为other
# request_result = requests.get('http://192.168.1.100:8080/rpc/other')
request_result = requests.get('http://192.168.19.3:8080/rpc/other')

print(request_result.json())
