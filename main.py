import config
from s_m import loop_m
import time
import asyncio
from connect import edit_main

# все боты
# import Bot__admin
# import Bot__help
# import Bot__гадалка
import Bot__police as police
# import Bot__журналист
import Bot__криминалист as crime

# Отношения с игроком
relationships_Bot__police, relationships_Bot__criminalist = 0, 0


# обработчик отношений, ждёт изменений в файле
def wait():
    while True:
        f = open('text.txt', 'r+', encoding='utf8')
        text = [str(i) for i in f.read().split('|')]
        f.close()
        if text[0] == 'main':
            open('text.txt', 'w').close()
            break
        time.sleep(1)

    return int(text[1])


# очистка файла перед запуском
open('text.txt', 'w').close()

# первые сообщения для подготовки. Моделируем ситуацию отсутсвия
loop_m('Чёрт, Паша, ты где пропал?')
loop_m('Уже неделя про шла... Где ты пропадаешь???')
loop_m('Если не отвечаешь через неделю, то ты уволен!')
loop_m('У тебя осталось 24 часа и ты не будешь стоять рядом со мной!')

edit_main('Bot__police', 0, 'Отвечай как можно скорей!')

relationships_Bot__police += wait()

print(relationships_Bot__police, relationships_Bot__criminalist)

# при плохих отношениях, майор не скажет о времени, а только потом напомнит ему
time_talk_answer = False

# Первая развязка (1, 2, 3)
if relationships_Bot__police >= 0:
    edit_main('Bot__police', 1, 'Я рад, что ты снова с нами в строю')
    time_relationships = wait()
    relationships_Bot__police += time_relationships
    if time_relationships < 0:
        edit_main('Bot__police', 2, 'Совсем страх потерял?')
        if wait() < 0:
            relationships_Bot__police += -1
            loop_m('Я сейчас на исходе, поэтому бегом на '
                   'место преступления по адресу "УЛИЦА"\nКонец связи')
            time_talk_answer = True
        else:
            relationships_Bot__police += 1
            loop_m('Кратко ввожу в курс дела. Рядом произошёл суицид, сходи да проверь там всё')
            edit_main('Bot__police', 3, 'Чтобы через 15 мин был там, понял?!')
            relationships_Bot__police += wait()
    else:
        loop_m('Тебе срочно надо выезжать "УЛИЦА", ведь убийца не дремлет')
        edit_main('Bot__police', 3, 'Добраться до точки и просмотреть убийтво, тебе даётся 15мин. Уяснил, Павел?')
        relationships_Bot__police += wait()

# Вторая развязка (4)
else:
    edit_main('Bot__police', 4, 'Ещё раз что-то вякнишь, тебе не жить')
    time_relationships = wait()
    relationships_Bot__police += time_relationships
    if time_relationships < 0:
        time_talk_answer = True
        loop_m('Я знаю тебя очень хорошо, и если ты не хочешь, чтобы твоя карьера рухнула'
               ' прямо сейчас, то бегом на место преступления!\n'
               'Вот координаты, сам разберёшься "КОООРДИНАТЫЫ"')
    else:
        loop_m('Значит неподалеку что-то случилось, выдвигайся туда\nУ тебя есть 15 мин. Вот координаты "КООРЛДИНАТЫ"')

# криминалист (0, 1)
loop_m('Слышал ты снова с нами\nХотел напомнить, что ты не забывай про меня. А что знаю я тебя...\n', None,
       config.TOKEN_CRIMINALIST)

edit_main('Bot__криминалист', 0, 'Скидывай мне улики, помогу тебе с ними. Если что,'
                                 ' они выглядят примерно так <b>"qwerty12"</b>')
relationships_Bot__criminalist += wait()

if relationships_Bot__criminalist == 0:
    edit_main('Bot__криминалист', 1, 'Я не удивлён')
    relationships_Bot__criminalist += wait()
    # time_relationships = wait()
    # relationships_Bot__criminalist += time_relationships
    # if time_relationships == -1:
    #     loop_m('мда...')
    # elif time_relationships == 1:
    #     loop_m('спасибо на этом.. Удати там, поторопись')
    # else:
    #     loop_m('Постараюсь')

print(relationships_Bot__criminalist, relationships_Bot__police)