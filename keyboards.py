import telebot


bot = telebot.TeleBot("")

def inline(message):
    print("IN")
    inlineKey = telebot.types.InlineKeyboardMarkup()
    callback_button = telebot.types.InlineKeyboardButton(text="Принять заявку", callback_data="accept")
    inlineKey.add(callback_button)
    print("=======================================")
    print(inlineKey)
    print("=======================================")

    bot.send_message(message.chat.id,'Улица Пушкина', reply_markup=inlineKey)

def main_menu(message):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.row("К работе готов", "Заявку принял")
    key.row("Убыл на заявку", "Прибыл на заявку")
    key.row("Выполнил заявку", "Прибыл в СП")
    #key.add(telebot.types.KeyboardButton('отправить местоположение', ))
    send = bot.send_message(message.chat.id, "Соощение Диспетчера", reply_markup=key)
