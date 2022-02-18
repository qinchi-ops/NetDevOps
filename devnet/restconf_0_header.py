#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

client = requests.session()

username = "admin"
password = "Cisc0123"

csr1_ip = "192.168.1.1"
csr2_ip = "192.168.1.2"

headers = {'Accept': 'application/yang-data+json', 'Content-Type': 'application/yang-data+json'}

