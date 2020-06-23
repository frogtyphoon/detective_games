import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN_POLICE)

bot_police = [
    [
        ['Я был пьян, что тебе надо?', 'Да как ты смеешь разговаривать со соим начальником???\n'
                                       'Ещё раз что-то вякнишь, сниму зарплату!'],
        ['Да кто ты такой, чтобы мне указывать?\n'
         'Я тебя одним пальцем положу, ты и не встанешь!', 'Да как ты смеешь разговаривать со соим начальником???\n'
                                                           'Ещё раз что-то вякнишь, сниму зарплату!'],
        ['Привет, дружок', 'Хорошо. Я рад, чо ты снова с нами в строю'],
        ['Извиняюсь за своё отсутвие, слегка приболел. Я готов к работе', 'Хорошо. Я рад, чо ты снова с нами в строю'],
    ]
]


def bot_police_main(num):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton(bot_police[num][0][0])
    item2 = types.KeyboardButton(bot_police[num][1][0])
    item3 = types.KeyboardButton(bot_police[num][2][0])
    item4 = types.KeyboardButton(bot_police[num][3][0])

    markup.add(item1, item2, item3, item4)  # добовляем эелементы в клавиатуру

    bot.send_message('991296393', 'Отвечай как можно скорей!',
                     parse_mode='html', reply_markup=markup)

    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def said(message):
        if 'Я был пьян,' in message.text:
            bot.send_message(message.chat.id, bot_police[num][0][1])
            return 

    bot.polling(none_stop=False, interval=0, timeout=2)

