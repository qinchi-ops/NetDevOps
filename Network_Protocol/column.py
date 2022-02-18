#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
plt.rcParams['font.family'] = 'sans-serif'
colorlist = ['r', 'b', 'g', 'y']


def mat_zhu(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))


    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=colorlist)

    # 竖向柱状图
    plt.bar(name_list, size_list, width=0.5, bottom=0,color=colorlist)


    # 添加主题和注释
    plt.title('Protocol with Bandwidth')  # 主题
    plt.xlabel('Bandwidth（M/s）')  # X轴注释
    plt.ylabel('Protocol')  # Y轴注释

    # x_values = [0,20,40,60]
    # plt.plot(x_values, size_list, linewidth=5)

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()

if __name__ == '__main__':
    size_list = ['30','20', '30','60']
    name_list = ['spotify','ssh', 'igmp','unknown']
    mat_zhu(size_list, name_list)
