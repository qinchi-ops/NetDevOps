from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result
import time
import os
import paramiko
import threading
import datetime
import traceback
import re
# vi nonir_backup_huawei.py
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

switchs = nr.filter(
    type="switch",
)

for host in switchs.inventory.hosts:
    print (host)
###################################      过滤出需要的设备   ###########################################################
# 模板目录
templates_path = './templates/'


###################################      提取需要的配置   ###########################################################
# 执行show命令
# 路由器show ip inter brief
routers_show_result = switchs.run(task=netmiko_send_command,
                                  name='Nornir执行Show命令',
                                  command_string="display current")

# print(routers_show_result['csr1'].result)



###################################      将配置文件写入 file   ###########################################################

log_path = '/network/log/net_backups'
log_dir = log_path + "/%i-%.2i-%i" % (now.year, now.month, now.day)


# Backup routers configuration

def switchs_config():
    for host in switchs.inventory.hosts:
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

if __name__ == '__main__':
    switchs_config()
