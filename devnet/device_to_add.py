#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import urllib3
from bs4 import BeautifulSoup
from readheader import readheaders

device_to_add = [{'name':'PythontestAddDevice1',
                      'ip':'4.3.2.1',
                    'description': 'pythontest',
                      'snmp_ro_community':'qytangro',
                      'snmp_rw_community':'qytangrw',
                      'ssh_username':'sshusername',
                      'ssh_password':'sshpassword',
                      'enable_password':'CIsco0123',
                      'type':'4'},
                     {'name': 'PythontestAddDevice2',
                      'ip': '4.3.2.2',
                        'description': 'pythontest',
                      'snmp_ro_community': 'qytangro',
                      'snmp_rw_community': 'qytangrw',
                      'ssh_username': 'sshusername',
                      'ssh_password': 'sshpassword',
                      'enable_password': 'CIsco0123',
                      'type': '4'}

                                    ]

devices_info = [{'name': 'pythonAddDevice1',
                 'ip': '192.168.0.99',
                 'description': '乾颐堂网络实验室',
                 'snmp_ro_community': 'tcpipro',
                 'snmp_rw_community': 'tcpiprw',
                 'ssh_username': 'prin',
                 'ssh_password': 'Cisc0123',
                 'enable_password': 'cisco',
                 'type': '4'
                 },
                {'name': 'pythonAddDevice2',
                 'ip': '192.168.0.100',
                 'description': '乾颐堂网络实验室',
                 'snmp_ro_community': 'tcpipro',
                 'snmp_rw_community': 'tcpiprw',
                 'ssh_username': 'prin',
                 'ssh_password': 'Cisc0123',
                 'enable_password': 'cisco',
                 'type': '4'
                 }]
device_to_adds = [{'name': 'pythondd1',
                   'ip': '5.3.2.1',
                   'description': '无敌的我',
                   'snmp_ro_community': 'tcpipro',
                   'snmp_rw_community': 'tcpiprw',
                   'ssh_username': 'wssd1',
                   'ssh_password': 'wssa123456',
                   'enable_password': 'admin',
                   'type': '4'},
                 {'name': 'pythondd2',
                   'ip': '6.3.2.2',
                   'description': '有趣的你',
                   'snmp_ro_community': 'tcpipro',
                   'snmp_rw_community': 'tcpiprw',
                   'ssh_username': 'wssd2',
                   'ssh_password': 'wss128937',
                   'enable_password': 'admin',
                  'type': '4'}
                 ]

login_url ='http://djg.mingjiao.org/accounts/login/'
add_devices_url ='http://djg.mingjiao.org/add_device'
username = 'user1'
password = 'cisco123'

def get_login():
    client = requests.session()
    login_page = client.get(login_url).content
    soup = BeautifulSoup(login_page,'lxml')
    csrftoken = soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
    login_data = {'username': username, 'password': password, "csrfmiddlewaretoken": csrftoken}
    # POST提交数据到登录页面
    client.post(login_url, data=login_data, headers=readheaders('http_header.txt'))
    return client


def add_device(device_db):
        client =get_login()
        add_device_soup =BeautifulSoup(client.get(add_devices_url).content,'lxml')
        add_device_csrftoken=add_device_soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
        for device in device_db:
            device.update({"csrfmiddlewaretoken":add_device_csrftoken})
            r = client.post(add_devices_url,data=device)
            print(r.status_code)

if __name__ == '__main__':
    add_device(device_to_adds)


