import telebot
import config
import time
from telebot import types


bot = telebot.TeleBot(config.TOKEN_ADMIN)

#  отправка первого сообщения без ввода
#  создание клавиатуры
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Да')
item2 = types.KeyboardButton('Конечно да!')

markup.add(item1, item2)  # добовляем эелементы в клавиатуру

bot.send_message('991296393','Здравствуйте, <b>Павел</b>\nВы хотите принять участие в нашей игре?',
                 parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def said(message):
    if message.text == 'Да' or message.text == 'Конечно да!':
        bot.send_message(message.chat.id, 'Начинаем')
        time.sleep(0.5)

        bot.send_message(message.chat.id, 'Правила игры:\n1)fdfdfdfdff\n2)fdfdfdfdfdf'
                                          '\n3)fdfsfsdfdffdf')
        time.sleep(4)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Да')
        item2 = types.KeyboardButton('Конечно да!')
        markup.add(item1, item2)  # добовляем эелементы в клавиатуру

        bot.send_message(message.chat.id, 'Всё понятно?', reply_markup=markup)


# @bot.message_handler(commands=['start'])
# def said(message):
#     # клавиатура
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Да')
#     item2 = types.KeyboardButton('Конечно да!')
#
#     markup.add(item1, item2)  # добовляем эелементы в клавиатуру
#
#     bot.send_message(message.chat.id, message.chat.id)
#     bot.send_message(message.chat.id, 'Здравствуйте, <b>{0.first_name}</b>\n'
#                                       'Вы хотите принять участие в нашей игре?'.format(message.from_user),
#                      parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)

