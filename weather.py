import requests

API = "9d25c51fa1e0dfe91110828f36f71afb"

def get_weather_emoji(description: str) -> str:
    """Возвращает эмодзи для погодного описания"""
    description = description.lower()
    if "ясн" in description:
        return "☀️"
    elif "облач" in description:
        return "☁️"
    elif "пасмур" in description:
        return "☁️"
    elif "дожд" in description:
        return "🌧"
    elif "гроза" in description:
        return "⛈"
    elif "снег" in description:
        return "❄️"
    elif "туман" in description:
        return "🌫"
    else:
        return "🌍"


def send_weather(bot,API,message):
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

            emoji = get_weather_emoji(description)

            bot.send_message(
                message.chat.id,
                f"🌍 Погода в {city.title()}:\n"
                f"🌡 Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"💧 Влажность: {humidity}%\n"
                f"🔽 Давление: {pressure} мм рт. ст.\n"
                f"💨 Ветер: {wind} м/с\n"
                f"{emoji} Состояние: {description.capitalize()}",
            )
        else:
            bot.send_message(
                message.chat.id, "⚠️ Город не найден, попробуй ещё раз.")
            bot.register_next_step_handler(message, send_weather)
    except Exception as e:
        print("Ошибка в send_weather:", e)
        bot.send_message(
            message.chat.id, "Ошибка при получении данных. Попробуй позже.")