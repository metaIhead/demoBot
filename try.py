from flask import *
import telebot
import os
import interactionDB


token = os.getenv("TOKEN")
app = Flask(__name__)
bot = telebot.TeleBot(token)

@app.route("/send_message", methods=['POST'])
def send_handler():
    request_data=request.json
    bot.send_message(request_data['id'], "Статус принят, "+request_data['text'])
    return 'NOT WORD'

@app.route("/", methods=['GET'])
def get_response():
    return render_template('table.html',load={'info_status': interactionDB.read_all_users() })

@bot.message_handler(func=lambda message: True, content_types=['text'])
def main_handler(message):
    main_menu(message)
    user_id=message.chat.id
    text=message.text
    name=str(message.from_user.first_name)+" "+str(message.from_user.last_name)

    interactionDB.insert_fitter(user_id, name)
    interactionDB.set_status(user_id, text)

def main_menu(message):
    keyboard= '{ "keyboard": [ [{"text": "К работе готов"}], [{ "text": "Заявку принял"}], [{ "text": "Убыл на заявку"}], [{ "text": "Прибыл на заявку"}],[{ "text": "Выполнил заявку"}], [{ "text": "Прибыл в СП"}] ]}'
    send = bot.send_message(message.chat.id, "Выберите статус", reply_markup=keyboard)
