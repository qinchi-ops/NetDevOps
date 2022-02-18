#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from pprint import pprint
from PIL import Image  # pip install Pillow
from io import BytesIO
header_keys = []
header_values = []


file = 'header.txt'

def input_header(file):
    f = open(file, 'r')
    headers_list = [x.split(':') for x in f]
    headers = {a[0]: a[1].strip() for a in headers_list}
    pprint(headers, indent=4)
    return headers

# {a[0]:a[1] for a in a_split} split转换dict方法

# def input_header(file):
#     f =  open(file,'r')
#    #print(f.readline())
#     for x in f:
#         y = x.split(':')
#         print(y)
#         # print(x.split(':')[0])
#         header_keys.append(x.split(':')[0])
#         header_values.append((x.split(':')[1]).strip())
#         # print(header_keys)
#         # print(header_values)
#         headers = dict(zip(header_keys,header_values))
        # pprint(headers,indent=4)
#     print(headers)
#     # pprint(headers, indent=4)
#     return headers
#
r = requests.get('http://djg.mingjiao.org/static/images/logo_long_new.png', headers=input_header(file))

imgContent = r.content

# 在PyCharm中展示图片
i = Image.open(BytesIO(r.content))
i.show()

# 下载并保存图片
imageFile = open('qyt_logo.jpg', 'wb')
imageFile.write(imgContent)
imageFile.close()

if __name__ == '__main__':
    pass
input_header(file)