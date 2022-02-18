#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import re       #import regular expression
import os       #import linux os command
import paramiko # import paramiko module
import pprint

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def device_ssh(ip, username, password, port=22, cmd='cmd ') :
    # 登录到设备，并返回执行结构,使用RSA_key 登录
    ssh.connect(ip,port=22,username=username,password=password,timeout=30,compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x
# def ssh_get_route(ip,username):
#     # 执行并返回命令"route -n"的结果
#     route_n_result = os.popen("route -n").read()
#     # gateway [2] 的IP为网关，匹配
#     gateway = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', route_n_result)[1]
#     return gateway

if __name__ == '__main__':
    # print(centos_ssh('192.168.64.129', 'root','python',cmd='ls'))
    # print(centos_ssh('192.168.64.129', 'root','python',cmd='pwd'))
    # print(device_ssh('192.168.50.83', 'cisco', 'cisco123', cmd='show run | be hostname '))
    # print(device_ssh('192.168.50.83', 'cisco', 'cisco123', cmd='dir '))
    # print(device_ssh('192.168.19.254','netdxs','8MmQksKJiTz', cmd='display current-configuration '))
    #print(    re.findall('(GigabitEthernet\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',centos_ssh('192.168.32.133', 'cisco', 'cisco123', cmd='show ip int bri')))
    #pprint.pprint(    re.findall('(GigabitEthernet\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',device_ssh('192.168.32.133', 'cisco', 'cisco123', cmd='show ip int bri')))
#     print('网关为：')
#     print(ssh_get_route('192.168.64.129', 'centos'))