#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from datetime import datetime, date
from flask import Flask, request, Response
import json

node = Flask(__name__)
# 打开Debug
node.debug = True


# GET使用动态路由实现RPC
@node.route('/rpc/<rpc_func>', methods=['GET'])
def rpc(rpc_func):
    # 如果动态传入的参数为'datetime'
    if rpc_func == 'datetime':
        # 返回时间datetime(JSON需要格式化)
        # response需要通过json转换为字符串
        # 响应码为200
        # mimetype为'application/json'
        return Response(response=json.dumps({'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}),
                        status=200,
                        mimetype='application/json')
    # 如果动态传入的参数为'date'
    elif rpc_func == 'date':
        # 返回日期date(JSON需要格式化)
        return {'datetime': date.today().strftime('%Y-%m-%d')}
    # 如果参数其他参数, 就报错('error'), 'function not find!'
    else:
        return {'error': 'function not find!'}


# POST实现JSON RPC
@node.route('/rpc_function', methods=['POST'])
def rpc_function():
    # 提取POST请求数据中的JSON数据
    client_post_data = request.json
    # 如果存在JSON数据
    if client_post_data:
        # 提取键'function'
        client_function = client_post_data.get('function')
        # 如果键'function'的值为datetime, 就返回时间datetime(JSON需要格式化)
        if client_function == 'datetime':
            # 返回时间datetime(JSON需要格式化)
            # response需要通过json转换为字符串
            # 相应码为200
            # mimetype为'application/json'
            return Response(response=json.dumps({'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}),
                            status=200,
                            mimetype='application/json')
        # 如果键'function'的值为date, 就返回日期date(JSON需要格式化)
        elif client_function == 'date':
            return {'datetime': date.today().strftime('%Y-%m-%d')}
        # 如果没有键'function', 就报错('error'), 'function not found!'
        else:
            return {'error': 'function not found!'}
    # 如果没有JSON数据, 就报错('error'), 'no json data'
    else:
        return {'error': 'no json data'}


if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
