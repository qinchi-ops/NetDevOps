#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from ldap3 import Server, ALL

ad_admin_username = 'administrator'
ad_admin_password = 'Cisc0123'

server = Server('ldaps://10.1.1.200', get_info=ALL, use_ssl=True)


if __name__ == '__main__':
    pass
