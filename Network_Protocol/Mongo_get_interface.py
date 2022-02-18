#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

from pymongo import *
import numpy as np
import pprint
from datetime import datetime, timedelta
from snmpv2_getbulk import snmpv2_getbulk
from snmpv2_get import snmpv2_get

client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
db = client['python']

def get_all_info(ip,ro):
    # 接口名称
    if_name_list = [x[1] for x in snmpv2_getbulk(ip,ro,"1.3.6.1.2.1.2.2.1.2",count=25,port=161)]
    # 接口速速
    if_speed_list = [x[1] for x in snmpv2_getbulk(ip,ro,"1.3.6.1.2.1.2.2.1.5",count=25,port=161)]
    # 进接口字节数
    if_in_bytes_list = [x[1] for x in snmpv2_getbulk(ip,ro, "1.3.6.1.2.1.2.2.1.10", count=25, port=161)]
    # 出接口字节数
    if_out_bytes_list = [x[1] for x in snmpv2_getbulk(ip,ro, "1.3.6.1.2.1.2.2.1.16", count=25, port=161)]
    name_speed_in_out_list = zip(if_name_list, if_speed_list, if_in_bytes_list, if_out_bytes_list)
    all_info_dict = {}
    if_name_list = []
    for x in name_speed_in_out_list:
        if 'Ethernet' in x[0]:
            all_info_dict[x[0] + '_' + 'speed'] = x[1]
            all_info_dict[x[0] + '_' + 'in_bytes'] = int(x[2])
            all_info_dict[x[0] + '_' + 'out_bytes'] = int(x[3])
            if_name_list.append(x[0])


    all_info_dict.update({'if_name_list': if_name_list})

    # cpmCPUTotal5sec
    cpu_5s = int(snmpv2_get(ip, ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)[1])
    # cpmCPUMemoryUsed
    mem_u = int(snmpv2_get(ip, ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)[1])
    # cpmCPUMemoryFree
    mem_f = int(snmpv2_get(ip, ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)[1])

    all_info_dict['ip'] = ip
    all_info_dict['cpu_5s'] = cpu_5s
    all_info_dict['mem_u'] = mem_u
    all_info_dict['mem_f'] = mem_f
    all_info_dict['record_time'] = datetime.now()

    return all_info_dict


def write_info_to_mongodb(device_info_dict):
    # 写入单条数据
    db.deviceinfo.insert_one(device_info_dict)

    # 查看并打印secie中的所有数据
    for obj in db.deviceinfo.find():
        pprint.pprint(obj, indent=4)


# def search_info_from_mongodb(ifname, direction, last_mins):
#     if_bytes_list = []
#     record_time_list = []
#
#     for obj in db.deviceinfo.find({'record_time': {'$gte': datetime.now() - timedelta(minutes=last_mins)}}):
#         if_bytes_list.append(obj[ifname + '_' + direction + '_bytes'])
#         record_time_list.append(obj['record_time'])
#
#     # numpy 的diff计算列表的差值
#     # np.diff([x for x in range(5)])
#     # array ([1,1,1,1])
#     # 通过这种方式获取两次获取的字节数的差值
#     diff_if_bytes_list = list(np.diff(if_bytes_list))
#
#     # 计算两次事件对象的秒数的差值，np的多态牛逼
#     diff_record_time_list = [x.seconds for x in np.diff(record_time_list)]
#
#     # 计算速率
#     # * 8 得到bit数
#     # /1000 计算kb
#     # / x[1]计算kbps
#     # round(x,2)保留两位小数
#     # zip把字节差列表 和时间列表压到一起
#
#     # print(list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list))))
#     # return list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list)))
#     speed_list = list(
#         map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list)))
#     record_time_list = record_time_list[1:]
#     print(record_time_list,speed_list)
    # print()
    # return record_time_list, speed_list
# def delete_all():
#     db.deviceinfo.remove()

if __name__ == '__main__':
    write_info_to_mongodb(get_all_info('192.168.19.11','tcpippro'))
    # search_info_from_mongodb('GigabitEthernet1','out',1)

