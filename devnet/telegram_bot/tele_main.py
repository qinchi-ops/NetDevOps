#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)

    app.send_message(chat_dest, msg)

@app.route('/help ?(.*)')
def help_command(message, cmd):
    chat_dest = message['chat']['id']
    sent_msg = '下载并提供Andyesk远程数字号码:\nhttps://anydesk.com/en'
    app.send_message(chat_dest, sent_msg)


@app.route('/tutorial ?(.*)')
def assist_command(message, context):
    path_key = '/openvpn/keys/cnb/phcnb6001.ovpn'
    path_tutorial = '/openvpn/tutorial/vpninstallation.pdf'
    document = open(path_tutorial, 'rb')
    chat_dest = message['chat']['id']
    app.send_message(chat_dest, '正在上传安装教程中，请稍后!!!')

    # context.bot.sendDocument(update.effective_chat.id,document=open(path_tutorial,'rb'))

@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   user_msg = message['text']

   msg = "Parrot Says: {}".format(user_msg)
   app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = '1997245175:AAGHpGWEijVG3ewEeCOp6PTCy0jVUzDxdNk'
    app.poll(debug=True)