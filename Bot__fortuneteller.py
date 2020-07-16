import logging
import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from connect import edit_bot


bot = Bot(token=config.TOKEN_FORTUNETELLER)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

side, num = 0, 0

Bot_fortuneteller = [
    [
        # 0, вступление
        ['Вы кто?', 'Я гадалка', 0],
        ['Здравствуйте. Позволите задать вам несколько вопросов?', 'Да', 1],
    ],
    [
        # 1
        ['Нет времени. Могу я вам задать несколько вопросов?', 'Да', 0],
        ['Не могу скзаать, можеи перейти к делу?', 'Да', 1],
    ],
    [
        # 2
        ['Скажите, знали ли вы Софию Хорову?»', 'Не могу точно сказать', 0],
        ['Вы моежете сказать, кто убил Софью Хорову?', 'Не могу точно сказать', 0],
    ],
    [
        # 3
        ['Спасибо за помощь в расследовании', 'Рад помочь', 0],
        ['Почему вам стоит доверять?', 'Не могу дать гарантий в свой адрес', 1],
    ],
    [
        # 4
        ['Я расследую её убийство. Ваши координаты были записаны на её руке,'
         ' и я хотел бы знать, как вы с этим связаны, и что вы знаете', 'Её убили… Мне жаль', 0],
        ['Я её знакомый, она пропала и не отзывается уже полтора дня, её никто не видел, и она не отвечает на'
         ' звонки. Она говорила про вас, может, вы что-то знаете?', 'Простите, связывайтесь со '
                                                                    'следствием, я ничего не знаю', 1],
    ],
    [
        # 5
        ['Спасибо за помощь', 'Чат закрыт', 0],
        ['Спасибо за сотрудничество, мы гарантируем вашу безопасность', 'Чат закрыт', 1],
    ],
    [
        # 6
        ['Что же, спасибо, вы правы...', 'Чат закрыт', 0],
        ['Но вы же гадалка!', 'Чат закрыт', 1],
    ],
    [
        # 7
        ['', '', 0],
        ['', '', 0],
    ],
]


# ответ персонажа на ответ игрока
@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    global side

    for i in range(4):
        if message.text == Bot_fortuneteller[num][i][0]:
            markup_remove = types.ReplyKeyboardRemove()
            await asyncio.sleep(2)
            await bot.send_message(message.chat.id, Bot_fortuneteller[num][i][1], reply_markup=markup_remove)
            side = Bot_fortuneteller[num][i][2]
            break

    edit_bot(side)


async def check():
    global num
    while True:
        f = open('text.txt', 'r+', encoding='utf8')
        text = [str(i) for i in f.read().split('|')]
        f.close()
        if text[0] == 'Bot__fortuneteller':
            open('text.txt', 'w').close()
            num = int(text[1])

            # главная функия диалога
            markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)  # создание клавиатуры

            item1 = types.KeyboardButton(Bot_fortuneteller[num][0][0])
            item2 = types.KeyboardButton(Bot_fortuneteller[num][1][0])

            markup.add(item1, item2)  # добовляем эелементы в клавиатуру

            await bot.send_message(config.ID_PERSON, text[2], reply_markup=markup)
        await asyncio.sleep(1)


if __name__ == '__main__':
    dp.loop.create_task(check())
    executor.start_polling(dp, skip_updates=True)