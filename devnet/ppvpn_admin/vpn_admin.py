#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#功能一，发送秘钥    （后面计划用inline实现精细分类，减少命令行）
#功能二，获取对应服务器的 接口流量状态  done , 需
#功能三, 开通新账户
#功能四，查询在线状态
#功能五，要添加一个安全限制功能，这个是管理员bot，不能让其他人使用

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from get_status import get_openvpn_status,get_interface_traffic,can3,hknode,cannode
from functools import wraps


def is_known_username(username):
    '''
    Returns a boolean if the username is known in the user-list.
    '''
    known_usernames = ['ge789', 'username2']

    return username in known_usernames


def private_access():
    """
    Restrict access to the command to users allowed by the is_known_username function.
    """
    def deco_restrict(f):

        @wraps(f)
        def f_restrict(message, *args, **kwargs):
            username = message.from_user.username

            if is_known_username(username):
                return f(message, *args, **kwargs)
            else:
                bot.reply_to(message, text='Who are you?  Keep on walking...')

        return f_restrict  # true decorator

    return deco_restrict
#ppvpn_admin_API_KEY
TOKEN = '1931022880:AAFKaiPhz89mbp_d84Vq0XKs8Db28XmulfE'
bot = telebot.TeleBot(TOKEN)

# chat_id = '730252290'

@bot.message_handler(commands=['start'])
@private_access()
def send_welcome(message):
    bot.reply_to(message, '我是VPN管理员，请慎重操作!!!')

@bot.message_handler(commands=['key', '秘钥'])
@private_access()
def send_key(message):
    bot.reply_to(message, '/phcnb -  下载 phcnb全部秘钥 \n /phcni -  下载 phcni全部秘钥 \n /phcnf -  下载 phcnf全部秘钥 \n '
                          '/phhkd -  下载 phhkd全部秘钥 ')

@bot.message_handler(commands=['vpn', 'vpn 下载', 'vpn_download'])
@private_access()
def send_vpn_client(message):
    bot.reply_to(message, 'VPN客户端下载地址:\nhttps://openvpn.net/client-connect-vpn-for-windows/')


####################################################VPN 状态获取#########################################################
@bot.message_handler(commands=['vpn_status'])
@private_access()
def send_help(message):
    bot.reply_to(message,  '/hknode_status -  查看hk节点openvpn连接情况 \n /cannode_status -  下查看can节点openvpn连接情况 \n '
                           '/can3_status -  查看can3节点openvpn连接情况')


@bot.message_handler(commands=['hknode_status'])
@private_access()
def send_help(message):
    bot.reply_to(message, '获取VPN连接信息中，请稍等 >>> loading......')
    bot.reply_to(message, get_openvpn_status(hknode))

@bot.message_handler(commands=['cannode_status'])
@private_access()
def send_help(message):
    bot.reply_to(message, '获取VPN连接信息中，请稍等 >>> loading......')
    bot.reply_to(message, get_openvpn_status(cannode))

@bot.message_handler(commands=['can3_status'])
@private_access()
def send_help(message):
    bot.reply_to(message, '获取VPN连接信息中，请稍等 >>> loading......')
    bot.reply_to(message, get_openvpn_status(can3))

####################################################VPN 状态获取#########################################################

##########################################    VPN  服务器接口流量#########################################################

@bot.message_handler(commands=['vpn_traffic'])
@private_access()
def send_help(message):
    bot.reply_to(message,  '/hknode_traffic -  查看hk节点流量带宽情况 \n /cannode_traffic -  下查看can节点流量带宽情况 \n '
                           '/can3_traffic -  查看can3节点流量带宽情况')


@bot.message_handler(commands=['hknode_traffic'])
@private_access()
def send_help(message):
    bot.reply_to(message, '获取服务器接口流量数据中>>>>>>>>>>>！')
    bot.reply_to(message, get_interface_traffic(hknode))

@bot.message_handler(commands=['cannode_traffic'])
@private_access()
def send_help(message):
    bot.reply_to(message, '获取服务器接口流量数据中>>>>>>>>>>>')
    bot.reply_to(message, get_interface_traffic(cannode))

@bot.message_handler(commands=['can3_traffic'])
@private_access()
def send_help(message):
    bot.reply_to(message, '获取服务器接口流量数据中>>>>>>>>>>>')
    bot.reply_to(message, get_interface_traffic(can3))


##########################################    VPN  服务器接口流量#########################################################


@bot.message_handler(commands=['install', '教程'])
def send_tutorial(message):
    bot.reply_to(message, '安装教程正在上传中，请稍等！！！')
    path_tutorial = '/openvpn/tutorial/vpninstallation.pdf'
    document = open(path_tutorial, 'rb')
    bot.send_document(message.chat.id,document)


###########################################         传递密钥         ###################################################
@bot.message_handler(commands=['phcnb'])
@private_access()
def send_keys(message):
    bot.reply_to(message, '正在传递秘钥中，请稍等！！！')
    key_path = '/openvpn/keys/cnb/'
    keys_phcnb6001 = open('/openvpn/keys/cnb/phcnb6001.ovpn', 'rb')
    keys_phcnb6002 = open('/openvpn/keys/cnb/phcnb6002.ovpn', 'rb')
    #
    key_name = ['phcnb6001.ovpn','phcnb6002.ovpn','phcnb6003.ovpn','phcnb6004.ovpn','phcnb6005.ovpn','phcnb6006.ovpn',
                'phcnb007.ovpn','phcnb2001.ovpn','phcnb2002.ovpn']
    try:
        for key in key_name:
            keys = open('/openvpn/keys/cnb/' + key, 'rb')
            bot.send_document(message.chat.id,keys)
    except:
        pass

@bot.message_handler(commands=['phcni'])
@private_access()
def send_keys(message):
    bot.reply_to(message, '正在传递秘钥中，请稍等！！！')

    key_name = ['phcni1.ovpn','phcni2.ovpn','phcni3.ovpn']
    try:
        for key in key_name:
            keys = open('/openvpn/keys/cni/' + key, 'rb')
            bot.send_document(message.chat.id,keys)
    except:
        pass

@bot.message_handler(commands=['phhkg'])
@private_access()
def send_keys(message):
    bot.reply_to(message, '正在传递秘钥中，请稍等！！！')

    key_name = ['phhkg002.ovpn','phhkg003.ovpn']
    try:
        for key in key_name:
            keys = open('/openvpn/keys/hkg/' + key, 'rb')
            bot.send_document(message.chat.id,keys)
    except:
        pass

@bot.message_handler(commands=['phhkd'])
@private_access()
def send_keys(message):
    bot.reply_to(message, '正在传递秘钥中，请稍等！！！')

    key_name = ['phhkd001.ovpn','phhkd002.ovpn','phhkd003.ovpn','phhkd004.ovpn','phcnd003.ovpn']
    try:
        for key in key_name:
            keys = open('/openvpn/keys/hkd/' + key, 'rb')
            bot.send_document(message.chat.id,keys)
    except:
        pass

@bot.message_handler(commands=['phcnf'])
@private_access()
def send_keys(message):
    bot.reply_to(message, '正在传递秘钥中，请稍等！！！')

    key_name = ['phcnf001.ovpn','phcnf002.ovpn','phcnf003.ovpn','phcnf004.ovpn','phcnf005.ovpn','phcnf006.ovpn',
                'phhkf001.ovpn','phhkf002.ovpn','phhkf003.ovpn','phhkf004.ovpn']
    try:
        for key in key_name:
            keys = open('/openvpn/keys/cnf/' + key, 'rb')
            bot.send_document(message.chat.id,keys)
    except:
        pass

###########################################         传递密钥         ###################################################


# def gen_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("phcnb", callback_data="cb_yes"),
#                                InlineKeyboardButton("phcnf", callback_data="cb_no"))
#     return markup
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "cb_yes":
#         # bot.reply_to(call, '安装教程正在上传中，请稍等！！！')
#         # path_tutorial = '/openvpn/tutorial/vpninstallation.pdf'
#         # document = open(path_tutorial, 'rb')
#         # bot.send_document(call.id, document)
#         bot.answer_callback_query(call.id, "Answer is Yes")
#     elif call.data == "cb_no":
#         bot.answer_callback_query(call.id, "Answer is No")
#
# @bot.message_handler(commands=['phcnb'])
# # @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#     bot.send_message(message.chat.id, "请选择需要下载的秘钥:", reply_markup=gen_markup())

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.polling()