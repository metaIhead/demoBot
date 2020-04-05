import smtplib as smtp
import os
from flask import *
import telebot
import interactionDB
import keyboards

token = os.getenv("TOKEN")
app = Flask(__name__)
bot = telebot.TeleBot(token)

handlers = {'Покурить \U0001F4A8': 'smoke','Поесть \U0001F374': 'eat','Выпить \U0001F378': 'drink','None':'new'}
admins = {'208428842': 'admin'}


@app.route("/"+token, methods=['POST'])
def bot_handler():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 'NOT WORD'

@bot.message_handler(commands=['start'])
def start_message(message):
    main_menu(message)


def email(user_id, table, message):

    info=interactionDB.get_new_order(user_id,"smoke")
    stol=info[0][1]
    strong=info[0][2]
    vkus=info[0][3]
    chai=info[0][4]
    h=info[0][6]
    name=str(message.from_user.first_name)+" "+str(message.from_user.last_name)

    data="Новый заказ! \n\n№ столика: "+str(stol)+"\nХочет: "+str(h)+" \nВкус: "+str(vkus)+"\nКрепость: "+str(strong)+"\nИмя: "+str(name)

    # data="Новый заказ! \n № столика "+info[0]+"\n Хочет \n Вкус"
    send = bot.send_message(208428842,data)
    send = bot.send_message(456383857,data)

def smoke(message):
    table="smoke"
    user_id=message.chat.id

    parametr = {'blank': 'table_num','table_num': 'strong','strong': 'taste','taste': 'tea'}
    for_order = {'table_num': 'handler','strong': 'table_num','taste': 'strong','tea': 'taste'}
    greeting = {'table_num': 'выберите номер столика','strong': 'выберите крепость','taste': 'выберите вкус, либо напишите свой вариант:','tea':'Хотите чаю?'}

    if message.text == "Да" or  message.text == "Нет":
        interactionDB.write_parametr_to_table(user_id, "tea", message.text,table)
        email(user_id, table,message)
        interactionDB.clear_table_smoke(user_id)
        interactionDB.clear_table_customers(user_id)
        main_menu(message)
    else:
        intent = interactionDB.read_intent_from_table(user_id,table)[0][0]
        if intent is None:
            intent='blank'
        interactionDB.write_parametr_to_table(user_id, for_order[parametr[intent]], message.text,table)
        interactionDB.write_parametr_to_table(user_id, "intent", parametr[intent],table)
        send = bot.send_message(user_id, greeting[parametr[intent]], reply_markup=keyboards.smoke_keys[parametr[intent]])



def eat(message):
    send = bot.send_message(message.chat.id, "Тут ещё идёт ремонт")
    interactionDB.clear_table_customers(message.chat.id)

def drink(message):
    send = bot.send_message(message.chat.id, "Раздел на ремонте")
    interactionDB.clear_table_customers(message.chat.id)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def main_handler(message):
    user_id=message.chat.id
    admins[user_id]
    # try:
    #     admins[user_id]
    # except:
    interactionDB.load_new_customer(user_id)
    handler = interactionDB.read_from_customer_table(user_id)[0][0]
    if handler is None:
        handler=handlers[message.text]
        interactionDB.write_to_customers_table(user_id, handler)
    exec(handler+"(message)")

def main_menu(message):
    keyboard= '{ "keyboard": [ [{"text": "Покурить \U0001F4A8"}], [{ "text": "Поесть \U0001F374"}], [{ "text": "Выпить \U0001F378"}] ] }'
    send = bot.send_message(message.chat.id, "Что хотите...", reply_markup=keyboard)
