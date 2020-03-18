from flask import *
import telebot
from keyboards import *

token="1128488996:AAHIwMHnJoq85VhgUMncZ9295HNmhTNPNH0"
app = Flask(__name__)
bot = telebot.TeleBot(token)

@app.route("/"+token, methods=['POST'])
def bot_handler():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("=========================================")
    return 'NOT WORD'

@app.route("/", methods=['GET'])
def get_response():
    return flask.render_template('index.html')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handler(message):
    main_menu(message)

def main_menu(message):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.row("К работе готов", "Заявку принял")
    key.row("Убыл на заявку", "Прибыл на заявку")
    key.row("Выполнил заявку", "Прибыл в СП")
    send = bot.send_message(message.chat.id, "Соощение Диспетчера", reply_markup=key)
