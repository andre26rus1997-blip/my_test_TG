import  telebot
from telebot import types
bot = telebot.TeleBot("8300321950:AAGARJW5aN-9R4q0zA9B5JeLlbeL-pT0cd8")

# Главное меню
def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🤝Помощь✌️",callback_data="help")
    btn2 = types.InlineKeyboardButton("📝Информация📌",callback_data="info")
    btn3 = types.InlineKeyboardButton("🥳Посмейся немного🤣",callback_data="jok")
    btn4 = types.InlineKeyboardButton("⛅Погода🌧️",callback_data="weather")
    btn5 = types.InlineKeyboardButton("❌Удалить🗑️",callback_data="delete")
    markup.add(btn1,btn2,btn3,btn4,btn5)
    return markup

# keyboard for help
def my_help():         #
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("😍Как пользоваться мной😍",callback_data="How_used")
    btn2 = types.InlineKeyboardButton("❤️Что я могу❤️",callback_data="ability")
    btn3 = types.InlineKeyboardButton("😭Напиши мне свою проблему😢",callback_data="trouble")
    btn4 = types.InlineKeyboardButton("⬅️ 😏Назад😏",callback_data="back")
    markup.add(btn1,btn2,btn3,btn4)
    return markup
# keyboard for info
def info():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("O проекте",callback_data="about_project")
    btn2 = types.InlineKeyboardButton("Контакты",callback_data="contacts")
    btn_back = types.InlineKeyboardButton("️⬅️Назад⬅️",callback_data="back_main")
    markup.add(btn1,btn2,btn_back)
    return markup

responses = {
    "How_used":"Что бы пользоваться мной просто нажимай кнопки  ",
    "trouble":"У тебя есть проблема давай ее решать",
    "ability":"Ммм могу многое в зависимости от того что ты хочешь",
    "about_project":"Привет, меня зовут Андрей, я начинающий программист...",
    "contacts": "Связаться со мной можно по ТГ https://t.me/Andre26ree",
    "jok": "🤣 Вот шутка!",
    "weather": "⛅ Сегодня хорошая погода "
}
menus = {
    "main": main_menu,
    "help": my_help,
    "info": info 
    }




@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Главное меню для тебя мой дорогой ❤️", reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        bot.delete_message(call.message.chat.id,call.message.message_id)
    except:
        pass




    # Если кнопка есть в словаре 
    if call.data in responses:
        bot.send_message(call.message.chat.id,responses[call.data])


    # Если кнопка соответствует в меню 
    elif call.data in menus:
        bot.send_message(
            call.message.chat.id,
            "Выберети кнопку👇",
            reply_markup=menus[call.data]()
        )




    elif call.data =="back" or call.data == "back_main":
        bot.send_message(call.message.chat.id,"🔙 Возврат в главное меню",reply_markup=main_menu())


@bot.message_handler(content_types=["text"])
def reply(message):
    name = message.from_user.first_name
    text = message.text.lower()
    if text in["привет","здравствуйте","ку","хай","Как ты"]:
        bot.reply_to(message,f"Привет! {name} Рад тебя видеть!")
    elif text in ["как дела","чем занимаешься","что как ты","ку"]:
        bot.reply_to(message,"Отлично, а у тебя?")
    elif text == "что делаешь?":
        bot.reply_to(message,"Учусь работать с Telebot!")
    else:
        bot.reply_to(message,f"Я тебя не понял  {name} 😅")



bot.polling(none_stop=True)