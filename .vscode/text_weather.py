import telebot
import requests

bot = telebot.TeleBot("8300321950:AAGARJW5aN-9R4q0zA9B5JeLlbeL-pT0cd8")
API = "9d25c51fa1e0dfe91110828f36f71afb"

# --- убираем webhook, чтобы работал polling ---



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
