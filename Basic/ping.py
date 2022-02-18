#!/usr/bin/python3.8
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import logging
#  关闭不必要的报错
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *
from kamene.layers.inet import ICMP, IP


def device_ping(ip):
    # 构建ping数据包
    ping_pkt = IP(dst=ip)/ICMP()
    # Ping并且把返回结果赋值给ping_result
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result :
        # 设计返回值
        #return (ip+' 通!')
        return '!'
    else:
        return '.'

if __name__ == '__main__':
    result = device_ping('1.1.1.1')
    result2 = device_ping('192.168.32.129')
    # 根据返回值涉设计打印
    print(result)
    print(result2)