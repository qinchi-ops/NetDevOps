#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

from pymongo import *
from datetime import datetime
client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
db = client['python']

# for obj in db.secie.find():
#
# 	print(obj)
# tina = {'name': 'tina', 'department': 'sales', 'age': '35', 'location': 'Beijing'}
#
# # 写入单条数据
# db.secie.insert_one(tina)
#
# # 查看并打印所有数据
# for obj in db.secie.find():
# 	print(obj)

####写入时间#####
#
# config = {'config':'test', 'record_time':datetime.now()}
# db.secie.insert_one(config)
# 查看并打印所有数据
# for obj in db.secie.find():
# 	print(obj)
# # config 键存在，时间倒序
# # -1 是倒序，1是正序
# for obj in db.secie.find({'config':{"$exists":True}}).sort('record_time',1):
# 	print(obj)
#
# # 基于时间的过滤
#
# start = datetime(2021, 8, 4, 2, 16, 1, 334000)
# end = datetime(2021, 8, 4, 2, 18, 50, 957000)
#
# for obj in db.secie.find({'config': {"$exists": True}, 'record_time': {'$gte': start, '$lt': end}}):
# 	print(obj)
#
# #######写入二进制文件######
# from bson import binary
#
# file_insert = {'filename':'result1.png','binfile':Binary.Binary(open('result1.png','rb').read())}
# db.secie.insert_one(file_insert)
#
# for obj in db.secie.find({'filename':{"$exists":True}}):
# 	print(obj)

#
#
# employees = [{'a':'b'},{'c':'d'},{'e':'f'}]
#
# # #逐个单条写入
# # for employee in employees:
# # 	db.secie.insert_one(employee)
#
# #一次性写入多个（写一个列表）
# db.secie.insert_many(employees)
#
# #查看并打印所有数据
# for obj in db.secie.find():
#
# 	print(obj)

####查找单条数据####

print(db.secie.find_one({'name': 'tina'}))
# 只匹配第一个
print(db.secie.find_one({'age': {'$gt': 34}}))

# 查找多条数据#####

for x in db.secie.find({'location': 'Beijing'}):
	print(x)

#########查找多条数据(多条件 and 关系)
##默认and关系
# for x in db.secie.find({'age': {'$gt': 34}, 'location': 'Beijing'}):
# 	print(x)
#
# #########查找多条数据(多条件 or 关系)
#
# for x in db.secie.find({'$or': [{'age': {'$gt': 34}, 'location': 'Beijing'}]}):
# 	print(x)
#
# ######查找多条数据（正序与倒序）
#
# ###ASCENDING 和 DESCENDING可以用1和-1 代替
# for x in db.secie.find({'$or': [{'age': {'$gt': 34}, 'location': 'Beijing'}]}).sort('age', ASCENDING):
# 	print(x)

# for x in db.secie.find({'$or': [{'age': {'$gt': 34}, 'location': 'Beijing'}]}).sort('age', DESCENDING):
# 	print(x)
#####更新数据#####

db.secie.update({'name':'collin'},{"$set":{'name':'qinke'}})
for obj in db.secie.find():
	print(obj)

####更新多条数据####
db.secie.update({'location':'Beijing'},{"$set":{'location':'BJ'}},multi=True)

for obj in db.secie.find():
	print(obj)


#####删除数据####
db.secie.remove({'location':'BJ'})
for obj in db.secie.find():
	print(obj)

#####删除全部数据####
# db.secie.remove()