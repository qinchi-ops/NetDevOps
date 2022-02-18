#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from datetime import datetime, date
from flask import Flask, render_template, request
import os
# 默认目录为当前目录的templates
template_dir = os.path.abspath('../templates')
# 修改目录
node = Flask(__name__, template_folder=template_dir)
# 打开Debug
node.debug = True


# 静态路由,最简单页面
@node.route('/', methods=['GET'])
def index():
    return "qytang flask home"


# 静态路由,最简单页面
@node.route('/html', methods=['GET'])
def html():
    return render_template('index.html')  # 模板文件在templates目录


@node.route('/template', methods=['GET'])
def template():
    return render_template('template.html', template='welcome to qytang!')


@node.route('/dynamic/<dynamic_name>', methods=['GET'])
def dynamic(dynamic_name):
    return render_template('dynamic.html', dynamic=dynamic_name)


@node.route('/complex', methods=['GET'])
def complex_data():
    return render_template('complex.html',
                           complex_dict={'dict_key':  'dict_value'},
                           complex_list=['list1', 'list2'])


@node.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return render_template('form_result.html',
                               name=name,
                               age=age)
    else:
        return render_template('form.html')


@node.route('/rpc/<rfc_func>', methods=['GET'])
def rpc(rfc_func):
    # response.content_type = 'application/json'
    if rfc_func == 'datetime':
        return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    elif rfc_func == 'date':
        return {'datetime': date.today().strftime('%Y-%m-%d')}
    else:
        return {'error': 'function not find!'}


@node.route('/rpc_function', methods=['POST'])
def rpc_function():
    # response.content_type = 'application/json'
    client_post_data = request.json
    if client_post_data:
        client_function = client_post_data.get('function')
        if client_function == 'datetime':
            return {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        elif client_function == 'date':
            return {'datetime': date.today().strftime('%Y-%m-%d')}
        else:
            return {'error': 'function not found!'}
    else:
        return {'error': 'no json data'}


if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
