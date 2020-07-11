import logging
import config
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from connect import edit_bot

bot = Bot(token=config.TOKEN_POLICE)
dp = Dispatcher(bot)

# отношение
relationships, num = 0, 0

logging.basicConfig(level=logging.INFO)

# список [ответов игрока, ответов персонажа, зависимоть отношения]
bot_police = [
    [
        # 0, вступление
        ['Я был пьян и не сосвем понимаю... Что тебе надо? Сидел бы и молчал',
         'Да как ты смеешь разговаривать так со мной, после всего что произолшо с нами?', -1],
        ['Да кто ты такой, чтобы мне указывать?\n'
         'Я тебя одним пальцем уделаю, ты и не встанешь!\nПодумай о своём поведение',
         'Да как ты смеешь разговаривать так со мной, после всего что произошло с нами?', -2],
        ['Привет, дружок', 'Хорошо', 0],
        ['Извиняюсь за своё отсутвие, слегка приболел. Я готов к работе', 'Хорошо', 1]
    ],
    [
        # 1
        ['Да пошёл ты!\nРад он... ага', 'Да как ты смеешь так разговаривать со мной?', -1],
        ['Я тоже рад, сэр', 'Так, приступим', 1],
        ['Я слушаю указаний', 'Так, приступим', 0],
        ['Могу ещё отказаться, так что можно быстрее?', 'Так, приступим', 0],
    ],
    [
        # 2
        ['Это мы ещё посмотрим...\nКто тут страх потерял', 'Не зли меня, детектив!', -1],
        ['Да... Это... Забывлся я', 'Хорошо', 0],
        ['Извини, я перепутал диалоги. Это было адресована не тебе', 'Хорошо', 1],
        ['Случайно потерял', 'Ясно...', 0],
    ],
    [
        # 3
        ['Так точно', 'Жду отчётов', 0],
        ['Как скажите', 'Жду отчётов', 0],
        ['Конец связи', 'Жду отчётов', 0],
        ['15 мин, тоже мне', 'Попробуй только опоздать', -1],
    ],
    [
        # 4
        ['Ты мне не указ\nМоя жизнь, мои правила', 'Так, всё. Не беси меня', -1],
        ['Хочется подойти к тебя и харкунть в лицо за такое отношение ко мне\n'
         'Я то всё помню, а ты вроде нет', 'Так, всё. Не беси меня', -2],
        ['Ох, как заговорил... Выкладывай давай', 'Ты так со мной не шути...', 0],
        ['Извини, я что-то перепутал. Думал на связи мой друг, а тут ты', 'Ты так со мной не шути...', 1],
    ],
    [
        # 5, мини диалог
        ['Пока не знаю... Всё только выстраивается у меня в голове', 'Хорошо', 0],
        ['Сложно сказать...', 'Хорошо', 0],
        ['Да, многое уже понятно', 'Хорошо', 1],
        ['Не лезь в чужое дело...', 'Как скажешь... Я только хотел узнать', -1],
    ],
    [
        # 6, опрос (тут цифры выолняют индексацию диалога, чтобы сказать с кем мы обащемся)
        ['Соседка с этажа', 'Хорошо', 1],
        ['Сосед этажом ниже', 'Хорошо', 2],
        ['Лучшая подруга', 'Хорошо', 3],
        ['Парень', 'Хорошо', 4],
    ],
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
