import telebot
import config
from time import sleep
from telebot import types

bot = telebot.TeleBot(config.TOKEN_CRIMINALIST)

# отношение
relationships = 0

# список [ответов игрока, ответов персонажа, зависимоть отношения]
bot_criminalist = [
    [
        ['Кто? впервые слышу...', 'Я не удивлён...\n', 0],
        ['Хорошо, я запомню. Спасибо!', 'Также скажу, что улики могут быть в любом месте.'
                                        ' Чем больше найдешь, тем лечге будеть поянть проиходящее\n'
                                        'Удачи тебе', 1],
        ['Уяснил. Спасибо, но лучше бы ты закрыл пасть, щенок', 'Я подозревал такое... Ладно, удачи тебе, тварь', -1],
        ['Да пошёл ты! я тут царь, а ты говнарь', 'Я подозревал такое... Ладно, удачи тебе, тварь', -1],
    ]
]


# главная функия диалога
def bot_criminalist_main(num, content):
    markup = types.ReplyKeyboardMarkup(row_width=1)  # создание клавиатуры

    item1 = types.KeyboardButton(bot_criminalist[num][0][0])
    item2 = types.KeyboardButton(bot_criminalist[num][1][0])
    item3 = types.KeyboardButton(bot_criminalist[num][2][0])
    item4 = types.KeyboardButton(bot_criminalist[num][3][0])

    markup.add(item1, item2, item3, item4)  # добовляем эелементы в клавиатуру

    bot.send_message('991296393', content,
                     parse_mode='html', reply_markup=markup)

    # ответ персонажа на ответ игрока
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def said(message):
        global relationships

        for i in range(4):
            if message.text == bot_criminalist[num][i][0]:
                markup_remove = types.ReplyKeyboardRemove()
                sleep(2)
                bot.send_message(message.chat.id, bot_criminalist[num][i][1], reply_markup=markup_remove)
                bot.stop_polling()
                relationships = bot_criminalist[num][i][2]

    bot.polling(none_stop=False, interval=0, timeout=1)  # запрос к серверу

    return relationships  # результат отношения от варината ответа