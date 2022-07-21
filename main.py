import telebot
from telebot import types
from weather import get_city_weather, get_city_weather_screen

bot = telebot.TeleBot('5570945317:AAGuWxuIMrPSTcZi22uk1eeoMV7rauA09zg')


@bot.message_handler(commands=['start', 'help', 'Start', 'Help'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>. ' \
           f'' + "Please enter the city name."
    bot.send_message(message.chat.id, mess, parse_mode='html')

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Kyiv', 'Lviv', 'Odesa', 'Kharkiv', 'Pirnove']
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, f"Or chose the city in the bot's menu.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def get_weather_from_text(message):
    city = message.text
    get_city_weather_screen(city)
    pict = open('screenshot.png', 'rb')
    bot.send_photo(message.chat.id, pict)
    w = get_city_weather(city)
    bot.send_message(message.chat.id, w)


bot.infinity_polling()
