#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import pg8000

#连接数据库
conn = pg8000.connect(host ='192.168.19.9', user = 'pythonpsql',password = 'pythonpsql',database = 'pythondb')

#执行数据库操作
cursor = conn.cursor()
cursor.execute("create table test1(t1 int, t2 varchar(40))")
cursor.execute("insert into test1(t1,t2) values (11, 'welcome to python')")
cursor.execute("insert into test1(t1,t2) values (12, 'welcome hello world')")
cursor.execute("select * from test1")

yourresults = cursor.fetchall()

for i in yourresults:
	print(i)


cursor.execute("drop table test1")
conn.commit()
