from nornir import InitNornir
# pip3 install nornir-netmiko
# pip3 install nornir-jinja2
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from vault.python_script.vault_1_init import client
import time
import os
import paramiko
import threading
import datetime
import traceback
import re

"""
This a an Network device backup script.  Support  Cisco , Fortinet ,Huawei . And if you have new device just modify the 

platform which called device_type in netmiko module.

"""
# get current time
now = datetime.datetime.now()

log_path = '/network/log'

# 加载配置文件config.yaml
nr = InitNornir(
    config_file="config.yaml",
    # dry_run=True
)

###################################      过滤出需要的设备   ###########################################################
#过滤出路由器

routers = nr.filter(
    type="router",
    # site='beijing'
)

# 过滤出fortigate
fortigates = nr.filter(
    type="fortigate",
    # site='beijing'
)

# 过滤出防火墙
asas = nr.filter(
    type="firewall",
    # site='beijing'
)

###################################      过滤出需要的设备   ###########################################################
# 模板目录
templates_path = './templates/'


###################################      从vault提取设备用户名密码并加入到设备yaml   ##########################################
# 从vault读取信息,并更新nornir inventory

for host in routers.inventory.hosts:
    print (host)
for host in routers.inventory.hosts.keys():
    # 从vault读取用户名和密码
    vault_data = client.secrets.kv.v2.read_secret_version(
                    mount_point='netlab',
                    path=f'{nr.inventory.hosts[host].platform}/cred'
                    )
    cred_data = vault_data['data']['data']
    # 更新nornir inventory对应host的用户名和密码
    nr.inventory.hosts[host].username = cred_data.get('username')
    nr.inventory.hosts[host].password = cred_data.get('password')

for host in fortigates.inventory.hosts.keys():
    # 从vault读取用户名和密码
    vault_data = client.secrets.kv.v2.read_secret_version(
                    mount_point='netlab',
                    path=f'{nr.inventory.hosts[host].platform}/auth'
                    )
    cred_data = vault_data['data']['data']
    # 更新nornir inventory对应host的用户名和密码
    nr.inventory.hosts[host].username = cred_data.get('username')
    nr.inventory.hosts[host].password = cred_data.get('password')


for host in asas.inventory.hosts.keys():
    # 从vault读取用户名,密码和secret密码
    vault_data = client.secrets.kv.v2.read_secret_version(
        mount_point='netlab',
        path=f'{nr.inventory.hosts[host].platform}/secret'
    )
    cred_data = vault_data['data']['data']
    # 更新nornir inventory对应host的用户名,密码和secret密码
    nr.inventory.hosts[host].username = cred_data.get('username')
    nr.inventory.hosts[host].password = cred_data.get('password')
    nr.inventory.hosts[host].connection_options['netmiko'].extras['secret'] = cred_data.get('secret')

    # print(cred_data.get('secret'))
###################################      从vault提取设备用户名密码并加入到设备yaml   ##########################################



###################################      提取需要的配置   ###########################################################
# 执行show命令
# 路由器show ip inter brief
routers_show_result = routers.run(task=netmiko_send_command,
                                  name='Nornir执行Show命令',
                                  command_string="show run")

# print(routers_show_result['csr1'].result)

asas_show_result = asas.run(task=netmiko_send_command,
                               name='Nornir执行Show命令',
                               command_string="show run", enable=True)


fortigates_show_result = fortigates.run(task=netmiko_send_command,
                                  name='Nornir执行Show命令',
                                  command_string="show full-configuration ")


# print('='*50 + 'start' + '='*50)
# print('-'*50 + '路由器配置' + '-'*50)
# print_result(routers_show_result)
# print('-'*50 + 'start' + '-'*50)
# print_result(asas_show_result)
# print('-'*50 + 'start' + '-'*50)
# print_result(fortigates_show_result)
# print('='*50 + 'Ending' + '='*50)
###################################      提取需要的配置   ###########################################################





###################################      将配置文件写入 file   ###########################################################

log_path = '/network/log/net_backups'
log_dir = log_path + "/%i-%.2i-%i" % (now.year, now.month, now.day)





# Backup routers configuration

def router_config():

    for host in routers.inventory.hosts:
        filename = log_dir + "/%s:%i-%.2i-%.2i-%.2i:%.2i:%.2i.log" % (host, now.year, now.month, now.day,
                                                                  now.hour, now.minute, now.second)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            with open(filename, "w") as fp:
                    for line in routers_show_result[host].result:
                        fp.write(line)
        elif os.path.exists(log_dir):
            with open(filename, "w") as fp:
                for line in routers_show_result[host].result:
                    # print(type(line))
                    fp.write(line)

# Backup ASA configuration
def asas_config():

    for host in asas.inventory.hosts:
        filename = log_dir + "/%s:%i-%.2i-%.2i-%.2i:%.2i:%.2i.log" % (host, now.year, now.month, now.day,
                                                                  now.hour, now.minute, now.second)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            with open(filename, "w") as fp:
                    for line in asas_show_result[host].result:
                        fp.write(line)
        elif os.path.exists(log_dir):
            with open(filename, "w") as fp:
                for line in asas_show_result[host].result:
                    fp.write(line)

# Backup fortigate configuration
def fortigates_config():
    for host in fortigates.inventory.hosts:
        filename = log_dir + "/%s:%i-%.2i-%.2i-%.2i:%.2i:%.2i.log" % (host, now.year, now.month, now.day,
                                                                  now.hour, now.minute, now.second)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
            with open(filename, "w") as fp:
                    for line in fortigates_show_result[host].result:
                        fp.write(line)
        elif os.path.exists(log_dir):
            with open(filename, "w") as fp:
                for line in fortigates_show_result[host].result:
                    fp.write(line)


# print(netmiko_show_result['mct-fg'].result)
# print(netmiko_show_result['csr2'].result)
# 打印返回结果
# for i in netmiko_show_result:
#     print('-'*50 + 'start' + '-'*50)
#     print(i)
#     print(type(i))
#     print('='*50 + i + '='*50)
#     print(type(netmiko_show_result[i].result))
#     print(netmiko_show_result[i].result)
#     print('-' * 50 + 'end' + '-' * 50)


########################      将配置文件写入 file   ###########################################################


if __name__ == '__main__':
    router_config()
    asas_config()
    fortigates_config()









