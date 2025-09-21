import telebot
from telebot import types
import requests

bot = telebot.TeleBot("8300321950:AAGARJW5aN-9R4q0zA9B5JeLlbeL-pT0cd8")
API = "9d25c51fa1e0dfe91110828f36f71afb"
bot.remove_webhook()

# Главное меню
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🤝Помощь✌️", callback_data="help")
    btn2 = types.InlineKeyboardButton("📝Информация📌", callback_data="info")
    btn3 = types.InlineKeyboardButton("🥳Посмейся немного🤣", callback_data="jok")
    btn4 = types.InlineKeyboardButton("⛅Погода🌧️", callback_data="weather")
    btn5 = types.InlineKeyboardButton("❌Удалить🗑️", callback_data="delete")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    return markup


# keyboard for help
def my_help():  #
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(
        "😍Как пользоваться мной😍", callback_data="How_used"
    )
    btn2 = types.InlineKeyboardButton("❤️Что я могу❤️", callback_data="ability")
    btn3 = types.InlineKeyboardButton(
        "😭Напиши мне свою проблему😢", callback_data="trouble"
    )
    btn4 = types.InlineKeyboardButton("⬅️ 😏Назад😏", callback_data="back")
    markup.add(btn1, btn2, btn3, btn4)
    return markup


# keyboard for info
def info():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("O проекте", callback_data="about_project")
    btn2 = types.InlineKeyboardButton("Контакты", callback_data="contacts")
    btn_back = types.InlineKeyboardButton("️⬅️Назад⬅️", callback_data="back_main")
    markup.add(btn1, btn2, btn_back)
    return markup


responses = {
    "How_used": "Что бы пользоваться мной просто нажимай кнопки  ",
    "trouble": "У тебя есть проблема давай ее решать",
    "ability": "Ммм могу многое в зависимости от того что ты хочешь",
    "about_project": "Привет, меня зовут Андрей, я начинающий программист...",
    "contacts": "Связаться со мной можно по ТГ https://t.me/Andre26ree",
    "jok": "🤣 Вот шутка!",
}
menus = {"main": main_menu, "help": my_help, "info": info}


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
            bot.send_message(message.chat.id, "⚠️ Город не найден, попробуй ещё раз.")
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
    # Проверяем стандартные ответы
    if text in ["привет", "здравствуйте", "ку", "хай", "Как ты"]:
        bot.reply_to(message, f"Привет! {name} Рад тебя видеть!")
        return
    elif text in ["как дела", "чем занимаешься", "что как ты", "ку"]:
        bot.reply_to(message, "Отлично, а у тебя?")
        return
    elif text == "что делаешь?":
        bot.reply_to(message, "Учусь работать с Telebot!")
        return

        # 2. Пробуем получить погоду
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

    # 3. Если ничего не подошло
    bot.reply_to(message, f"Я тебя не понял, {name} 😅")


bot.polling(none_stop=True)
