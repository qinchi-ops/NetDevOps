#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from telegram.ext import *
from telebot import TeleBot
path_key = '/openvpn/keys/cnb/phcnb6001.ovpn'
phcnb = []
phcnf = []
phcni = []
phhkg = []
phhkd = []
yourresults = ['phcnb','phcna','phcnf','phhkd','phkg','phcni']

def keys_command(update, context):
    update.message.reply_text('正在快递发送秘钥中，请稍后!!!')
    user_notify = """
    
    请输入验证密码:
    输入0：退出
    """
    phcnb_notify = """
    
    请输入秘钥选项:
    输入1：phcnb6001
    输入2：phcnb6002
    输入3：phcnb6003
    输入4：phcnb6004
    输入0：退出
    
    """

    while True:
        print(user_notify)
        user_input = input('请输入验证密码:')
        if user_input == '0':
            break
        elif user_input == 'phcnb':
            print(phcnb_notify)
            user_input = input('请选择秘钥:')
            if user_input == '1':
                context.bot.sendDocument(update.effective_chat.id, document=open(path_key, 'rb'))

        # elif user_input == 'phcnf':
        #     user_sn = input('请输入验证密码:')
        #     if not user_sn:
        #         continue
        #     if user_sn not in yourresults:
        #         print('验证码不正确!')
        #     for teacher in yourresults:
        #         if teacher[0] == user_sn:
        #             print(f'学员姓名:{teacher[0]} 学员年龄:{teacher[1]} 学员作业数:{teacher[2]}')
        else:
            print('验证密码错误！请重试')



if __name__ == '__main__':
    pass
