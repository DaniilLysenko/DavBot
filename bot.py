import telebot

token = ""

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Отправить')
    voskl = u'\U00002757'
    check = u'\U00002705'
    minus = u'\U000026D4'
    bot.send_message(message.chat.id, """Чтобы ваша вещь была опубликована,отправьте смс с таким описанием:
Фото (отправляйте не документом)
Название
Размер
Цена
Город
Не пишите информацию в описании под фото.
В настройках проверьте чтобы у вас был добавлен ник""" + voskl +
"""После окончания нажмите кнопку «отправить»"""+ check +
"""\nБЕЗ ДОБАВЛЕННОГО НИКА В НАСТРОЙКАХ,ВАШ ПОСТ НЕ БУДЕТ ОПУБЛИКОВАН!"""+minus,reply_markup=user_markup)

res = {}
ids = [307513248,462143542,399588814]
photo = {}

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global res, photo
    if (int(len(message.text)) > 120):
        bot.send_message(message.chat.id, 'Длина сообщения должна быть меньше 120 символов')
    elif message.text == "Отправить":
        if photo.get(message.from_user.id) != None:
            if res.get(message.from_user.id) != None and len(res[message.from_user.id]) > 0:
                if message.from_user.username == None:
                    bot.send_message(message.chat.id, 'Укажите ник в настройках!')
                else:
                    uid = message.from_user.id
                    bot.send_message(message.chat.id, """Спасибо, ваш пост будет скоро опубликован
    Вы можете отправить ещё одну вещь.""")
                    res[uid] += "Продавец - https://telegram.me/" + str(message.from_user.username)
                    for num in ids:
                        bot.send_photo(num, photo[uid])
                        bot.send_message(num, res[uid])
                    res.pop(uid)
                    photo.pop(uid)
            else:
                bot.send_message(message.chat.id, 'Вы ничего не добавили в описание')
        else:
            bot.send_message(message.chat.id, 'Вы не добавили фотографию товара')
                
    else:
        if (res.get(message.from_user.id) != None):  
            res[message.from_user.id] += message.text + "\n"
        else:
            res[message.from_user.id] = message.text + "\n"
    
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    global photo
    if message.from_user.username == None:
        bot.send_message(message.chat.id, 'Укажите ник в настройках!')
    else: 
        photo[message.from_user.id] = message.photo[0].file_id
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
