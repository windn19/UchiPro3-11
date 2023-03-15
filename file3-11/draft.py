import telebot, ... # импорты библиотек
TOKEN, API_KEY, URL_WEATHER_API = '...' # константы
EMOJI_CODE = {200: '⛈', ...}  # словарь с emoji
bot = telebot.TeleBot(TOKEN)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # добавление клавиатуры

def get_weather(lat, lon):
    """Запрос к API и возврат строки с ответом."""
    ...

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Приветственное сообщение."""
    return ...

@bot.message_handler(content_types=['location'])
def send_weather(message):
    """Извлечение координат и отправка ответа."""
    lon, lat = message.location.longitude, message.location.latitude
    ... = get_weather(lon, lat)
    bot.send_message(...)

@bot.message_handler(regexp='О проекте')
def send_about(message):
    """Сообщение о проекте."""
    ...

bot.infinity_polling()
