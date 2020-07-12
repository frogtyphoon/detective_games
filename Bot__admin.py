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
    # третье убийство
    [
        # 46 начало разговора с свидетельницей
        ['Вы поняли, почему это произошло?', 'Не совсем, но мне кажется, это не случайная смерть', 0],
        ['Какая была ваша первая реакция?', 'Я увидела, как летит человек с 8 этажа и сразу поняла, что ему не жить. '
                                            'Я естественно перепугалась и вызвала полицию', 1],
    ],
    [
        # 47
        ['Вы видели, кто мог это сделать или можете предположить?', 'Нет, я никого не видела в окне. '
                                                                    'Больше ничего не могу сказать', 0],
        ['Видели, как это произошло?', 'Нет, только уже само падение', 1],
    ],
    [
        # 48 (основа для окончания диалога с свидетельницей)
        ['спасибо за помощь, можете быть свободны', 'Уходит...', 0],
        ['Благодарим за помощь', 'Уходит...', 1],
    ],
    [
        # 49
        ['Вы видели, как она выпала?', 'Нет, я больше ничего не видела и не знаю', 0],
        ['Рядом были её близкие?', 'Вроде, нет. Никто не был, только незнакомцы. Больше я ничего не знаю', 1],
    ],
    [
        # 50 начало разговора с мужем
        ['Куда вы уезжали?', 'Я был в командировке, но уже возвращался, когда мне позвонила полиция', 0],
        ['Вы заметили что-то странное, когда вернулись?', 'Она в тот день решила помыть окна, '
                                                          'раньше она этого не делала и всегда была аккуратной', 1],
    ],
    [
        # 51
        ['Она знала, что Вы приедете?', 'Нет, она не знала, но при этом кого-то ждала... Ничего не знаю', 0],
        ['У вас не было ссор в последние время?', 'Нет, всё было хорошо. Мы любили друг друг. '
                                                  'Это очень сильная потеря для меня...', 1],
    ],
    [
        # 52 (основа для окончания диалога с мужем - 1)
        ['Можете быть свободны', 'Уходит...', 0],
        ['Спасибо за помощь', 'Уходит...', 1],
    ],
    [
        # 53 (основа для окончания диалога с мужем - 2)
        ['Соболезнуем...', 'Уходит...', 0],
        ['Хорошо, можете быть свободны', 'Уходит...', 1],
    ],
    [
        # 54
        ['Можете предположить, почему она это сделала?', 'Возможно она кого-то ждала, но то что вернусь я, она не знала', 0],
        ['Вы живёте одни или с кем-то?', 'Одни, но у нас есть дом.работница, которая как раз и занимается окнами. '
                                         'Но в тот день она не должна была прийти', 1],
    ],
    [
        # 55 начало разговора с подругой
        ['Как вы считаете, могло ли это быть случайностью?', 'Не, не. Однозначно нет. Она живёт аккуратной жизнью. '
                                                             'Я вообще удивлена что она полезла мыть окна, '
                                                             'так что это точно подстава от своих', 0],
        ['Она в тот день ждала кого-то?', 'Не знаю, бро. Она не была из тех, кто любил тусить или тем более изменять.', 1],
    ],
    [
        # 56
        ['Можете сказать, кто это мог сделать?', 'Не, бро. У неё врагов вообще не было. Говорю, девчёнка аккуратная, '
                                                 'но она стала покупать какие-то препараты и говорила, '
                                                 'что если скажет где покупает, она будет мертва', 0],
        ['С ней происходило что-то странное в эти дни?', 'Не совсем, но да. Она стала очень сильно уставать,. '
                                                         'Говорила, что это из-за своей дурацкой работы. '
                                                         'Такая вот она рабочая', 1],
    ],
    [
        # 57
        ['То есть она вам так и не сказала?', 'Нет. Она слово закон, на неё можно положиться', 0],
        ['Какие препараты?', 'Допинг. Обычный допинг. Ничего такого, обычное дело понимаешь', 1],
    ],
    [
        # 58 (окончание диалога с подругой)
        ['Можете быть свободны', 'Уходит...', 0],
        ['Спасибо, идите', 'Уходит...', 1],
    ],
    [
        # 59
        ['Вы знаете где она работала?', 'Не, я не интересовалась', 0],
        ['И как она решила эту проблему?', 'Думаете она стала меньше работать? неее. Она ещё та. '
                                           'Решила покупать допинги и сидела на них. Всё. Я конечно хотела узнать, '
                                           'где она берёт эту дрянь, но так и не узнала', 1],
    ],
    [
        # 60
        ['Как она проводила свободное время?', 'Никак, просто никак. Она не отдыхала. Больше я ничего не знаю', 0],
        ['С кем она дружит?', 'Я ничего не знаю, она меня ни с кем не знакомила, кроме мужа. Больше не знаю', 1],
    ],
    [
        # 61 начало расговора с подозреваемым
        ['Мы вас задержали по подозрению в убийстве 3х человек', 'Я никого не убивал!', 0],
        ['Где вы были 07.07.2020 в 09:00?\nА  07.07.2020 в 11:30 или 07.07.2020 в 14:00?\nГде вы были?',
         'У меня нет алиби, это правда. И то, что я был мелким дилером, тоже. Но я никого не убивал', 1],
    ],
    [
        # 62
        ['Докажите', 'У меня нет алиби, это правда. И то, что я был мелким дилером, тоже. Но я никого не убивал', 0],
        ['Вы задержаны по подозрению в трёх убийствах, и будете находиться в камере до выяснения всех деталей', 'Его уводят...', 1],
    ],
    [
        # 63 (окончание диалога с подозреваемым)
        ['Вы задержаны по подозрению в трёх убийствах, и будете находиться в камере до выяснения всех деталей', 'Его уводят...', 0],
        ['Это ничего не объясняет! Вы задержаны', 'Его уводят...', 1],
    ],
    # четвертое убийство
    [
        # 64 начало диалога с тетей
        ['Вы замечали что-то странное за ней?', 'Замечала за ней пару раз странное поведение, но особо не придавала этому значения', 0],
        ['Она употребляет?', 'Нет. Я никогда не видела и не замечала. Я знала о том, что она далеко не пай-девочка, '
                             'но не могла ей ничего запрещать, она ведь уже далеко не маленькая девочка', 1],
    ],
    [
        # 65
        ['Какое именно?', 'Ну... Я знала о том, что она далеко не пай-девочка, но не могла ей ничего запрещать, '
                          'она ведь уже далеко не маленькая девочка. Больше ничего такого', 0],
        ['Можете рассказать что-нибудь ещё?', 'Знаю, что она не была в отношениях...Друзей не так много... Всё, больше не знаю', 1],
    ],
    [
        # 66 (окончание диалога с тетей и лучшей подругой)
        ['Спасибо за помощь', 'Уходит...', 0],
        ['Можете быть свободны', 'Уходит...', 1],
    ],
    [
        # 67
        ['У неё есть враги?', 'Знаю, что она не была в отношениях...Друзей не так много... Всё, больше не знаю', 0],
        ['Можете рассказать, что с ней происходило странного в последее время?', 'Замечала за ней пару раз странное поведение, '
                                                                                 'но особо не придавала этому значения.. '
                                                                                 'Больше ничего', 1],
    ],
    [
        # 68
        ['Вы как лучшая подруга, можете сказать, какая на самом деле Ваша подруга?', 'Она оторва, хотя отличница и '
                                                                                     'Всегда кажется так миленькой. '
                                                                                     'Вот постоянно отшивает парней', 0],
        ['Что-то странно проиходило в посленее время?', 'Она не любила парней, но в последенее время стала тесно общаться с кем-то', 1],
    ],
    [
        # 69
        ['Почему она это делает?', 'Да не знаю... Хотя красивы парней было много. Больше ничего не знаю', 0],
        ['Не могла найти любовь?', 'Да кто её знает.  Но где-то с полгода назад она начала тесно с кем-то общаться', 1],
    ],
    [
        # 70
        ['Знаете кто это?', 'Нет, не знаю, но как-то я видела его мельком из машины, один раз. '
                            'Скажу точно, он мне не понравился, лицо его. Не доброе оно', 0],
        ['Можете рассказать подробности?', 'Он её подвозил и забирал откуда ей надо было. Она говорила, что у них выгодное сотрудничество, '
                                           'Она что-то дает ему, а он что-то ей. Особо о нём она не говорила, и тем более не показывала', 1],
    ],
    [
        # 71
        ['Вы знаете, почему она решила так сделать?', 'Не всё знаю, но он её подвозил и забирал откуда ей надо было. '
                                                      'Она говорила, что у них выгодное сотрудничество, она что-то дает ему, а он что-то ей. '
                                                      'Особо о нём она не говорила, и тем более не показывала. А катался на тонированой машине', 0],
        ['Есть что-то ещё?', 'Нет, особо больше ничего. Хотя парня я этого видела как-то. Вид у него не добрый', 1],
    ],
    [
        # 72 начало разговора с свидетельницей
        ['Что произошло? как она упала?', 'Я шла за ней около пяти минут как минимум, нам в одну сторону надо было, она что-то приняла, '
                                          'а потом стала немного шататься, затем и вовсе упала. Больше я ничего не знаю... Это было быстро', 0],
        ['Что вы сделали, когда это увидели?', 'Я испугалась, подбежала, а у неё судороги, и она задыхается. Похоже было на асфиксию. '
                                               'Тут же позвонила в скорую. Больше я ничего не знаю', 1],
    ],
    [
        # 73 (основа для окончания диалога с свидетельницей)
        ['Хорошо, мы понимаем, спасибо', 'Уходит...', 0],
        ['Спасибо, до свидания', 'Уходит...', 1],
    ],
    [
        # 74 начало диалога с невестой
        ['Где вы были в вечер?', 'Я была у подруги. Вернулась домой, зашла, а там лежит он… Меня охватила паника, ужас, шок!', 0],
        ['Было с ним что-то странное в последние время?', 'Нет, ничего такого. Всё как обычно', 1],
    ],
    [
        # 75
        ['Он мог перепутать дозу?', 'Это невозможно, он относился к этому с полной ответственностью. '
                                    'Всегда был абсолютно адекватен, я..я не знаю, что могло произойти и что он мог принимать, '
                                    'как мог спутать дозы…»', 0],
        ['Он мог пропускать приёмы врача?', 'Нет, он никогда не пропускал приём инсулина, и тем более, не могу случайно спутать дозы. '
                                            'Он очень ответственный человек', 1],
    ],
    [
        # 76 (основа окончания диалога с невестой)
        ['Мы вам соболезнуем, можете идти', 'Уходит...', 0],
        ['Мы выясним правду, идите', 'Уходит...', 1],
    ],
    [
        # 77 начало диалога с лучшим другом
        ['Было что-то подозрительное в последне время?', 'Да. В последнее время он стал более скрытный, говорил, что переживает за Киру, '
                                                         'да и за свою жизнь. Но толком ничего не сказал... Это всё пожалуй', 0],
        ['Он употребляет?', 'Да, по приколу пару раз употребляли, но мы лишь баловались, при этом всегда доставал дозу он', 1],
    ],
    [
        # 77
        ['Он серьёзно относился к лекарствам? Не пропускал приём?', 'Ещё как! Всегда был в себе и никогда не пропускал. '
                                                                    'Он очень ответственный ', 0],
        ['Он вам всё рассказывает?', 'Вообще да, но парой может что-то утаить', 1],
    ],
    [
        # 77 (основа окончания диалога с лучшим другом)
        ['Хорошо, спасибо', 'Уходит...', 0],
        ['Спасибо за вашу помощь, можете быть свободны', 'Уходит...', 1],
    ],
    [
        # 77
        ['Сколько раз вы пробовали?', 'Только пару раз. Нам это не собо понравилось', 0],
        ['Вы до сих пор это делаете?', 'Мы вот пару раз попрбовали и всё, забыли. Та ещё дрянь', 1],
    ],
    [
        # 77 начало разговора с отцом
        ['Насколько сильны были ваши отношения?', 'Да. Я с ним был ближе чем мать', 0],
        ['Вы замечали что-то странное?', 'Я спросил, как у него дела, он нервно отмахнулся, стал заикаться. '
                                         'Это показалось странным и даже подозрительным', 1],
    ],
    [
        # 77
        ['Каким он был?', 'Он всегда был не то, чтобы правильным, но и границы не переходил. Также отвесным и серьёзным', 0],
        ['Вы недавно куда-то ездили. Куда?', 'Мы недавно ездили с ним на рыбалку', 1], # шо за херня?
    ],
    [
        # 77 (основа для окончания диалога с отцом)
        ['Мы рады, что вы нам помогли', 'Уходит...', 0],
        ['Спасибо , вы свободны', 'Уходит...', 1],
    ],
    [
        # 77
        ['Вы пытались узнать, что с ним?', 'Нет, больше я стал не спрашивать, да и он не говорил ничего', 0],
        ['Каким он был?', 'Он всегда был не то, чтобы правильным, но и границы не переходил. Также отвесным и серьёзным', 1],
    ],
    [
        # 77
        ['Произошло что-то странное?', 'Я спросил, как у него дела, он нервно отмахнулся, стал заикаться. '
                                       'Это показалось странным и даже подозрительным', 0],
        ['Вы пытались узнать, что с ним?', 'Нет, больше я стал не спрашивать, да и он не говорил ничего', 1],
    ]

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
