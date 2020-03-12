import requests


data={"chat_id": 208428842,"reply_markup" : {"InlineKeyboardMarkup" : {"InlineKeyboardButton" : {"text" : "test",},},},"text" : "kek",}




url='https://api.telegram.org/bot1098656388:AAGuCIRD0Yw7fbbgVi8CeBp7FQovGxYTGzE/sendMessage'
r = requests.post(url, data)
res = r.text
print(res)
