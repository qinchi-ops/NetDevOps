#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from pymongo import *
import numpy as np
from Mongo_get_interface import  db
from datetime import datetime, timedelta
from dateutil import parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import matplotlib.ticker as mtick
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'

def search_info_from_mongodb(ifname, direction, last_mins):
    client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
    db = client['python']
    if_bytes_list = []
    record_time_list = []

    for obj in db.deviceinfo.find({'record_time': {'$gte': datetime.now() - timedelta(minutes=last_mins)}}):
        if_bytes_list.append(obj[ifname + '_' + direction + '_bytes'])
        record_time_list.append(obj['record_time'])

    # numpy 的diff计算列表的差值
    # np.diff([x for x in range(5)])
    # array ([1,1,1,1])
    # 通过这种方式获取两次获取的字节数的差值
    diff_if_bytes_list = list(np.diff(if_bytes_list))

    # 计算两次事件对象的秒数的差值，np的多态牛逼
    diff_record_time_list = [x.seconds for x in np.diff(record_time_list)]

    # 计算速率
    # * 8 得到bit数
    # /1000 计算kb
    # / x[1]计算kbps
    # round(x,2)保留两位小数
    # zip把字节差列表 和时间列表压到一起

    # print(list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list))))
    # return list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list)))
    speed_list = list(
        map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list)))
    record_time_list = record_time_list[1:]
    # print((record_time_list,speed_list))
    # print()
    return (record_time_list, speed_list)

def rate_show(ifname, direction, last_mins):
    # 连接数据库
    results = search_info_from_mongodb(ifname, direction, last_mins)
    # print(results)
    time_record_list=results[0]

    int_rate_list = results[1]

    # # 把结果写入time_list和cpu_list的列表
    # for int_rate,time_record in results:
    #     time_record_list.append(results[0])
    #     int_rate_list.append(results[1])

    print(int_rate_list)
    print(time_record_list)
    #
    # # 转换字符串到时间对象
    # time_record_list = [i.strftime('%H:%M:%S') for i in time_record_list]
    # print(time_record_list)
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 添加主题和注释
    plt.title('Interface inbound Rate')
    plt.xlabel('Record Time')
    plt.ylabel('Interface Rate Kbps')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 格式化X轴
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S"))  # 设置时间标签显示格式
    # 格式化Y轴
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))#格式化Y轴
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))  # 格式化Y轴
    # 传入数据,time为X轴,cpu为Y轴
    ax.plot(time_record_list, int_rate_list, linestyle='solid', color='r', label='interface rate')
    # 设置Y轴 最小值 和 最大值
    ax.set_ylim(bottom=0, top=20)

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 显示图像
    plt.show()

if __name__ == '__main__':
     rate_show('GigabitEthernet1','out',1)

