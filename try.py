from flask import *
import telebot


token = os.getenv("TOKEN")
app = Flask(__name__)
bot = telebot.TeleBot(token)

@app.route("/"+token, methods=['POST'])
def bot_handler():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("=========================================")
    return 'NOT WORD'

@app.route("/", methods=['GET'])
def get_response():
    return render_template('index.html')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def main_handler(message):
    main_menu(message)
    user_id=message.chat.id
    text=message.text
    interactionDB.insert_fitter(user_id)
    interactionDB.set_status(user_id, text)

def main_menu(message):
    keyboard= '{ "keyboard": [ [{"text": "К работе готов"}], [{ "text": "Заявку принял"}], [{ "text": "Убыл на заявку"}], [{ "text": "Прибыл на заявку"}],[{ "text": "Выполнил заявку"}], [{ "text": "Прибыл в СП"}] ]}'
    send = bot.send_message(message.chat.id, "Выберите статус", reply_markup=keyboard)
