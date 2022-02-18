#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
import datetime
a = datetime.datetime(2021, 8, 4, 5, 19, 47, 984000)
b = a.strftime('%H:%M:%S')
# b = a.strftime('%y-%m-%d  %H:%M:%S')
time_record_list = [datetime.datetime(2021, 8, 4, 5, 19, 47, 984000),datetime.datetime(2021, 8, 4, 5, 20, 47, 984000),datetime.datetime(2021, 8, 4, 5, 21, 47, 984000)]
time_record_list = [i.strftime('%H:%M:%S') for i in time_record_list]
date_list = []
# strftime('%y-%m-%d %a %H:%M:%S')
# for time in time_record_list:
#     date_list.append(time.date())
#     print(time.date())
#     print(date_list)

# print(b)
print(time_record_list)