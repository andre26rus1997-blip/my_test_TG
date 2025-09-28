

from telebot import types

# Главное меню


def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🤝Помощь✌️", callback_data="help")
    btn2 = types.InlineKeyboardButton("📝Информация📌", callback_data="info")
    btn3 = types.InlineKeyboardButton(
        "🥳Посмейся немного🤣", callback_data="jok")
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
    btn2 = types.InlineKeyboardButton(
        "❤️Что я могу❤️", callback_data="ability")
    btn3 = types.InlineKeyboardButton(
        "😭Напиши мне свою проблему😢", callback_data="trouble"
    )
    btn4 = types.InlineKeyboardButton("⬅️ 😏Назад😏", callback_data="back")
    markup.add(btn1, btn2, btn3, btn4)
    return markup


# keyboard for info
def info():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(
        "O проекте", callback_data="about_project")
    btn2 = types.InlineKeyboardButton("Контакты", callback_data="contacts")
    btn_back = types.InlineKeyboardButton(
        "️⬅️Назад⬅️", callback_data="back_main")
    markup.add(btn1, btn2, btn_back)
    return markup
