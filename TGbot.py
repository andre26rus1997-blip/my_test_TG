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
}



@bot.message_handler(commands=["start"])
def start(message):


    try:
        bot.delete_message(message.chat.id,message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении /start:{e}")

    bot.send_message(message.chat.id,"Главное меню для тебя мой дорогой",reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if call.data in responses:
        bot.send_message(call.message.chat.id,responses[call.data])



    elif call.data == "help":

        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Это раздел помощи пожалуйста не стесняйся ", reply_markup=my_help())
    elif call.data =="info":

        bot.send_message(call.message.chat.id,"📌 Это раздел информации. Выбери, что тебе интересно:",reply_markup=info())
        bot.delete_message(call.message.chat.id,call.message.message_id)
    elif call.data =="about_project":
        bot.send_message(call.message.chat.id,"Привет меня зовут Андрей я начинающий "
                                              "програмист этот пот пой первый пед проэкт , который будет вклюать по мксимуму функций , по которым я "
                                              "буду учиться програмированию и TeleBot. 🛠 ")
    elif call.data =="contacts":
        bot.send_message(call.message.chat.id,"Связаться со мной можно по ТГ https://t.me/Andre26ree")

    elif call.data =="info":
        bot.send_message(call.message.chat.id,"Это команда info")
    elif call.data =="jok":
        bot.send_message(call.message.chat.id,"This is jok")
    elif call.data =="weather":
        bot.send_message(call.message.chat.id,"эта погода ")

    elif call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id,"🥳Главное меню снова тут 🥳",reply_markup=main_menu())

    elif call.data =="back":
        bot.delete_message(call.message.chat.id, call.message.message_id)
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