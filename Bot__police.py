import telebot
import config
from time import sleep
from telebot import types

bot = telebot.TeleBot(config.TOKEN_POLICE)

# отношение
relationships = 0

# список [ответов игрока, ответов персонажа, зависимоть отношения]
bot_police = [
    [
        ['Я был пьян, что тебе надо?', 'Да как ты смеешь разговаривать со своим начальником???\n'
                                       'Ещё раз что-то вякнишь, сниму зарплату!', -1],
        ['Да кто ты такой, чтобы мне указывать?\n'
         'Я тебя одним пальцем положу, ты и не встанешь!', 'Да как ты смеешь разговаривать со соим начальником???\n'
                                                           'Ещё раз что-то вякнишь, сниму зарплату!', -2],
        ['Привет, дружок', 'Хорошо. Я рад, что ты снова с нами в строю', 0],
        ['Извиняюсь за своё отсутвие, слегка приболел. Я готов к работе', 'Хорошо. Я рад, чо ты снова с нами в строю',
         1],
    ]
]

# главная функия диалога
def bot_police_main(num):
    markup = types.ReplyKeyboardMarkup(row_width=1)  # создание клавиатуры

    item1 = types.KeyboardButton(bot_police[num][0][0])
    item2 = types.KeyboardButton(bot_police[num][1][0])
    item3 = types.KeyboardButton(bot_police[num][2][0])
    item4 = types.KeyboardButton(bot_police[num][3][0])

    markup.add(item1, item2, item3, item4)  # добовляем эелементы в клавиатуру

    bot.send_message('991296393', 'Отвечай как можно скорей!',
                     parse_mode='html', reply_markup=markup)

    # ответ персонажа на ответ игрока
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def said(message):
        global relationships

        for i in range(4):
            if message.text == bot_police[num][i][0]:
                markup_remove = types.ReplyKeyboardRemove()
                sleep(2)
                bot.send_message(message.chat.id, bot_police[num][i][1], reply_markup=markup_remove)
                bot.stop_polling()
                relationships = bot_police[num][i][2]

    bot.polling(none_stop=False, interval=0, timeout=1)  # запрос к серверу

    return relationships  # результат отношения от варината ответа
