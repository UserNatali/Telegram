import telebot
from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name} </u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, 'І тобі привіт', parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Твій id:{message.from_user.id}', parse_mode='html')
#     elif message.text == 'фото':
#         photo = open('photo_2022-02-11_12-50-06.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, 'Я тебе не розумію', parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, яке круте фото')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить вебсайт", url="https://itproger.com"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Старт')
    markup.add(types.InlineKeyboardButton("Посетить вебсайт", url="https://itproger.com"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)




bot.polling(none_stop=True)
