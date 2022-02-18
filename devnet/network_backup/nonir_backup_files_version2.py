from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
import time
import os
import paramiko
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

)

# 过滤出fortigate
fortigates = nr.filter(
    type="fortigate",

)

# 过滤出防火墙
asas = nr.filter(
    type="firewall",

)


# 过滤出防火墙
h3c = nr.filter(
    type="h3c",

)

###################################      过滤出需要的设备   ###########################################################
# 模板目录
templates_path = '../../../../../../../../onedrive/Backup/project/python/devnet/templates/'

###################################      提取需要的配置   ###########################################################
# 执行show命令
# 路由器show ip inter brief
routers_show_result = routers.run(task=netmiko_send_command,
                                  name='Nornir执行Show命令',
                                  command_string="show run")



asas_show_result = asas.run(task=netmiko_send_command,
                               name='Nornir执行Show命令',
                               command_string="show run", enable=True)

h3c_show_result = h3c.run(task=netmiko_send_command,
                               name='Nornir执行display命令',
                               command_string="disp current", enable=True)

fortigates_show_result = fortigates.run(task=netmiko_send_command,
                                  name='Nornir执行Show命令',
                                  command_string="show full-configuration ")


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


def h3c_config():

    for host in h3c.inventory.hosts:
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




########################      将配置文件写入 file   ###########################################################


if __name__ == '__main__':
    router_config()
    asas_config()
    fortigates_config()









