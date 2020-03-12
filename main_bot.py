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
    print(message.text)
    #print(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    pass
    #print(call)


    # try:
    #     eval(to_menu+'(chat_id,to_menu)')
    #     answers=append(answer)
    #     print(answers)
    # except: # эксепт вылазит когда введена неожидаемая строка
    #     print("exept")
    #     #eval(now_menu+'(message)') # отправляется то меню, в котором находился человек последний раз
    #     pass

 # Обработчик для документов и аудиофайлов
# @bot.message_handler(content_types=['photo'])
# def handle_photo(message):
#     print("get photo")
#     file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
#     list_of_dir=os.listdir('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/')
#
#     if str(message.from_user.id) not in list_of_dir:
#         print("no exist")
#         os.mkdir('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/'+str(message.from_user.id))
#         src='/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/'+str(message.from_user.id)+'/'+get_datetime()+'.jpg'
#         with open(src, 'wb') as new_file:
#            new_file.write(downloaded_file)
#         photos_list.append(src.replace('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/',''))
#     else:
#         print("exist")
#         src='/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/'+str(message.from_user.id)+'/'+get_datetime()+'.jpg'
#         print(src)
#         with open(src, 'wb') as new_file:
#            new_file.write(downloaded_file)
#         photos_list.append(src.replace('/home/tester-vmn/projects/inventBotPilot/operface/main_oper_face/static/photos_instal/',''))
#
#     print(photos_list)
#     bot.send_message(message.chat.id, "фото сохранено")




# @bot.message_handler(content_types=['location'])
# def handle_loc(message):
#     print("location")
#     payload = str(message.location.longitude) + ',' + str(message.location.latitude)
#     url = 'https://geocode-maps.yandex.ru/1.x/?apikey=7b6e026e-a615-4157-a55c-9c7e9b90fa1a&format=json&geocode=' + payload
#     r = requests.get(url)
#     data = r.json()
#     second=data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
#     send = bot.send_message(message.chat.id, second)
#     location.append(second)


bot.polling(none_stop=True, interval=1)
