# https://nornir.readthedocs.io/en/latest/tutorial/inventory.html
# pip3 install nornir
from nornir import InitNornir
from nornir.core.inventory import Host
from pprint import pprint

nr = InitNornir(config_file="config.yaml")

# 要求的格式
print('-'*50 + '打印Host schema' + '-'*50)
pprint(Host.schema(), indent=4)

# {   'connection_options': {   '$connection_type': {   'extras': {   '$key': '$value'},
#                                                       'hostname': 'str',
#                                                       'password': 'str',
#                                                       'platform': 'str',
#                                                       'port': 'int',
#                                                       'username': 'str'}},
#     'data': {'$key': '$value'},
#     'groups': ['$group_name'],
#     'hostname': 'str',
#     'name': 'str',
#     'password': 'str',
#     'platform': 'str',
#     'port': 'int',
#     'username': 'str'}

# ---------------------上面的格式决定了hosts.yaml的数据格式-------------------------------
# asa1:
#     groups:
#         - cisco_asa
#     hostname: 192.168.1.3
#     connection_options: # enable密码部分需要提前准备
#         netmiko:
#             extras:
#                 secret:
#     data:
#         site: beijing
#         type: firewall
#         interface_list:
#             -   interface_name: GigabitEthernet0/0
#                 ipaddr: 202.100.1.254
#                 netmask: 255.255.255.0
#                 nameif: Outside
#                 security_lvl: 0
#             -   interface_name: GigabitEthernet0/1
#                 ipaddr: 10.1.1.254
#                 netmask: 255.255.255.0
#                 nameif: Inside
#                 security_lvl: 100

print('-'*50 + '打印Hosts' + '-'*50)
# 所有主机
pprint(nr.inventory.hosts)
# 特定主机
pprint(nr.inventory.hosts['csr1'])

print('-'*50 + '打印Groups' + '-'*50)
# 所有组
pprint(nr.inventory.groups)
# 特定组
pprint(nr.inventory.groups['cisco_ios'])

# csr1从group获取data
print('-'*50 + '打印csr1信息(从group得到信息)' + '-'*50)
csr1 = nr.inventory.hosts['csr1']
# 类型为 <class 'nornir.core.inventory.Host'>
print(type(csr1))
# 可以提取data下所有的key,注意是data下
print(csr1.keys())
# 提取键site下的值
print(csr1['site'])
# 提取键interface_list下的值
print(csr1['interface_list'])

# csr2从default获取data
print('-'*50 + '打印csr2信息(从default得到信息)' + '-'*50)
csr2 = nr.inventory.hosts['csr2']
# 类型为 <class 'nornir.core.inventory.Host'>
print(type(csr2))
# 可以提取data下所有的key,注意是data下
print(csr2.keys())
# 提取键site下的值
print(csr2['site'])

# 不同的过滤方案
print('-'*50 + '过滤方案一' + '-'*50)
# 站点为beijing的所有主机
print(nr.filter(site="beijing").inventory.hosts)

print('-'*50 + '过滤方案二' + '-'*50)
# 站点为beijing, 并且类型为router的所有主机
print(nr.filter(site="beijing", type="router").inventory.hosts)

print('-'*50 + '过滤方案三' + '-'*50)
# 站点为beijing, 并且类型为router的所有主机
print(nr.filter(site="beijing").filter(type="router").inventory.hosts)

print('-'*50 + '过滤方案四' + '-'*50)
# 站点为beijing, 并且类型为router的所有主机
filter1 = nr.filter(site="beijing")
filter2 = filter1.filter(type="router")
print(filter2.inventory.hosts)

# 找到组内的设备
print('-'*50 + '查找组内的设备' + '-'*50)
# 组cisco_ios下的所有主机
print(nr.inventory.children_of_group("cisco_ios"))

