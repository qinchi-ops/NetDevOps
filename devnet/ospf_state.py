#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
event manager applet interface_shutdown
 event syslog pattern "Interface .*, changed state to administratively down"
 action 1.0 regexp "\s+[A-Za-z]+[0-9]+," "$_syslog_msg" ifname
 action 2.0 syslog msg "eem try to no shutdown interface $ifname"
 action 3.0 cli command "en"
 action 4.0 cli command "guestshell run python3 /home/guestshell/no_shut_if.py $ifname"
"""
from cli import configure
import sys

configure('interface GigabitEthernet1 '  + '\nno shutdown')
configure('interface GigabitEthernet1 '  + '\nno shutdown')

