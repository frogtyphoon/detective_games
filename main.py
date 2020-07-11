import config
from s_m import loop_m
from time import sleep
import asyncio
from connect import edit_main
import Bot__journalist

# ВСТУПЛЕНИЕ

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
        sleep(1)

    return int(text[1])


# очистка файла перед запуском
open('text.txt', 'w').close()

# первые сообщения для подготовки. Моделируем ситуацию отсутсвия
loop_m('Чёрт, Паша, ты где пропал?')  # функция, позволяющая отправлять сообщения
loop_m('Уже неделя прошла... Где ты пропадаешь???')
loop_m('Если не отвечаешь через неделю, то ты уволен!')
loop_m('У тебя осталось 24 часа, и если ты будешь продолжать меня игнорить,'
       ' то скоро будешь валаяться в углу и молить о помощи!')

edit_main('Bot__police', 0, 'Отвечай как можно скорей!')

relationships_Bot__police += wait()

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
        sleep(2)
        loop_m('Тебе срочно надо выезжать на "УЛИЦА", ведь всё возможно')
        sleep(1)
        loop_m('Тебе даётся 15 мин, чтобы добраться до точки и просмотреть место происшествия')
        sleep(1)
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

# криминалист
loop_m('Слышал ты снова с нами\nХотел напомнить, чтобы ты не забывал про меня. А то знаю я тебя...\n', None,
       config.TOKEN_CRIMINALIST)

# криминалист (0, 1)
edit_main('Bot__криминалист', 0, 'Я буду помогать тебе с уликами. Отправляй мне все улики, которые найдешь.'
                                 ' Они выглядят примерно так “asdfgq” Я тебе отправлю по ним показания')
relationships_Bot__criminalist += wait()

if relationships_Bot__criminalist == 0:
    edit_main('Bot__криминалист', 1, 'Всё по старой схеме')
    relationships_Bot__criminalist += wait()

# первые новости, bot__journalist
Bot__journalist.news_1()

sleep(20)

# криминалист
loop_m('Сосвем забыл скинуть тебе досье. Держи', None, config.TOKEN_CRIMINALIST)

# если нагрубил, то о времени сообщается позже. примерно 5 мин от времени которое даётся
sleep(10)  # пока 10, должно быть 300сек = 5мин
if time_talk_answer:
    loop_m('Совсем забыл сказать, что мы ограничены по времени и работать нужно как можно быстрее,'
           ' иначе приедут федералы и будет худо\nУ тебя на все дела осталось 10 мин', None, config.TOKEN_POLICE)

# ПЕРВОЕ УБИЙСТВО

count = 0  # подсчёт улик

# считает улики и видёт подсчёт времени
for _ in range(600):  # 600сек = 10 мин
    f = open('text.txt', 'r+', encoding='utf8')
    text = [str(i) for i in f.read().split('|')]
    f.close()
    if text[0] == 'main':
        open('text.txt', 'w').close()
        count += 1
    if count == 5:
        break
    sleep(1)

sleep(10)

# bot__police
loop_m('Походу всё... Пора уходить', None, config.TOKEN_POLICE)

# мини диалог (5)
edit_main('Bot__police', 5, 'Есть какие-то предположения у тебя в голове?')  # отдаём через файл команду полицаю

relationships_Bot__police += wait()  # Ждём ответа

sleep(1)
loop_m('Теперь мы можем опросить свидетелей и друзей, может они нам что-то расскажут?')

sleep(2)
loop_m('У нас времени не совсем много, так что ты сможешь опросить только пару человек')
# bot__police, опрос (6)

for _ in range(2):
    edit_main('Bot__police', 6, 'Кого опрашиваем?')
    count = wait()
    if count == 1:  # диалог - соседка с этажа
        sleep(4)
        edit_main('Bot__admin', 0, 'Здравствуйте, я соседка с Этажа')  # отдаём через файл команду полицаю
        if wait() == 0:  # развязка (1, 2, 3, 4)
            edit_main('Bot__admin', 1, 'Но он к ней часто приходил')
            if wait() == 0: # развязка (2, 3, 4)
                edit_main('Bot__admin', 2, 'Возможно часам к 8.30')
                if wait() == 0:  # развязка (3, 4)
                    edit_main('Bot__admin', 3, ' Через какое-то время я услышла крики')
                    if wait() >= 0:  # тк это независит
                        edit_main('Bot__admin', 4, 'Дальше уже не слышала, ушла')
                else:
                    edit_main('Bot__admin', 4, 'Нет, в этот момент я ушла...')

            else:
                edit_main('Bot__admin', 4, 'Я бы на Вашем месте опросила его и не спускала глаз!')
        # развязка (4, )
        else:
            edit_main('Bot__admin', 121, 'Но я не уверена')

    elif count == 2:  # диалог - сосед этажом ниже
        pass
    elif count == 3:  # диалог - лучшая подруга
        pass
    else:  # диалог - Парень
        pass

# # помощник (знакомство)
# loop_m('Привет, я помощник криминалиста. Хотел сказать, что отправляй мне все улики,'
#        ' которые найдешь. Они выглядят примерно так “asdfgq” Я тебе отправлю по ним показания,'
#        ' а в случаи чего криминалист поможет тебе. Дам подсказку. Он парень добрый, постарайся с'
#        ' ним обращаться хорошо и он сможет давать показаний больше', None, config.TOKEN_HELP)
#
# sleep(2)
#
# # помощник подсказка
# if relationships_Bot__criminalist < 0:
#     loop_m('Дам подсказку. Он парень добрый, постарайся с ним обращаться хорошо и он сможет давать показаний больше.')
