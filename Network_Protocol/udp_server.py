#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
import socket
import sys

address = ("0.0.0.0", 6666)
# 创建UDP套接字Socket, AF_INET为IPv4, SOCK_DGRAM为Datagram就是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 套接字绑定到地址,元组(host, port)
s.bind(address)

print('UDP服务器就绪！等待客户数据！')
while True:

    try:

    recv_source_data = s.recvform)2048

    ####
    ####
    ###

    if md5_recv == md5_value.encode():
        print('=' * 80)
    print("{0:<30}:{1:<30}".format("数据来自于", str(addr)))
    print("{0:<30}:{1:<30}".format("数据序号为", seq_id))
    print("{0:<30}:{1:<30}".format("数据长度为", length))
    print("{0:<30}:{1:<30}".format("数据内容为", str(pickle.loads(data))))

    except
    KeyboardInterrupt:
        sys.exit()
