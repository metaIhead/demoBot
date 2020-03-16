from flask import Flask ,request
import telebot
import json
import requests
import datetime as d
import transliterate
from keyboards import *

def handler(message):
    print(message.chat.id)
    print("______")
    bot.send_message(message.chat.id,message.chat.id)
    main_menu(message)


token="1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0"
app = Flask(__name__)

bot = telebot.TeleBot(token)

def handler(message):
    print(len(message))
    bot.send_message(message.chat.id,message.chat.id)
    main_menu(message)

@app.route("/"+token, methods=['POST'])
def get_response():
    message = request.json
    handler(message)
    return "Hello World!"
