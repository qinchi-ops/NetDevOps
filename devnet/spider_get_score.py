#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
import requests
import re
from readheader import readheaders
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = requests.session()
# 获取个人作业URL
url = 'https://qytsystem.qytang.com/python_enhance/python_enhance_homework'


# 格式化打印BeautifulSoup对象
# print(taobao_soup.prettify())
def get_score():
    qyt_home = client.get(url, headers=readheaders('http_header.txt'))
    # lxml HTML 解析器

    qyt_soup = BeautifulSoup(qyt_home.text, 'lxml')
    # print(qyt_soup.a.attrs)
    # print(qyt_soup.a.text)
    # print(qyt_soup.a['href'])
    # print(qyt_soup.find_all('a'))
    # print(qyt_soup.find_all('img'))
    # print(len(qyt_soup.find_all('img')))

    # for a in qyt_soup.find_all('a'):
    #     print(a.get('href'))

    # print(qyt_soup.find_all(re.compile("a|p|div")))
    #
    # for div in qyt_soup.find_all('div'):
    #     print(div)
    # for score in qyt_soup.find_all('tbody', class_="text - center"):
    # score_list=[]
    # print(qyt_soup.find_all('tbody'))
    course_list = []
    score_list = []
    for score in qyt_soup.find_all('tbody'):
        for x in score.find_all('tr'):
            y = x.text.strip().split('\n')
            course_list.append(y[1])
            score_list.append(y[-1])
    # print(course_list)
    # print(score_list)
    cout_A = score_list.count('A')
    cout_Aa = score_list.count('A-')
    cout_B = score_list.count('B')
    cout_Bb = score_list.count('B-')
    cout_C = score_list.count('C')
    course_score_count = [cout_A,cout_Aa,cout_B,cout_Bb,cout_C]
    course_score_list = ['A','A-','B','B-','C']


    pythonbasic_count = course_list.count('Python基础')
    pythonprotocol_count = course_list.count('经典自动化协议')
    pythondjg_count = course_list.count('Django')
    pythonhttp_count = course_list.count('DevNet')

    course_homework_count = [pythonbasic_count,pythonprotocol_count,pythondjg_count,pythonhttp_count]
    course_homework_list = ['Python基础','经典自动化协议','Django','DevNet']
    print('='*80)
    print(course_score_count)
    print(course_score_list)
    print('='*80)
    print(course_homework_count)
    print(course_homework_list)
    print('=' * 80)


    return course_score_count,course_score_list,course_homework_count,course_homework_list

def course_score_pie():

    course_score_list=(get_score())[1]
    course_score_count = (get_score())[0]
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(course_score_count, labels=course_score_list, autopct='%1.1f%%',
            startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
    plt.title('课程分数分布图')
    plt.legend(loc='upper right')
    plt.show()

def course_homework_pie():
    course_homework_count=np.array((get_score())[2])
    course_homework_list =(get_score())[3]
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(course_homework_count, labels=course_homework_list, autopct='%1.1f%%',
            startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文
    # plt.pie(course_homework_count, labels=course_homework_list)
    plt.title('课程作业分布图')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':

    course_score_pie()
    course_homework_pie()
    # print((get_score())[0])
    # print((get_score())[1])
    # print((get_score())[2])
    # print((get_score())[3])

