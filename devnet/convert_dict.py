#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


dict_a = {   'ifconfig': 'ens192: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n'
                '        inet 192.168.19.3  netmask 255.255.255.0  broadcast '
                '192.168.19.255\n'
                '        inet6 fe80::20c:29ff:fee1:5bac  prefixlen 64  scopeid '
                '0x20<link>\n'
                '        ether 00:0c:29:e1:5b:ac  txqueuelen 1000  (Ethernet)\n'
                '        RX packets 550913  bytes 1010628469 (963.8 MiB)\n'
                '        RX errors 0  dropped 19  overruns 0  frame 0\n'
                '        TX packets 327901  bytes 78139560 (74.5 MiB)\n'
                '        TX errors 0  dropped 0 overruns 0  carrier 0  '
                'collisions 0\n'
                '\n'
                'lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536\n'
                '        inet 127.0.0.1  netmask 255.0.0.0\n'
                '        inet6 ::1  prefixlen 128  scopeid 0x10<host>\n'
                '        loop  txqueuelen 1000  (Local Loopback)\n'
                '        RX packets 2134  bytes 1584937 (1.5 MiB)\n'
                '        RX errors 0  dropped 0  overruns 0  frame 0\n'
                '        TX packets 2134  bytes 1584937 (1.5 MiB)\n'
                '        TX errors 0  dropped 0 overruns 0  carrier 0  '
                'collisions 0\n'
                '\n'}


# for x,y in dict_a.items():
#     print(y)
print (y for x,y in dict_a.items())