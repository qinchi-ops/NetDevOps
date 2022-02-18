#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

conn = sqlite3.connect('router_backup.sqlite')
cursor = conn.cursor()
cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5 varchar(999))")

