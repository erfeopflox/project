import telebot
from telebot import types

bot = telebot.TeleBot("7304730422:AAHY-ls0PKRV9unxsHvFN9c9lvPXC8qD2To")

web_app_url = "t.me/freetokens_KT_bot/webapp"

text = "Это приложение - копия игры Hamster Kombat, сделанная за 100 минут!\n\nНажмите на кнопку снизу, что запустить его!"

button = types.InlineKeyboardButton('Запустить', url=web_app_url)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text=text, reply_markup=keyboard)

bot.polling()
