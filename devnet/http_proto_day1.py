#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from django.shortcuts import render
import json
from random import randint
import datetime
import time


def data_from_django(request):
    return render(request, 'data_from_django.html', {'chart1_label': 'CPU利用率',
                                         # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                         'chart1_time': json.dumps(['2018-8-1',
                                                                    '2018-8-2',
                                                                    '2018-8-3',
                                                                    '2018-8-4',
                                                                    '2018-8-5',
                                                                    '2018-8-6']),
                                         # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                         'chart1_data': json.dumps([randint(0, 100),
                                                                    randint(0, 100),
                                                                    randint(0, 100),
                                                                    randint(0, 100),
                                                                    randint(0, 100),
                                                                    randint(0, 100)]),
                                         # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                         'chart1_color': json.dumps(['#007bff'])})


def data_from_ajax(request):
    return render(request, 'data_from_ajax.html')


# 产生随机数据
times_list = []
router1_cpu = []
router2_cpu = []
for i in range(50):
    times_list.append((datetime.datetime.now() + datetime.timedelta(minutes=i)).strftime('%Y-%m-%d %M:%S'))
    router1_cpu.append(randint(20, 60))
    router2_cpu.append(randint(30, 70))
    i += 1

# 产生数据, 可以添加多个设备的线形图信息
routers_cpu = [
    {'name': 'R1',  # 线的名字
     'symbolSize': 0,  # 这个参数表示在图像上显示的原点大小，为0则不显示,
     'data': router1_cpu,  # 利用率的列表
     # markPoint用于标记最大值和最小值
     'markPoint': {
                    'itemStyle': {
                      'color': '#00BFFF'
                    },
                    'data': [
                        {'type': 'max', 'name': '最大值'},
                        {'type': 'min', 'name': '最小值'}
                    ]
                },
     # 平滑线
     'smooth': True,
     # 线形图
     # 'type': 'line',
     # 柱状图
     'type': 'bar',
     # 线的颜色
     'color': '#00BFFF'},
    {'name': 'R2',
     # 'symbolSize': 0,  # 这个参数表示在图像上显示的原点大小，为0则不显示,
     'data': router2_cpu,
     'markPoint': {
         'itemStyle': {
             'color': '#FF3300'
         },
         'data': [
             {'type': 'max', 'name': '最大值'},
             {'type': 'min', 'name': '最小值'}
         ]
     },
     'smooth': True,
     'type': 'line',
     'color': '#FF3300'}
]


def echarts_from_django(request):
    return render(request, 'echarts_from_django.html', {'chart1_label': 'CPU利用率',
                                                        # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                                        # 图标的列表
                                                        'chart1_legends': json.dumps([x['name'] for x in routers_cpu]),
                                                        # X轴时间的列表
                                                        'chart1_time': json.dumps(times_list),
                                                        # 多个设备(多线)的数据
                                                        'chart1_data': json.dumps(routers_cpu),

                                                        'pie1_label': '报名方向分布',
                                                        # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                                        'pie1_directions': json.dumps(['教主VIP', 'Python强化']),
                                                        # 必须使用json转换为字符串!因为要把它嵌入JS!并不会被For循环
                                                        'pie1_data': json.dumps([{'value': 60, 'name': '教主VIP'},
                                                                                 {'value': 30, 'name': 'Python强化'}])})


def echarts_final_line(request):
    return render(request, 'echarts_final_line.html')



if __name__ == '__main__':
    data_from_django(1)
