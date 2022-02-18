#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
from matplotlib import pyplot as plt
from pymongo import *
import re

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
color_list = ['r', 'b', 'g', 'y']


# ---------------------------pie------------------------------------------
def mat_pie_src(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(7, 7))

    # 将某部分爆炸出来，使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = (0.01, 0.01, 0.01, 0.01)

    patches, label_text, percent_text = plt.pie(size_list,
                                                # explode=explode,
                                                labels=name_list,
                                                labeldistance=1.1,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)

    # 改变文本的大小,方法是把每一个text遍历。调用set_size方法设置它的属性
    for l in label_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20

    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


def get_ip_src_count():
    client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
    db = client['python']

    count_dict = {}
    src_ip = []
    ip_count = []

    for obj in db.pcap_info_test9.find():
        try:
            # 如果count_dict中没有原IP地址，添加键，并且初始化个数为1
            if obj['ip_src'] not in count_dict.keys():
                count_dict.update({obj['ip_src']: 1})
            # 如果已经存在了键，则将值加一
            else:
                count_dict[obj['ip_src']] += 1
        except Exception:
            pass

    # 按照降序进行排序
    order_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    # 保留最大的五个值
    if len(order_list) > 5:
        order_list = order_list[0:5]

    # 返回IP和数量的列表
    for ip, count in order_list:
        src_ip.append(ip)
        ip_count.append(count)
    return ip_count, src_ip


# --------------------------------------column1---------------------------------------
def mat_column_stream(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(12, 10))

    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=color_list)

    # 竖向柱状图
    plt.bar(name_list, size_list, width=0.5, color=color_list)

    # 旋转标签
    plt.xticks(rotation=15)

    # 添加主题和注释
    plt.title('Packets information')
    plt.xlabel('Source Destination PORT')
    plt.ylabel('pkt accounts')

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


def get_stream_count():
    client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
    db = client['python']

    count_dict = {}
    three_tripe_list = []
    stream_count_list = []

    for obj in db.pcap_info_test9.find():
        try:
            # 如果是TCP协议
            if obj['ip_proto'] == '6':
                # 如果count_dict中没有三元组，添加键，并且初始化个数为1
                three_tripe_key = obj['ip_src'] + ' ' + obj['ip_dst'] + ' ' + obj['tcp_dstport']
                if three_tripe_key not in count_dict.keys():
                    count_dict.update({three_tripe_key: 1})
                # 如果已经存在了键，则将值加一
                else:
                    count_dict[three_tripe_key] += 1
        except Exception:
            pass

    # 按照降序进行排序
    order_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    # 保留最大的五个值
    if len(order_list) > 5:
        order_list = order_list[0:5]

    # 返回三元组和数量的列表
    for three_tripe, stream_count in order_list:
        three_tripe_list.append(three_tripe)
        stream_count_list.append(stream_count)
    return stream_count_list, three_tripe_list


# --------------------------------------column2---------------------------------------
# 记录协议编号和映射的字典
ip_protocol_dict = {'0': 'HOPOPT', '1': 'ICMP', '2': 'IGMP', '3': 'GGP', '6': 'TCP', '7': 'CBT', '8': 'EGP', '9': 'IGP','10': 'BBN-RCC-MON', '11': 'NVP-II', '12': 'PUP', '13': 'ARGUS', '14': 'EMCON', '15': 'XNET','16': 'CHAOS','17': 'UDP', '18': 'MUX', '19': 'DCN-MEAS', '20': 'HMP', '21': 'PRM', '22': 'XNS-IDP','23': 'TRUNK-1','24': 'TRUNK-2', '25': 'LEAF-1', '26': 'LEAF-2', '27': 'RDP', '28': 'IRTP', '29': 'ISO-TP4','30': 'NETBLT','31': 'MFE-NSP', '32': 'MERIT-INP', '33': 'DCCP', '34': '3PC', '35': 'IDPR', '36': 'XTP','37': 'DDP','38': 'IDPR-CMTP', '41': 'IPv6', '42': 'SDRP', '43': 'IPv6-Route', '44': 'IPv6-Frag', '45': 'IDRP','46': 'RSVP','47': 'GRE', '48': 'MHRP', '49': 'BNA', '50': 'ESP', '52': 'I-NLSP', '53': 'SWIPE','54': 'NARP / NHRP[1',
'55': 'MOBILE', '56': 'TLSP', '57': 'SKIP', '58': 'IPv6-ICMP', '59': 'IPv6-NoNxt','60': 'IPv6-Opts','64': 'SAT-EXPAK', '65': 'KRYPTOLAN', '66': 'RVD', '67': 'IPPC', '70': 'VISA', '71': 'IPCV','72': 'CPNX','73': 'CPHB', '74': 'WSN', '75': 'PVP', '76': 'BR-SAT-MON', '77': 'SUN-ND', '78': 'WB-MON','79': 'WB-EXPAK','80': 'ISO-IP', '81': 'VMTP', '82': 'SECURE-VMTP', '83': 'VINES', '84': 'TTP', '85': 'NSFNET-IGP','86': 'DGP','87': 'TCF', '88': 'IGRP', '89': 'OSPF', '90': 'Sprite-RPC', '91': 'LARP', '92': 'MTP','93': 'AX.25','94': 'IPIP', '95': 'MICP', '96': 'SCC-SP', '97': 'ETHERIP', '98': 'ENCAP', '101': 'IFMP','102': 'PNNI','103': 'PIM', '104': 'ARIS', '105': 'SCPS', '106': 'QNX', '107': 'A/N', '108': 'IPComp','109': 'SNP','110': 'Compaq-Peer', '111': 'IPX-in-IP', '112': 'VRRP', '115': 'L2TP', '116': 'DDX', '117': 'IATP','118': 'STP','119': 'SRP', '120': 'UTI', '121': 'SMP', '123': 'PTP', '124': 'ISIS over IPv4', '125': 'FIRE','126': 'CRTP','127': 'CRUDP', '128': 'SSCOPMCE', '129': 'IPLT', '130': 'SPS', '131': 'PIPE', '132': 'SCTP','134': 'RSVP-E2E-IGNORE', '135': 'Mobility Header', '136': 'UDPLite', '137': 'MPLS-in-IP'}


def mat_column_protocal_coun(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(8, 6))

    # 横向柱状图
    plt.barh(name_list, size_list, height=0.5, color=color_list)

    # 竖向柱状图
    # plt.bar(name_list, size_list, width=0.5, color=color_list)

    # 旋转标签
    # plt.xticks(rotation=15)

    # 添加主题和注释
    plt.title('IP protocol statistics')
    plt.xlabel('Pkt accounts')
    plt.ylabel('Protocols')

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


def get_protocol_count():
    client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
    db = client['python']

    count_dict = {}
    ip_protocol_list = []
    pkt_count_list = []

    for obj in db.pcap_info_test9.find():
        try:
            # 如果count_dict中没有三元组，添加键，并且初始化个数为1
            find_key = ip_protocol_dict[obj['ip_proto']]
            if find_key not in count_dict.keys():
                count_dict.update({find_key: 1})
            # 如果已经存在了键，则将值加一
            else:
                count_dict[find_key] += 1
        except Exception:
            pass

    # 按照降序进行排序
    order_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    # 保留最大的五个值
    if len(order_list) > 5:
        order_list = order_list[0:5]

    # 返回协议和数量的列表
    for protocol_name, count in order_list:
        ip_protocol_list.append(protocol_name)
        pkt_count_list.append(count)
    return pkt_count_list, ip_protocol_list


if __name__ == '__main__':
    # 得到源IP地址分布的饼图
    size_list, name_list = get_ip_src_count()
    mat_pie_src(size_list, name_list)

    # 得到TCP同一三元组包数量分布的柱状图
    size_list, name_list = get_stream_count()
    mat_column_stream(size_list, name_list)

    # 得到协议分布的柱状图
    size_list, name_list = get_protocol_count()
    mat_column_protocal_coun(size_list, name_list)
