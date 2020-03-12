# -*- coding: utf-8 -*-
import telebot
import json
import requests
import datetime as d
import transliterate
from keyboards import *


def  get_datetime():
    a = d.datetime.today().strftime("%Y%m%d")
    today = d.datetime.today()
    datetime=today.strftime("%Y-%m-%d-%H-%M-%S")
    return datetime


user_id=[]
chat_id=[]
photos=[]
location=[]
score=[]
start_answers=[]
final_answers=[]
photos_list=[]

bot = telebot.TeleBot("1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0")

#Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    print("start")
    # print("user id:",message.from_user)
    # print("chat id:",message.chat.id)
    #bot.send_message(message.chat.id,message.from_user.first_name)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print("______")
    print(message)
    print("______")
    print(message.chat)
    print("______")
    print(message.chat.id)
    print("______")
    #print(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    pass
    #print(call)

bot.polling(none_stop=True, interval=1)
