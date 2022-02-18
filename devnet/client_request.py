#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from pprint import pprint

import requests
import base64
from bs4 import BeautifulSoup


file = 'request_header.txt'

def input_header(file):
    f = open(file, 'r')
    headers_list = [x.split(':') for x in f]
    headers = {a[0]: a[1].strip() for a in headers_list}
    # pprint(headers, indent=4)
    return headers
server_ip = '192.168.19.3'
server_port = '8080'
base_url = 'http://' + server_ip +':'+server_port+'/'
#执行命令的URL
exec_cmd_url = base_url + 'cmd'
#上传文件的URL
upload_url = base_url + 'upload'
#下载文件的URL
download_url = base_url +'download'

upload_file_dir = './client_upload_file_dir/'
download_file_dir = './client_download_file_dir/'

def json_rpc_client_exec_cmd(exec_cmd):
    for key,values in exec_cmd.items():
        if values == 'ifconfig' or values =='pwd':
            # print(exec_cmd_url+'/'+values)
            # return requests.get(exec_cmd_url+'/'+values)
            result= (requests.get(exec_cmd_url + '/' + values,headers=input_header(file))).json()
            # print(result)
            # pprint(result,indent=4)
            for x, y in result.items():
                return y
            # return (values for key,values in result)
            # return requests.get(exec_cmd_url + '/' + values, headers=input_header(file))
        else:
            return values + '不是内部或则和外部命令,也不是可运行的程序或者批处理文件'

def json_rpc_client_upload(file_name):
    # 创建一个空字典准备传递json数据用
    upload_dict = {}
    # 创建列表包含上传文件名，
    upload_list = [file_name]
    # 打开文件读取二进制内容
    with open(upload_file_dir + file_name, 'rb') as f:
        # 将内容转换为base64格式
        base64_file = str(base64.b64encode(f.read()), "utf-8")
        # 列表添加文件内容格式为base64
        upload_list.append(base64_file)
        # 列表添加value 为文件名和内容的列表 {'key':['a','b']}
        upload_dict['upload_file'] = upload_list
        # 请求上传文件的url并附带上传文件json数据
        result = requests.post(upload_url, json=upload_dict)
        # 关闭文件
        f.close()
        # 返回服务器返回的内容
        return result.text
def json_rpc_client_download(file_name):
    # 提取服务器返回的json数据
    result = requests.post(
        download_url, json={
            'download_file': file_name}).json()
    # print(result)
    # 提取key值
    result_keys = list(result.keys())[0]
    # 判断key值
    if 'download_file' == result_keys:
        # 提取value内容
        result_list = result.get('download_file')
        # 提取图片内容base64解密还原二进制数据
        result_file = base64.b64decode(result_list[1])
        # 将图片内容写入文件
        with open(download_file_dir + result_list[0], 'wb') as f:
            f.write(result_file)
            f.close()
        print(result_list[0] + ' 下载成功！')
        # return result_list[0] + ' 下载成功！'
    # 如果服务器返回不是key不是'download_file'返回错误信息
    else:
        print(result.get('error'))
        # return result.get('error')


#     pass
# rpc_client_exec_cmd=requests.get(exec_cmd_url)
# json_rpc_client_exec_cmd = (requests.get(exec_cmd_url))
# json_rpc_client_upload = (requests.post(upload_url)).json()
# json_rpc_client_download = (requests.get(download_url)).json()

# filename={'upload': open(upload_file_dir+filename,'rb')}
# r = requests.get(upload_url+'/'+filename,headers=input_header(file))

# r = requests.get('http://192.168.19.3:8080/upload')
# r = requests.get('http://192.168.19.3:8080/upload',headers=input_header(file))
# pprint(input_header(file),indent=4)
# print(r.request.headers)

# def json_rpc_client_upload(filename):
#     # print(upload_file_dir + filename)
#     # print(upload_url)
#     filename={'upload': open(upload_file_dir+filename,'rb')}
#     values = {'upload_file': 'file.txt', 'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
#     # 建立并保持会话
#     client = requests.session()
#     # 获取登录页面的内容
#     rpf = client.get(upload_url).content
#     # soup = BeautifulSoup(rpf, 'lxml')
#     # print(upload_url)
#     r = requests.get('http://192.168.19.3:8080/upload',headers=input_header(file))
#     # print(r.headers)
#     # print(r.json())
#     # print ((r.request.headers).json())
#     # return requests.post(upload_url, files=filename, data=values,headers=input_header(file))
#     rp = requests.post(upload_url, files=filename, data=values)
#     # return r.cookies.keys()
#     # return soup
#     pprint (rpf)

    # return requests.post(upload_url,files=files,data=values)
    # imageFile = open('qyt_logo.jpg', 'wb')
    # imageFile.write(imgContent)
    # imageFile.close()
# def json_rpc_client_download(filename):
#     # print(download_url + '/' + filename)
#     r = requests.get(download_url+'/'+filename,headers=input_header(file))
#
#     # filename = {'download': open(download_file_dir + filename, 'rb')}
#     imgContent = r.content
#     if imgContent:
#         # 下载并保存图片
#         imageFile = open(download_file_dir + filename, 'wb')
#         imageFile.write(imgContent)
#         imageFile.close()
#         print(filename+'下载成功')
#     else:
#         print('download file not exist')


if __name__ == '__main__':
    # exec_cmd = {'cmd':'ifconfig'}
    # print(json_rpc_client_exec_cmd(exec_cmd))
    # exec_cmd = {'cmd':'pwd1'}
    # print(json_rpc_client_exec_cmd(exec_cmd))
    # exec_cmd = {'cmd1': 'pwd'}
    # print(json_rpc_client_exec_cmd(exec_cmd))
    # print(json_rpc_client_upload('logo.png'))
    json_rpc_client_download('logo.png')
    json_rpc_client_download('logo1.png')
