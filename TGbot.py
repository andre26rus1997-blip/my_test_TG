import telebot
from keyboards import main_menu, my_help, info
from responses import simple_responses, responses
from weather import send_weather, get_weather_emoji


bot = telebot.TeleBot("8429683137:AAEhGBEH0AAIAxkCojS3aNDbfqMcGwmdHpA")
API = "9d25c51fa1e0dfe91110828f36f71afb"

menus = {
    "main": main_menu,
    "help": my_help,
    "info": info
}


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, "Главное меню для тебя мой дорогой ❤️", reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "weather":
        bot.send_message(call.message.chat.id, "🌍 Напиши название города:")
        bot.register_next_step_handler(call.message, lambda m: send_weather(bot, API, m))

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





# Ответы на простые соообщения
@bot.message_handler(content_types=["text"])
def reply(message):
    name = message.from_user.first_name
    text = message.text.lower().strip()

    for keys, response in simple_responses.items():
        if text in keys:
            bot.reply_to(message, response.format(name=name))
            return

  


bot.polling(none_stop=True)
