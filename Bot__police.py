import logging
import config
from config import bot, dp
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from s_m import loop_m
from connect import edit_bot

# отношение
relationships, num = 0, 0

logging.basicConfig(level=logging.INFO)

# список [ответов игрока, ответов персонажа, зависимоть отношения]
bot_police = [
    [
        # 0
        ['Я был пьян, что тебе надо?', 'Да как ты смеешь разговаривать со своим начальником???', -1],
        ['Да кто ты такой, чтобы мне указывать?\n'
         'Я тебя одним пальцем положу, ты и не встанешь!', 'Да как ты смеешь разговаривать со соим начальником???', -2],
        ['Привет, дружок', 'Хорошо', 0],
        ['Извиняюсь за своё отсутвие, слегка приболел. Я готов к работе', 'Хорошо', 1]
    ],
    [
        # 1
        ['Да пошёл ты!', 'Да как ты смеешь так разговаривать со мной?', -1],
        ['Я тоже рад, сэр', 'У нас не подалеку совершилось самоубийтсво. Тебе стоит выехать и разобраться.'
                            ' Возможно здесь что-то не чисто. Это серьёзное дело, будь готов ко всему', 1],
        ['Я слушаю указаний', 'У нас не подалеку совершилось самоубийтсво. Тебе стоит выехать и разобраться.'
                              ' Возможно здесь что-то не чисто. Это серьёзное дело, будь готов ко всему', 0],
        ['Могу ещё отказаться, так что можно быстрее?', 'У нас не подалеку совершилось самоубийтсво.'
                                                        ' Тебе стоит выехать и разобраться.'
                                                        ' Возможно здесь что-то не чисто. Это серьёзное дело,'
                                                        ' будь готов ко всему', 0],
    ],
    [
        # 2
        ['Это мы ещё посмотрим...\nКто тут страх потерял', 'Не зли меня детектив!', -1],
        ['Да... Это... Забывлся я', 'Хорошо', 0],
        ['Извините, я перепутал диаолги. Это было адресована не Вам', 'Хорошо', 1],
        ['Случайно потерял', 'Хорошо', 0],
    ],
    [
        # 3
        ['Так точно', 'Жду отчётов', 0],
        ['Как скажите, брат)', 'Жду отчётов', 1],
        ['Конец связи', 'Жду отчётов', 0],
        ['15 мин, тоже мне', 'Попробуй только опоздать', -1],
    ],
    [
        # 4
        ['Ты мне не указ\n Моя жизнь, мои правила', 'Так, всё. Не беси меня', -1],
        ['Хочется подойти к тебя и харкунть в лицо за такое отношение ко мне.'
         ' Вспомни, просто вспомни!', 'Так, всё. Не беси меня', -2],
        ['Ох, как заговорил... Выкладывай давай', 'Ты так со мной не шути...', 0],
        ['Извините, я что-то перепутал. Думал на свзи мой друг, а тут вы', 'Ты так со мной не шути...', 1],
    ]
]


# ответ персонажа на ответ игрока
@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    global relationships

    for i in range(4):
        if message.text == bot_police[num][i][0]:
            markup_remove = types.ReplyKeyboardRemove()
            await asyncio.sleep(2)
            await bot.send_message(message.chat.id, bot_police[num][i][1], reply_markup=markup_remove)
            relationships = bot_police[num][i][2]
            break

    edit_bot(relationships)


async def check():
    global num
    while True:
        f = open('text.txt', 'r+', encoding='utf8')
        text = [str(i) for i in f.read().split('|')]
        f.close()
        if text[0] == 'Bot__police':
            open('text.txt', 'w').close()
            num = int(text[1])

            # главная функия диалога
            markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)  # создание клавиатуры

            item1 = types.KeyboardButton(bot_police[num][0][0])
            item2 = types.KeyboardButton(bot_police[num][1][0])
            item3 = types.KeyboardButton(bot_police[num][2][0])
            item4 = types.KeyboardButton(bot_police[num][3][0])

            markup.add(item1, item2, item3, item4)  # добовляем эелементы в клавиатуру

            await bot.send_message(config.ID_PERSON, text[2], reply_markup=markup)
        await asyncio.sleep(1)


if __name__ == '__main__':
    dp.loop.create_task(check())
    executor.start_polling(dp, skip_updates=True)
