#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


#（1）利用循环语句和判断条件，分别输出列表中的字符和数字
l = [1,2,'my','name','is',4,'katty']
int_list= []
str_list= []
for x in l:
    if isinstance(x,int):
        int_list.append(x)
    else:
        str_list.append(x)
print('数字为: ' + str(int_list))
print('字符串为:' + str(str_list))

#（2）利用循环语句输出1-50中5的倍数，将其存放到一个列表里面
output_list = []
for k in range(1,50):
    if k%5==0:
        output_list.append(k)
print(output_list)

#（3）定义一个判断字符串长度是否大于10的函数
a = 'asjkdh'
b = 'asdk123'
c = 'akshdka'
def howlong(string):
    if len(string) > 10:
        print ('字符串长度为：' + str(len(string))+'  ========>' '长度大于10')
    elif len(string) < 10:
        print ('字符串长度为：' + str(len(string))+'  ========>' '长度小于10')
    else:
        print ('字符串长度为：' + str(len(string))+'  ========>' '长度等于10')


#（4）定义一个求阶乘的函数

def jiecheng(int_number):

    while True:
        int_number >> 0


#（5）利用列表生成式，生成1-5的阶乘

#（6）利用函数和列表生产式，标记一个列表，奇数标记为1，偶数标记为2，并且统计一下奇数和偶数的数量。例如：[1,4,2,4,2,9,5], 得到[1,2,2,2,2,1,1]



if __name__ == '__main__':
    pass

howlong(a)
howlong('ioasdo1q0o2easdlhasodhaoshd')
howlong('1234567890')