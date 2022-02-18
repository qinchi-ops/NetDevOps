#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging

import telegram
from telegram.ext import *
import responses
# from tele_requests import resp

# API_KEY = '1985713463:AAHiCm5wffTBJuqgPlyqBPESDFrNkDkvySU'

API_KEY = '1997245175:AAGHpGWEijVG3ewEeCOp6PTCy0jVUzDxdNk'

# chat_id = '547459503'
path_key = '/openvpn/keys/cnb/phcnb6001.ovpn'
path_tutorial = '/openvpn/tutorial/vpninstallation.pdf'
# files = {'document':open(path_tutorial,'rb')}

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')




# def help_command(update, context):
#     update.message.reply_text('下载运行并提供远程数字号码\nhttps://anydesk.com/en')

# def assist_command(update, context):
#     # update.message.reply_text('downloading')
#     # return update.message(resp)
#     context.bot.sendDocument(update.effective_chat.id,document=open(path_tutorial,'rb'))

def start_command(update, context):
    update.message.reply_text('是VPN服务机器人，小P')


def help_command(update, context):
    update.message.reply_text('/vpn_download  下载VPN客户端  \n /vpn_tutorial vpn安装使用教程  \n /vpn_assist  远程协助，下载使用Anydesk  ')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)

def assist_command(update, context):
    update.message.reply_text('正在上传安装教程中，请稍后!!!')
    # return update.message(resp)
    context.bot.sendDocument(update.effective_chat.id,document=open(path_tutorial,'rb'))


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('vpn_tutorial', assist_command))
    dp.add_handler(CommandHandler('custom', custom_command))


    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()