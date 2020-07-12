import logging
import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from connect import edit_bot


bot = Bot(token=config.TOKEN_HELP)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

side, num = 0, 0

bot_help = [
    [
        # 0, вступление
        ['Кто это пишет?', 'Я не могу скзаать, тк если меня поймают', 0],
        ['Вы уверены, что это тот человек?', 'Да', 1],
    ],
    [
        # 1
        ['Вы уверены, что это тот человек?', 'Да', 0],
        ['Почему вам стоит доверять?', 'Не могу дать гарантий в свой адрес', 1],
    ],
    [
        # 2
        ['Спасибо за помощь в расследовании', 'Рад помочь', 0],
        ['Хорошо, мы сделаем всё, что в наших силах', 'Спасибо', 0],
    ],
    [
        # 3
        ['Спасибо за помощь в расследовании', 'Рад помочь', 0],
        ['Почему вам стоит доверять?', 'Не могу дать гарантий в свой адрес', 1],
    ],
]


# ответ персонажа на ответ игрока
@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    global side

    for i in range(4):
        if message.text == bot_help[num][i][0]:
            markup_remove = types.ReplyKeyboardRemove()
            await asyncio.sleep(2)
            await bot.send_message(message.chat.id, bot_help[num][i][1], reply_markup=markup_remove)
            side = bot_help[num][i][2]
            break

    edit_bot(side)


async def check():
    global num
    while True:
        f = open('text.txt', 'r+', encoding='utf8')
        text = [str(i) for i in f.read().split('|')]
        f.close()
        if text[0] == 'Bot__help':
            open('text.txt', 'w').close()
            num = int(text[1])

            # главная функия диалога
            markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)  # создание клавиатуры

            item1 = types.KeyboardButton(bot_help[num][0][0])
            item2 = types.KeyboardButton(bot_help[num][1][0])

            markup.add(item1, item2)  # добовляем эелементы в клавиатуру

            await bot.send_message(config.ID_PERSON, text[2], reply_markup=markup)
        await asyncio.sleep(1)


if __name__ == '__main__':
    dp.loop.create_task(check())
    executor.start_polling(dp, skip_updates=True)