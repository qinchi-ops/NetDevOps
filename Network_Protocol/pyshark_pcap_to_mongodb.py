import pyshark
import pprint
from pymongo import *


def write_info_to_db(dict_info):
    client = MongoClient('mongodb://python:python@192.168.19.10:27017/python')
    db = client['python']
    db.pcap_info_test9.insert_one(dict_info)

    # for obj in db.pcap_info.find():
    #     print(obj)


# ####################传一个函数,对pkt进行处理#####################
cap = pyshark.FileCapture('test.pcapng', keep_packets=False)  # 读取pcap文件,数据包被读取后,不在内存中保存!节约内存!

pkt_list = []


def write_all_layer(pkt):
    pkt_dict = {}
    new_pkt_dict = {}
    for layer in pkt.__dict__.get('layers'):
        # 把Pyshark能decode的每一层的所有字段, 并入(update)pkt_dict中
        pkt_dict.update(layer.__dict__.get('_all_fields'))
    # 为了写入mongoDB，需要将键的'.'，替换为'_'
    for key in pkt_dict.keys():
        new_pkt_dict.update({'{0}'.format(key.replace('.', '_')): pkt_dict[key]})
    pprint.pprint(new_pkt_dict, indent=4)

    write_info_to_db(new_pkt_dict)


if __name__ == '__main__':
    # 把函数应用到数据包
    cap.apply_on_packets(write_all_layer)
