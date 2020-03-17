# -*- coding: utf-8 -*-
import json
import telebot
import requests
from keyboards import *


URL='https://api.telegram.org/bot/getUpdates'
r = requests.get(url = URL)
data = json.loads(r.text)
user_id=data['result'][0]['message']['from']['id']
text=data['result'][0]['message']['text']

# # URL='https://api.telegram.org/bot1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0/getUpdates'
# bot = telebot.TeleBot("1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0")
#
#
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    # print("______")
    # bot.send_message(message.chat.id,message.chat.id)
    # main_menu(message)
    #print(message)

bot.polling(none_stop=True)
