#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

from ssh import device_ssh
import re
import hashlib
import time


def get_config(ip, username='admin', password='Cisco123'):
    try:
        conf = device_ssh(ip, username, password, cmd='show run | be hostname ')
        # 获取路由器配置

        return conf
    except Exception:

        return


def check_diff(ip, username='admin', password='cisco123'):
    conf1 = get_config(ip, username, password)
    m = hashlib.md5()
    m.update(str(conf1).encode())
    before_md5 = m.hexdigest()
    while True:

        conf2= get_config(ip, username, password)
        n = hashlib.md5()
        n.update(str(conf2).encode())
        now_md5 = n.hexdigest()
        if before_md5 == now_md5:
            print(n.hexdigest())
        else:
            print(n.hexdigest())
            print('MD5 value changed')
            break
    time.sleep(5)

if __name__ == '__main__':
    # print(get_config('192.168.19.201', 'cisco', 'cisco123'))
    # print(get_config('192.168.19.202', 'cisco', 'cisco123'))
    print(get_config('192.168.19.203', 'cisco', 'cisco123'))
    # check_diff('192.168.90.201', 'cisco', 'cisco123')
