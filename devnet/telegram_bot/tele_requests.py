#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from telegram import *
chat_id = '547459503'
path_key = '/openvpn/keys'
path_tutorial = '/openvpn/tutorial/vpninstallation.pdf'
files = {'document':open(path_tutorial,'rb')}
# resp = requests.post('https://api.telegram.org/bot1997245175:AAGHpGWEijVG3ewEeCOp6PTCy0jVUzDxdNk/sendDocument?chat_id=-547459503',files=files)


#
# if __name__ == '__main__':
#     pass
# sendDocument(chat_id, document, filename = NULL, caption = NULL,
#   disable_notification = FALSE, reply_to_message_id = NULL,
#   reply_markup = NULL, parse_mode = NULL)
#
# bot <- Bot(token = bot_token("RTelegramBot"))
# chat_id <- user_id("Me")
# document_url <- paste0(
#   "https://github.com/ebeneditos/telegram.bot/raw/gh-pages/docs/",
#   "telegram.bot.pdf"
# )
#
# bot$sendDocument(
#   chat_id = chat_id,
#   document = document_url
# )