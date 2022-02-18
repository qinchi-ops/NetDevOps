#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


import json
from socket import *
import os
import base64


def Server_JSON(ip, port):
    # 创建TCP Socket, (ip,port):
    sockobj = socket(AF_INET, SOCK_STREAM)
    # 绑定套字到地址，地址为(host,port)的元组
    sockobj.bind((ip, port))
    # 在拒绝连接前，操作系统可以挂起的最大连接数量，一般配置为5
    sockobj.listen(5)

    while True:  # 一直接受请求，直到ctrl+c终止程序
        try:
            # 接受TCP连接，并且返回(conn,address)的元组，conn为新的套字节对象，可以用来接收和发送数据，address是连接客户端的
            connection, address = sockobj.accept()
            # conn.settimeout(5.0)	#设置连接超时!
            # 打印连接客户端的IP地址
            print('Server Connected by', address)
            received_message = b''  # 预先定义接收信息变量
            received_message_fragment = connection.recv(1024)  # 读取接收到的信息，写入到接收到信息分a片
            if len(received_message_fragment) < 1024:  # 如果长度小于1024！表示客户发的数据小于1024！

                received_message = receoved_message_fragment
                obj = json.loads(received_message.decode())  # 把接收到信息jason.loads回到正常的obj

            else:
                while len(received_message_fragment) == 1024:  # 等于1024表示还有后续数据!
                    received_message = received_message + received_message_fragment  # 把接收到信息分片重组装
                    received_message_fragment = connection.recv(1024)  # 继续接收后续的1024的数据
                else:
                    received_message = received_message + received_message_fragment  # 如果数据小于1024！拼接到最后数据
                obj = jason.loads(received_message.decode())  # 把接收到信息json.loads回正常的obj

            if 'exec_cmd' in obj.keys():
            ####################

            elif 'upload_file' in obj.keys():

                # 应该考虑写入上传的 文件名！但是由于实验室相同目录测试！所以使用了'upload_file.py'
                ######
                ####
                print('上传文件{0}保存文件!'.format(obj.get('upload_file')))
                return_data = {'message': 'Upload Success!'}
            elif 'download_file' in obj.keys():
            ####
            ###
            ###
            connection.send(json.dumps(return_data).encode())
            connection.close()
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':

    # 使用Linux解释起& WIN 解释器
    Server_IP = '0.0.0.0'
    Server_port = 6666
    Server_JSON(Server_IP, Server_Port)