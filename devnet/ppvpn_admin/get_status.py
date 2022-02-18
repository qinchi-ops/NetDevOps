#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from netmiko import ConnectHandler
can3 = {

    'host':'can-3',
    'device_type':'linux',
    'ip':'139.159.137.108',
    'username':'root',
    'password':'PNZAPKESv1TyMSoarTsU'
}

hknode = {

    'host':'hk-node',
    'device_type':'linux',
    'ip':'94.74.96.187',
    'username':'root',
    'password':'PNZAPKESv1TyMSoarTsU'
}

cannode = {

    'host':'can-node',
    'device_type':'linux',
    'ip':'139.159.150.119',
    'username':'root',
    'password':'PNZAPKESv1TyMSoarTsU'
}


# server = {
#
#     'host':'server',
#     'device_type':'linux',
#     'ip':'192.168.19.5',
#     'username':'centos',
#     'password':'centos'
# }
# net_connect = ConnectHandler(**my_fg)
# net_connect = ConnectHandler(**can_3)

# output = net_connect.send_command('ifconfig eth0')

# output = net_connect.send_command('cat /var/log/openvpn/status.log ')

# output = net_connect.send_command('python3 interface_traffic.py eth0  ')
#
# print(output)


def get_interface_traffic(host):
    net_connect = ConnectHandler(**host)
    traffic = net_connect.send_command('python3 interface_traffic.py eth0  ')

    return traffic

def get_openvpn_status(host):
    net_connect = ConnectHandler(**host)
    status = net_connect.send_command('cat /var/log/openvpn/status.log  ')

    return status


if __name__ == '__main__':
    print(get_openvpn_status(cannode))