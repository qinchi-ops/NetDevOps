#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from datetime import datetime, date
from flask import Flask, request, Response
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import json
import os
import base64

node = Flask(__name__)
# 打开Debug
node.debug = True


# GET使用动态路由实现RPC
# @node.route('/rpc/<rpc_func>', methods=['GET'])
# def rpc(rpc_func):
#     # 如果动态传入的参数为'datetime'
#     if rpc_func == 'datetime':
#         # 返回时间datetime(JSON需要格式化)
#         # response需要通过json转换为字符串
#         # 响应码为200
#         # mimetype为'application/json'
#         return Response(response=json.dumps({'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}),
#                         status=200,
#                         mimetype='application/json')
#     # 如果动态传入的参数为'date'
#     elif rpc_func == 'date':
#         # 返回日期date(JSON需要格式化)
#         return {'datetime': date.today().strftime('%Y-%m-%d')}
#     # 如果参数其他参数, 就报错('error'), 'function not find!'
#     else:
#         return {'error': 'function not find!'}

@node.route('/cmd/<rpc_func>', methods=['GET'])
def rpc(rpc_func):
    # 如果动态传入的参数为'datetime'
    if rpc_func == 'ifconfig':
        # 返回时间datetime(JSON需要格式化)
        # response需要通过json转换为字符串
        # 响应码为200
        # mimetype为'application/json'
        return Response(response=json.dumps({'ifconfig':os.popen('ifconfig').read()}),
                        status=200,
                        mimetype='application/json')
    # 如果动态传入的参数为'date'
    # elif rpc_func == 'date':
    #     # 返回日期date(JSON需要格式化)
    #     return {'datetime': date.today().strftime('%Y-%m-%d')}
    # 如果参数其他参数, 就报错('error'), 'function not find!'
    else:
        return {'error': 'no cmd in json!'}
# ifconfig_result = os.popen('ifconfig').read()
# print (os.popen('ifconfig').read())

# UPLOAD_FOLDER = '/devnet/upload'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return  {'message': 'upload success!', 'uploadfile': filename}
#
#             # return redirect(url_for('uploaded_file',
#             #                         filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''
@node.route('/upload', methods=['POST'])
def upload():
    # 将请求的json文件赋值于变量
    upload_json = request.json
    # 提取key值
    upload_key = list(upload_json.keys())[0]
    # 提取value值是一个list类型
    res_upload = upload_json.get('upload_file')
    # list[1]为文件的base64内容
    base64_file = res_upload[1]
    # base64解码得到文件二进制内容
    result_file = base64.b64decode(base64_file)
    # 将文件写入指定目录文件名下
    with open('/devnet/upload/' + res_upload[0], 'wb') as f:
        f.write(result_file)
        f.close()
        return {'meassage': 'Upload success', upload_key: res_upload[0]}

@node.route('/download', methods=['POST'])
def download():
    download_dict = {}
    # 提取POST请求携带的json数据
    download_json = request.json
    # 提取key值
    download_value = download_json.get('download_file')
    # 创建一个空列表春芳
    download_list = [download_value]
    # 判断key值
    if 'logo.png' == download_value:
        # 创建一个返回的空字典
        with open('/devnet/download/' + download_value, 'rb') as f:
            # 将文件内容转换成base64
            base64_file = str(base64.b64encode(f.read()), "utf-8")
            # base64_filename = str(base64.b64encode(download_key),"utf-8")
            download_list.append(base64_file)
            # 将key和value添加至返回的空列表
            download_dict['download_file'] = download_list
            return download_dict
    else:
        return {'error': 'download file not exist!'}

# @node.route('/upload', methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return {'message': 'upload success!','uploadfile':filename}
#             # return redirect(url_for('uploaded_file',
#             #                         filename=filename))
#             # <form method=post enctype=multipart/form-data>
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

# @node.route('/upload/file', methods=['POST'])
# def rpc_function(file):
#     # response.content_type = 'application/json'
#     client_post_data = request.json
#     if client_post_data:
#         client_function = client_post_data.get('function')
#         if file == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file :
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return {'message': 'upload success!','uploadfile':filename}




# # POST实现JSON RPC
# @node.route('/upload/rpc_function', methods=['POST'])
# def rpc_function():
#     # 提取POST请求数据中的JSON数据
#     client_post_data = request.json
#     # 如果存在JSON数据
#     if client_post_data:
#         # 提取键'function'
#         client_function = client_post_data.get('function')
#         # 如果键'function'的值为datetime, 就返回时间datetime(JSON需要格式化)
#         if client_function == 'datetime':
#             # 返回时间datetime(JSON需要格式化)
#             # response需要通过json转换为字符串
#             # 相应码为200
#             # mimetype为'application/json'
#             return Response(response=json.dumps({'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}),
#                             status=200,
#                             mimetype='application/json')
#         # 如果键'function'的值为date, 就返回日期date(JSON需要格式化)
#         elif client_function == 'date':
#             return {'datetime': date.today().strftime('%Y-%m-%d')}
#         # 如果没有键'function', 就报错('error'), 'function not found!'
#         else:
#             return {'error': 'function not found!'}
#     # 如果没有JSON数据, 就报错('error'), 'no json data'
#     else:
#         return {'error': 'no json data'}


if __name__ == "__main__":
    # 运行Flask在host='192.168.1.200', port=8080
    # 在linux上可以使用'0.0.0.0'
    node.run(host='0.0.0.0', port=8080)
