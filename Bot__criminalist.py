import logging
import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from connect import edit_bot

bot = Bot(token=config.TOKEN_CRIMINALIST)
dp = Dispatcher(bot)

# отношение
relationships, num = 0, 0

logging.basicConfig(level=logging.INFO)

# список [ответов игрока, ответов персонажа, зависимоть отношения]
bot_criminalist = [
    [
        # 0
        ['Кто? впервые слышу...', 'Ничего нового', 0],
        ['Хорошо, я запомню. Спасибо!', 'Также скажу, что улики могут быть в любом месте.'
                                        ' Чем больше найдешь, тем легче будет понять происходящее\n'
                                        'Удачи тебе)', 1],
        ['Уяснил. Спасибо, но лучше бы ты закрыл пасть, помощник', 'Я подозревал такое... Ладно, удачи тебе\n'
                                                                   'Всё равно буду рад помочь тебе', -1],
        ['Да пошёл ты! я тут царь, а ты говнарь', 'Я подозревал такое... Ладно, удачи тебе\n'
                                                  'Всё равно буду рад помочь тебе', -1],
    ],
    [
        # 1
        ['Да пососи', 'Мда...', -1],
        ['Ну бывает, извиняй', 'Спасибо хоть на этом... Удачи там, поторопись', 1],
        ['Постараюсь тебя вспомнить, а то башка раскалывается...', 'Спасибо хоть на этом... Удачи там, поторопись', 1],
        ['Держи в курсе', 'Постараюсь', 0],
    ],
]


# ответ персонажа на ответ игрока
@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    global relationships

    for i in range(4):
        if message.text == bot_criminalist[num][i][0]:
            markup_remove = types.ReplyKeyboardRemove()
            await asyncio.sleep(2)
            await bot.send_message(message.chat.id, bot_criminalist[num][i][1], reply_markup=markup_remove)
            relationships = bot_criminalist[num][i][2]
            break

    edit_bot(relationships)


async def check():
    global num
    while True:
        f = open('text.txt', 'r+', encoding='utf8')
        text = [str(i) for i in f.read().split('|')]
        f.close()
        if text[0] == 'Bot__криминалист':
            open('text.txt', 'w').close()
            num = int(text[1])

            # главная функия диалога
            markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)  # создание клавиатуры

            item1 = types.KeyboardButton(bot_criminalist[num][0][0])
            item2 = types.KeyboardButton(bot_criminalist[num][1][0])
            item3 = types.KeyboardButton(bot_criminalist[num][2][0])
            item4 = types.KeyboardButton(bot_criminalist[num][3][0])

            markup.add(item1, item2, item3, item4)  # добовляем эелементы в клавиатуру

            await bot.send_message(config.ID_PERSON, text[2], reply_markup=markup)
        await asyncio.sleep(1)


if __name__ == '__main__':
    dp.loop.create_task(check())
    executor.start_polling(dp, skip_updates=True)