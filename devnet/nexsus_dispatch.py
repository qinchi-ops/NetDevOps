#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cisco.interface import *
from nxos import *

lo0 = Interface("loopback0")

if lo0.show().admin_state == 'down':
    lo0.set_state(s='up')
    py_syslog(3, "Interface state is down,try to no shutdown!")
else:
    py_syslog(3, "Interface state is up!")
