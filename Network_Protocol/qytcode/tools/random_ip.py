#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import random


def random_section():
    section = random.randint(1, 254)
    return section


def random_ip():
    ip = str(random_section()) + '.' + str(random_section()) + '.' + str(random_section()) + '.' + str(random_section())
    return ip


if __name__ == '__main__':
    print(random_ip())
