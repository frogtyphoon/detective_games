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
        # 0, Начало связки - соседка с этажа
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
    [
        # 10, Начало связки - сосед этажом ниже
        ['Что вы моежете сказать о  вашей соседке Лене?', 'Ну...', 0],
        ['Вы что-нибудь слышали подозрительное вчера ?', 'Да', 1],
    ],
    [
        # 11
        ['Почему?\nБыла не добра к вам?', 'Не особо', 0],
        ['Почему?\nМешала вам?', 'Да', 1],
    ],
    [
        # 12 (Основа для конца диалога с соседом этажом ниже )
        ['Спасибо, Вы нам помогли. Нам пора ', 'Уходит...', 0],
        ['Можете быть свободны', 'Уходит...', 1],
    ],
    [
        # 13
        ['Знаете почему были эти оры?', 'Ненаивадела кого-то', 0],
        ['Знаете кому они адресованы?', 'Да, её парню', 1],
    ],
    [
        # 14
        ['Знаете почему были эти оры?', 'Она кричала', 0],
        ['Знаете кому они адресованы?', 'Да, её парню', 1],
    ],
    [
        # 15
        ['Знаете кому?', 'Да, вроде её парню', 0],
        ['По какой причине она кричала?', 'Не знаю... ', 1],
    ],
    [
        # 16
        ['Вы видели как он входил или выходил?', 'Нет', 0],
        ['Знаете, почему были эти оры?', 'Она ненавидела его', 1],
    ],
    [
        # 17, Начало связки - лучшая подруга
        ['Что Вы можете сказать про свою подругу?', 'Она была классной подругой, но до половины первого курса... ', 0],
        ['Были ли у неё каке-то проблемы?', 'Не могу сказать точно', 1],
    ],
    [
        # 18
        ['Как она изменилась?', 'Она была то активной, то вообще никакой', 0],
        ['Вы знаете, почему это произолшо?', 'Нет...', 1],
    ],
    [
        # 19 (Основа для конца диалога с лучшей подругой)
        ['Спасибо', 'Уходит...', 0],
        ['Хорошо, идите', 'Уходит...', 1],
    ],
    [
        # 20
        ['Это мог быть из-за бликих к ней людей?', 'Сказать не могу, но возможно из-за парня', 0],
        ['В тот момент ходил гриб, могла ли она заболеть?', 'Было похоже на это', 1],
    ],
    [
        # 21
        ['Что именно происходило?', 'Стали часто ссорится', 0],
        ['Да, лично', 'Было похоже на это', 1],
    ],
    [
        # 22
        ['Вы знаете причину?', 'Нет', 0],
        ['Он угрожал ей?', 'Не могу сказать, но она мне гвоорила, что кого-то боиться', 1],
    ],
    [
        # 23
        ['Это мог быть её парень?', 'Не могу сказать точно', 0],
        ['У неё были враги?', 'Врагов у неё не было и это точно', 1],
    ],
    [
        # 24, Начало связки - парень
        ['Да, я знаю\nСкажите мне,  что было с вашими отношениями?', 'Всё было хорошо, пока она не изменилось', 0],
        ['Знаю\nЧто можете сказать о Лене?', 'Она очень хорошая и нормальная девушка', 1],
    ],
    [
        # 25
        ['Что повелкло вас для принятие такого решения?', 'Она стала что-то употреблять', 0],
        ['Как прошло расстование?', 'Она начала орать всякое', 1],
    ],
    [
        # 26
        ['Вы не пробовали помочь ей?', 'Конечно пробовал, но она меня не слушала', 0],
        ['Можете сказать ещё причину?', 'Нет', 1],
    ],
    [
        # 27 (Основа для конца диалога с парнем)
        ['Хорошо, мы всё поняли, спасибо', 'Уходит...', 0],
        ['Свободны', 'Уходит...', 1],
    ],
    [
        # 28
        ['Во сколько это было?', 'Часов в 8', 0],
        ['Почему вы не остались помочь ей?', 'Она тогда употреблаля что-то', 1],
    ],
    [
        # 29
        ['Вы от неё переехали, почему?', 'Она стала употреблять что-то', 0],
        ['В посленее время были ли у неё координальные изменения в жизни?', 'Да. Походу с катушек слетела.', 1],
    ],
    [
        # 30
        ['Почему вы не поверели ей?', 'Она тогда стала употреблять что-то', 0],
        ['А кто мог предположительно убить её?', 'Да никто не мог', 1],
    ],
    # второе убийство
    [
        # 31 начало связи, соседка загородного дома
        ['Как часто он приезжал сюда?', 'Он приезжал один раз в два месяца, чтобы побыть одному', 0],
        ['Вы с ним хорошо общаетесь? Почему решили заглянуть в дом?', 'В один момент стало тихо и он не выходил. '
                                                                      'Решили постучаться, но квартира была открыта. '
                                                                      'Зашли, а там он.', 1],
    ],
    [
        # 32
        ['В этот всё было как обычно?', 'Нет, в этот раз он приехал раньше, это было странно', 0],
        ['Видели что-то подозрительное?', 'Нет, всё было тихо. Больше ничего такого', 1],
    ],
    [
        # 33
        ['Можете предположить причину?', 'Нет, мы с ним мало общаемся ', 0],
        ['Вы видели кого-то нибудь в тот день?', 'Нет, всё было тихо', 1],
    ],
    [
        # 34 (основа для конца диалога с соседкой загородного дома)
        ['Ладно, мы поняли, спасибо', 'Уходит...', 0],
        ['Отдыхайте', 'Уходит...', 1],
    ],
    [
        # 35
        ['Можете предположить, кто это мог быть?', 'Нет, мы с ним мало общаемся ', 0],
        ['Вы хорошо его знали?', 'Нет, почти не знал. Только вот, что он приезжал один раз в два месяца, '
                                 'чтобы побыть одному', 1],
    ],
    [
        # 36 начало разговора с женой
        ['Вы как жена, скажите, были ли у него враги?', 'Не было, я не могу сказать, кто это мог сделать', 0],
        ['Можете предположить, кто мог такое сделать?', 'Возможно, это сделала та женщина, собака которой не '
                                                        'пережила операции.', 1],
    ],
    [
        # 37
        ['С ним проиходило что-то странное в последние время?', 'То, что он поехал сюда. Обычно он этого не делает.', 0],
        ['Почему он уехал от вас в эти дни?\nКакая причина?', 'Он из дома уехал неожиданно, сказал, что ему нужно '
                                                              'немного времени, это было странно, он никогда себя '
                                                              'так вел.', 1],
    ],
    [
        # 38
        ['Может есть что-то ещё?', 'Еще иногда он волновался часто, а во сне бормотал что-то по типу «это все он...», '
                                   'а кто-он, я не знаю...', 0],
        ['Вы не думали, что это могло быть из-за того случая с собакой', 'Не думаю. Мой муж давно уже пережил эту ситуацию. '
                                                                         'Зачем ему это?', 1],
    ],
    [
        # 39 (основа для конца диалога с женой убитого)
        ['Ладно, мы поняли, спасибо', 'Уходит...', 0],
        ['Отдыхайте', 'Уходит...', 1],
    ],
    [
        # 40
        ['Думаете она могла так сделать?', 'Да, конечно. Она тогда долго обвиняла моего мужа в смерти своей собакой. '
                                           'Может, совсем с ума сошла?.', 0],
        ['Вы не думали, что он сделал это из-за того, что не смог спасти собаку?', 'Мой муж давно уже пережил эту ситуацию, '
                                                                                   'не думаю что именно сейчас он решил сделать это', 1],
    ],
    [
        # 41 начало диалога с хозяйкой мертвой собаки
        ['Где вы находились в этот момент?', 'Я была в стоматологии', 0],
        ['Вы поддерживали с ним общение?', 'Нет, не общаюсь', 1],
    ],
    [
        # 42
        ['Как сможете подтвердить?', 'Запись в стоматологию', 0],
        ['Как вы относитесь к нему, после случившегося?', 'Да, я зла и обвиняю в смерти моей собаки его, '
                                                          'ведь это он не сумел удержать ситуацию под контролем, '
                                                          'но я не буду опускаться до убийства', 1],
    ],
    [
        # 43
        ['Как вы относитесь к нему, после случившегося?', 'Да, я зла и обвиняю в смерти моей собаки его, '
                                                          'ведь это он не сумел удержать ситуацию под контролем, '
                                                          'но я не буду опускаться до убийства', 0],
        ['Вы что нибудь знаете про него или его жизнь?', 'Не особо. Но если возвращаться к моей собаке, '
                                                         'то до меня дошли слухи, что он был под кайфом во время операции', 1],
    ],
    [
        # 44
        ['Думаете он до сих пор употребляет?', 'Думаю нет. Если это правда, то он должен был бросить, т.к. это была большая ошибка', 0],
        ['Верите в эти слухи?', 'Не знаю, верить ли нет...', 1],
    ],
    [
        # 45 (основа для конца диалога с хозяйкой собаки)
        ['Хорошо, мы учтём', 'Уходит...', 0],
        ['Благодарим Вас за помощь', 'Уходит...', 1],
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
