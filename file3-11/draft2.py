from pprint import pprint

import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from settings import telegram_token, api_token

TOKEN = telegram_token
API_KEY = api_token
URL_WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'

bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Получить погоду', request_location=True))
keyboard.add(KeyboardButton('О проекте'))


def get_weather(lat, lon):
    params = {'lat': lat,
              'lon': lon,
              'lang': 'ru',
              'units': 'metric',
              'appid': API_KEY}
    response = requests.get(url=URL_WEATHER_API, params=params).json()
    print(response)


@bot.message_handler(content_types=['location'])
def send_weather(message):
    pprint(message.json)
    lon = message.location.longitude
    lat = message.location.latitude
    result = get_weather(lat, lon)
    if result:
        bot.send_message(message.chat.id, result, reply_markup=keyboard)


bot.infinity_polling()
