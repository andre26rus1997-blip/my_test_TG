import  telebot
from telebot import types
import requests
import json
bot = telebot.TeleBot("8300321950:AAGARJW5aN-9R4q0zA9B5JeLlbeL-pT0cd8")
API = ("9d25c51fa1e0dfe91110828f36f71afb")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет введите пожалуйста любой город ")


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    bot.reply_to(message,f"weahers is now: {res.json()}")
    




bot.polling(none_stop=True)