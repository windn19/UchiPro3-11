from pprint import pprint

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from settings import telegram_token

TOKEN = telegram_token

bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Получить погоду', request_location=True))
keyboard.add(KeyboardButton('О проекте'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    pprint(message.json)
    text = 'Отправь мне свое местоположение и я отправлю тебе погоду.'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(regexp='О проекте')
def send_about(message):
    pprint(message.json)
    text = 'Бот позволяет получить погоду в текущем местоположении!\n'
    text += 'Для получения погоды - отправь боту геопозицию.\n'
    text += 'Погода берется с сайта https://openweathermap.org.\n'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


bot.infinity_polling()
