#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
import datetime
from matplotlib import pyplot as plt
now = datetime.datetime.now()
now_m3=(datetime.datetime.now() - datetime.timedelta(hours=3))
now_m6=(datetime.datetime.now() - datetime.timedelta(hours=6))
now_m9=(datetime.datetime.now() - datetime.timedelta(hours=9))
now_m12=(datetime.datetime.now() - datetime.timedelta(hours=12))
now_a3 =(datetime.datetime.now() + datetime.timedelta(hours=3))
now_a6 =(datetime.datetime.now() + datetime.timedelta(hours=6))
now_a9 =(datetime.datetime.now() + datetime.timedelta(hours=9))
now_a12 =(datetime.datetime.now() + datetime.timedelta(hours=12))
# print(now)
#
# print(now_a3)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'


def mat_line(cpu_usage_list):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行, 每行一图, 第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    # ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S')) # 设置时间标签显示格式
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))  # 设置时间标签显示格式

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    # 把cpu_usage_list的数据,拆分为x轴的时间,与y轴的利用率
    x = []
    y = []

    for time, cpu in cpu_usage_list.items():
        x.append(time)
        y.append(cpu)
        # print(x)

    # 添加主题和注释
    plt.title('Route CPU Usage')
    plt.xlabel('Gather time')
    plt.ylabel('CPU utilize')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让他自适应

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果你有两套数据,完全可以在一幅图中绘制双线
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()

if __name__ == '__main__':
    cpu_usage_list= {
                        now_m12:random.randint(0,100),
                        now_m9: random.randint(0,100),
                        now_m6: random.randint(0,100),
                        now_m3: random.randint(0,100),
                        now:random.randint(0,100),
                        now_a3:random.randint(0,100),
                        now_a6:random.randint(0,100),
                        now_a9:random.randint(0,100),
                        now_a12:random.randint(0,100)
    }
    mat_line(cpu_usage_list)

