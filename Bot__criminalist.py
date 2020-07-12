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


# первое убийство
# пока улики выглядт как текст, возможно в будущем это буду картинки

# улика 1
@dp.message_handler(commands=['cvDfQx'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'На шее есть едва заметный след от веревки,'
                                            ' подозрение на удушение, а не самоубийство')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 2
@dp.message_handler(commands=['YxCcog'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Не одни мужские следы в прихожей, был кто-то еще, кроме ее парня.')
    edit_bot(0)  # говорим, что одна улика найдена


# улика 3
@dp.message_handler(commands=['JURXEP'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Предсмертная записка на кухонном столе, но почерк не ее, '
                                            'если разобрать тетради с записями с лекций.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 4
@dp.message_handler(commands=['xBorjB'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'В личном дневнике девушки, спрятанном на кухне, есть записи о том, что она'
                                            ' кого-то боится, подозрение, что убийцу.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 5
@dp.message_handler(commands=['fHuFhQ'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'В кухонном шкафу найдены шприцы, как их применяла '
                                            'девушка- не известно.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена

# Второе убийство

# улика 1
@dp.message_handler(commands=['tYeowX'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Пуля была выпущена с правой стороны, но жена говорит, что он был левшой.') # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 2
@dp.message_handler(commands=['alVmku'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'В доме были найдены следы драки, о чем свидетельствует кровь на полу возле входной двери.')
    edit_bot(0)  # говорим, что одна улика найдена


# улика 3
@dp.message_handler(commands=['SRhzEk'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Шприцы с неизвестным веществом были найдены в мусорном баке недалеко от дома.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 4
@dp.message_handler(commands=['OCVfku'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Открытая квартира, значит, убийца не закрыл за собой дверь, после убийства')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 5
@dp.message_handler(commands=['lLAinF'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Еще теплая сигарета, если бы это было самоубийство, он бы докурил.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена

# Третье убийство

# улика 1
@dp.message_handler(commands=['EWiBQY'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Горячий чайник и две кружки, одна из которых стояла помытой возле раковины.') # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 2
@dp.message_handler(commands=['EGgSmc'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Сцарапанный лак на ногтях, жертва сопротивлялась и пыталась удержаться.')
    edit_bot(0)  # говорим, что одна улика найдена


# улика 3
@dp.message_handler(commands=['bvGuQd'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'На жертве замечены заживающие следы от инъекций')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 4
@dp.message_handler(commands=['ADzzJz'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Содранная мужская сережка, зажатая в кулаке жертвы, с кровью неизвестного')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 5
@dp.message_handler(commands=['OakEHo'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Найден дневник с записью на неизвестном языке, а также шприцы за батареей.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена

# Четвертое убийство

# улика 1
@dp.message_handler(commands=['HdKpla'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'В сумке найдены шприцы и вложенные в записную книгу пакетики с неизвестным веществом.') # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 2
@dp.message_handler(commands=['EbaSkQ'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'На венах девушки видны были уже заживающие следы от инъекций.')
    edit_bot(0)  # говорим, что одна улика найдена


# улика 3
@dp.message_handler(commands=['xPAlvZ'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Нашли на руке какие-то символы. Пхоже на адрес или пароль. Думаю с ними стоит разобраться потом')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 4
@dp.message_handler(commands=['jDsWcm'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'Пена у рта похожа, на ту, что бывает при отравлении сильнейшим ядом - мышьяком.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена

# Пятое убийство

# улика 1
@dp.message_handler(commands=['WjYyPx'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'В шприце, который использовала жертва, видно, что вместо стандартной нормы был весь шприц, '
                                            'что говорит о смертельной дозе') # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 2
@dp.message_handler(commands=['vHTupk'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'На пострадавшем есть следы от удушья.')
    edit_bot(0)  # говорим, что одна улика найдена


# улика 3
@dp.message_handler(commands=['aSDzMl'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'На дверной руке имеются следы крови, но не жертвы. Скорее всего, убийца поранился шприцем.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 4
@dp.message_handler(commands=['mCSysL'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'На полу имеются потертости. Скорее всего, убийца был в обуви с грубой подошвой.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена


# улика 5
@dp.message_handler(commands=['FbmigM'])
async def said(message: types.Message):
    await bot.send_message(message.chat.id, 'В мусорном ведре есть пустые пакетики, в которых было неизвестное содержимое.')  # отправляем улику
    edit_bot(0)  # говорим, что одна улика найдена

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