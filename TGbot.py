import telebot
from telebot import types
from keyboards import main_menu,my_help,info
from responses import simple_responses,responses
import requests


bot = telebot.TeleBot("8429683137:AAEhGBEH0AAIAxkCojS3aNDbfqMcGwmdHpA")
API = "9d25c51fa1e0dfe91110828f36f71afb"




@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, "Главное меню для тебя мой дорогой ❤️", reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "weather":
        bot.send_message(call.message.chat.id, "🌍 Напиши название города:")
        bot.register_next_step_handler(call.message, send_weather)
    # Если кнопка есть в словаре
    if call.data in responses:
        bot.send_message(call.message.chat.id, responses[call.data])

    # Если кнопка соответствует в меню
    elif call.data in menus:
        bot.send_message(
            call.message.chat.id, "Выберети кнопку👇", reply_markup=menus[call.data]()
        )
    elif call.data == "back" or call.data == "back_main":
        bot.send_message(
            call.message.chat.id, "🔙 Возврат в главное меню", reply_markup=main_menu()
        )
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass


def get_weather_emoji(description):
    description = description.lower()
    if "ясно" in description:
        return "☀️"
    elif "облачно" in description:
        return "☁️"
    elif "пасмурно" in description:
        return "☁️"
    elif "дождь" in description:
        return "🌧"
    elif "гроза" in description:
        return "⛈"
    elif "cнег" in description:
        return "❄️"
    elif "туман" in description:
        return "🌫"
    else:
        return "🌍"


def send_weather(message):
    city = message.text.lower().strip()
    try:
        res = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric&lang=ru"
        )
        if res.status_code == 200:
            data = res.json()

            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = round(data["main"]["pressure"] * 0.75006375541921)
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            bot.send_message(
                message.chat.id,
                f"🌍 Погода в {city.title()}:\n"
                f"🌡 Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"🔽 Давление:{pressure}мм рт. ст.\n"
                f"💨 Ветер:{wind} m/c\n"
                f"☁️ Состояние:{description.capitalize()}",
            )
        else:
            bot.send_message(
                message.chat.id, "⚠️ Город не найден, попробуй ещё раз.")
            bot.register_next_step_handler(message, send_weather)
    except:
        bot.send_message(
            message.chat.id, "Ошибка при получении данных. Попробуй позже."
        )


# Ответы на простые соообщения
@bot.message_handler(content_types=["text"])
def reply(message):
    name = message.from_user.first_name
    text = message.text.lower().strip()

    for keys, response in simple_responses.items():
        if text in keys:
            bot.reply_to(message, response.format(name=name))
            return

    # Пробуем получить погоду
    try:
        res = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={text}&appid={API}&units=metric&lang=ru"
        )
        if res.status_code == 200:
            data = res.json()
            city_name = data["name"]
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            bot.reply_to(message, f"🌍 Погода в {city_name}: {temp}°C, {desc}")
            return
    except:
        pass

    # Если ничего не подошло
    bot.reply_to(message, f"Я тебя не понял, {name} 😅")


bot.polling(none_stop=True)
