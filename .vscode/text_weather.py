import telebot
import requests

bot = telebot.TeleBot("8443100317:AAFRkXbC7ms2RN9C0RwG2eoJ-z6fRVRxcG4")
API = "9d25c51fa1e0dfe91110828f36f71afb"





@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Введите, пожалуйста, любой город 🌍")

@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric"
    )
    if res.status_code == 200:
        data = res.json()
        temp = data["main"]["temp"]
        bot.reply_to(message, f"В городе {city.title()} сейчас {temp}°C 🌡️")
    else:
        bot.reply_to(message, "❌ Город не найден, попробуй ещё раз.")

bot.polling(none_stop=True)
