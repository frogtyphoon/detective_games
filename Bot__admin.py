# бот переговорная

import logging
import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from connect import edit_bot

bot = Bot(token=config.TOKEN_ADMIN)
dp = Dispatcher(bot)

# выбор
side, num = 0, 0

logging.basicConfig(level=logging.INFO)

# список [ответов игрока, ответов персонажа, зависимоть отношения]
bot_admin = [
    [
        # Первое убийство
        # 0, соседка с этажа
        ['Что Вы можете нам рассказать из интересного?', 'У неё был парень, имени не знаю', 0],
        ['Вы вчера слышали какие-нибудь звуки из её крватиры?', 'Часов в 8 слышала какие-то звуки', 1],
    ],
    [
        # 1
        ['В тот день он пришёл к ней?', 'Да, он пришёл к часам 8', 0],
        ['Что вы знаете про этого Парня?', 'Ничего, но мужики все странные', 1],
    ],
    [
        # 2
        ['Что нибудь происходило в этот момент?', 'Ещё бы', 0],
        ['Вы знаете, когда он ушёл?', 'Нет...', 1],
    ],
    [
        # 3
        ['Что именно вы слышали?', 'Обрывки фраз по типу «ты не можешь меня бросить после всего» '
                                   'и «мне страшно одной, вдруг он придет.»', 0],
        ['Вы знаете, кто кричал?', 'Слышала, как она кричала, что любит его, а он ее нет.', 1],
    ],
    [
        # 4 (Основа для конца диалога для соседки снизу)
        ['Хорошо, спасибо', 'Уходит...', 0],
        ['Можете быть свободны', 'уходит...', 1],
    ],
    [
        # 5
        ['Какие звуки вы именно слышали?', 'Вроде я слышал крики', 0],
        ['Это мог быть чей-то разговор?', 'Да', 1],
    ],
    [
        # 6
        ['Вы знаете причину?', 'Нет', 0],
        ['Что-нибудь ещё слышали?', 'Нет', 1],
    ],
    [
        # 7
        ['Вы знаете что-нибудь ещё?', 'Нет', 0],
        ['Спасибо, досвидание', 'Уходит...', 1],
    ],
    [
        # 8
        ['Можете сказать, что они кричали друг другу?', 'лышала Обрывки фраз по типу'
                                                        ' «ты не можешь меня бросить после всего»', 0],
        ['Вы занете причину ссоры?', 'Нет', 1],
    ],
    [
        # 9
        ['Кто придёт, вы можете расскзать?', 'Не знаю', 0],
        ['Мог ли парень приченить ей вред?', 'Мужчина существа опасные, так что да', 1],
    ],
]


# ответ персонажа на ответ игрока
@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    global side

    for i in range(4):
        if message.text == bot_admin[num][i][0]:
            markup_remove = types.ReplyKeyboardRemove()
            await asyncio.sleep(2)
            await bot.send_message(message.chat.id, bot_admin[num][i][1], reply_markup=markup_remove)
            side = bot_admin[num][i][2]
            break

    edit_bot(side)


async def check():
    global num
    while True:
        f = open('text.txt', 'r+', encoding='utf8')
        text = [str(i) for i in f.read().split('|')]
        f.close()
        if text[0] == 'Bot__admin':
            open('text.txt', 'w').close()
            num = int(text[1])

            # главная функия диалога
            markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)  # создание клавиатуры

            item1 = types.KeyboardButton(bot_admin[num][0][0])
            item2 = types.KeyboardButton(bot_admin[num][1][0])
            item3 = types.KeyboardButton(bot_admin[num][2][0])
            item4 = types.KeyboardButton(bot_admin[num][3][0])

            markup.add(item1, item2, item3, item4)  # добовляем эелементы в клавиатуру

            await bot.send_message(config.ID_PERSON, text[2], reply_markup=markup)
        await asyncio.sleep(1)


if __name__ == '__main__':
    dp.loop.create_task(check())
    executor.start_polling(dp, skip_updates=True)
