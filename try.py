from flask import Flask ,request
import telebot
import json
import requests
import datetime as d
import transliterate
from keyboards import *

token=""
app = Flask(__name__)

bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handler(message):
    print(message)
    #bot.send_message(message.chat.id,message.chat.id)


@app.route("/"+token, methods=['POST'])
def get_response():
    message = request.json
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Hello World!"
