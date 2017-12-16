import telebot

token = "403570865:AAE3M9pxGBnWLh-nTMEONnvykQhfY2W6NpQ"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Добавить товар', 'Отправить')
    bot.send_message(message.chat.id, """Здравствуйте,чтобы ваша вещь была опубликована 
Отправьте нам сообщение с таким описание:
Фотографию
Название вещи
Размер
Цена 
Ваш город
Также в настройках проверьте что бы у вас был добавлен ник.
Текст Сообщения должен быть до 120 символов.
После окончания описания, нажмите кнопку "Отправить" """,reply_markup=user_markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if (int(len(message.text)) > 120):
        bot.send_message(message.chat.id, 'Длина сообщения должна быть меньше 120 символов')
    elif message.text == "Отправить":
    	bot.send_message(message.chat.id, 'Спасибо,ваш пост будет скоро опубликован, чтобы добавить еще один товар нажмите кнопку "Добавить товар"')
    elif message.text == "Добавить товар":
        bot.send_message(message.chat.id, """Здравствуйте,чтобы ваша вещь была опубликована 
Отправьте нам сообщение с таким описание:
Фотографию
Название вещи
Размер
Цена 
Ваш город
Также в настройках проверьте что бы у вас был добавлен ник.
Текст Сообщения должен быть до 120 символов.
После окончания описания, нажмите кнопку "Отправить" """) 	
bot.polling(none_stop=True, interval=0)
