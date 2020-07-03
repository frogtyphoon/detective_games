import config
from s_m import loop_m
import time
import asyncio
from connect import edit_main

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
loop_m('Уже неделя прошла... Где ты пропадаешь???')
loop_m('Если не отвечаешь через неделю, то ты уволен!')
loop_m('У тебя осталось 24 часа, и если ты будешь продолжать меня игнорить,'
       ' то скоро будешь валаяться в углу и молить о помощи!')

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
            edit_main('Bot__police', 3, 'Чтобы через 15 мин был там, ок?!')
            relationships_Bot__police += wait()
    else:
        loop_m('У нас неподалеку совершилось самоубийство. Тебе стоит выехать и разобраться.'
               ' Возможно, здесь что-то не чисто. Это серьёзное дело, будь готов ко всему')
        loop_m('Тебе срочно надо выезжать на "УЛИЦА", ведь убийца не дремлет')
        loop_m('ТТебе даётся 15 мин, чтобы добраться до точки и просмотреть место происшествиея')
        edit_main('Bot__police', 3, 'Всё уяснил, Павел?')
        relationships_Bot__police += wait()

# Вторая развязка (4)
else:
    edit_main('Bot__police', 4, 'Лучше бы заткнулся и послушал меня, пока не стало хуже!')
    time_relationships = wait()
    relationships_Bot__police += time_relationships
    if time_relationships < 0:
        time_talk_answer = True
        loop_m('Я сейчас на пределе, и если ты хочешь обсудить это, то лучше перенести это\n'
               'А сейчас выдвигайся на место происшествие и как можно скорее. '
               'Вот координаты, сам разберёшься "КОООРДИНАТЫЫ"')
    else:
        loop_m('Значит неподалеку что-то случилось, выдвигайся туда\nУ тебя есть 15 мин. Вот координаты "КООРЛДИНАТЫ"')

# криминалист (0, 1)
loop_m('Слышал ты снова с нами\nХотел напомнить, чтобы ты не забывал про меня. А то знаю я тебя...\n', None,
       config.TOKEN_CRIMINALIST)

edit_main('Bot__криминалист', 0, 'Я буду помогать тебе с уликами. Точнее рассказывать больше про их историю,'
                                 ' а сами улики будешь скидывать моему помощнику, он в скором времени тебе напишет')
relationships_Bot__criminalist += wait()

if relationships_Bot__criminalist == 0:
    edit_main('Bot__криминалист', 1, 'Всё по старой схеме')
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