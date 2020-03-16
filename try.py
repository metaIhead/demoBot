from flask import Flask ,request
import telebot
import json
import requests
import datetime as d
import transliterate
from keyboards import *


token="1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0"
app = Flask(__name__)

@app.route("/"+token, methods=['POST'])
def get_response():
    response=request.json
    print(response)
    return "Hello World!",response


bot = telebot.TeleBot(token)
message=response
#Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    print("start")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):

    print(message.chat.id)
    print("______")
    bot.send_message(message.chat.id,message.chat.id)
    main_menu(message)
