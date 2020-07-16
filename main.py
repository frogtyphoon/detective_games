import config
from s_m import loop_m, loop_m_photo, loop_m_admin
from time import sleep
from connect import edit_main
import Bot__journalist

# ВСТУПЛЕНИЕ

# Отношения с игроком
relationships_Bot__police, relationships_Bot__criminalist = 0, 0

# подозреваемые
suspect = []


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

loop_m_admin('ИГРА НАЧАЛАСЬ')


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
                   'место преступления в парк имени 400-летия на десткую площадку"\nКонец связи')
            time_talk_answer = True
        else:
            relationships_Bot__police += 1
            loop_m('Кратко ввожу в курс дела. Рядом произошёл суицид, сходи да проверь там всё')
            edit_main('Bot__police', 3, 'Чтобы через 20 мин был там, ок?!')
            relationships_Bot__police += wait()
    else:
        loop_m('У нас неподалеку совершилось самоубийство. Тебе стоит выехать и разобраться.'
               ' Возможно, здесь что-то не чисто. Это серьёзное дело, будь готов ко всему')
        sleep(2)
        loop_m('Тебе срочно надо выезжать в парк имени 400-летия на десткую площадку, ведь всё возможно')
        sleep(1)
        loop_m('Тебе даётся 20 мин, чтобы добраться до точки и просмотреть место происшествия')
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
               'Вот координаты, сам разберёшься "56.040239, 92.920635"')
    else:
        loop_m('Значит неподалеку что-то случилось, выдвигайся туда\nУ тебя есть 20 мин. Вот координаты'
               ' "56.040239, 92.920635"')

# криминалист
loop_m('Слышал, ты снова с нами\nХотел напомнить, чтобы ты не забывал про меня. А то знаю я тебя...\n', None,
       config.TOKEN_CRIMINALIST)

# криминалист (0, 1)
edit_main('Bot__криминалист', 0, 'Я буду помогать тебе с уликами. Отправляй мне все улики, которые найдешь.'
                                 ' Они выглядят примерно так “asdfgq” Я тебе отправлю по ним показания.'
                                 ' Отправляй через "/"')
relationships_Bot__criminalist += wait()

if relationships_Bot__criminalist == 0:
    edit_main('Bot__криминалист', 1, 'Всё по старой схеме')
    relationships_Bot__criminalist += wait()

# первые новости, bot__journalist
Bot__journalist.news_1()

sleep(20)

# криминалист, Досье
loop_m('Сосвем забыл скинуть тебе досье. Держи', None, config.TOKEN_CRIMINALIST)
loop_m_photo('AgACAgIAAxkDAAIBcV8QPvYaD3u0_ZPyt8w3VdCwOqX1AAJkrjEbPNiBSCta4itSNvIxZJvfky4AAwEAAwIAA20AA2bKAgABGgQ')


# если нагрубил, то о времени сообщается позже. примерно 5 мин от времени которое даётся
sleep(300)  # должно быть 300сек = 5мин
if time_talk_answer:
    loop_m('Совсем забыл сказать, что мы ограничены по времени и работать нужно как можно быстрее,'
           ' иначе приедут федералы и будет худо\nУ тебя на все дела осталось 20 мин', None, config.TOKEN_POLICE)


# ПЕРВОЕ УБИЙСТВО
# оповещение для админа
loop_m_admin('Начинается первое убийство')

count = 0  # подсчёт улик

# считает улики и видёт подсчёт времени
for i in range(900):  # 900сек = 15 мин
    if i == 900 or i == 600 or i == 300 or i == 60:  # оповещение для админа
        loop_m_admin(str(i / 60) + 'мин')
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
    count = wait()  # выбираем кого опрашиваем

    # диалоги с подозреваемыми
    if count == 1:  # диалог - соседка с этажа (0 - 9)
        sleep(4)
        edit_main('Bot__admin', 0, 'Здравствуйте, я соседка с Этажа')  # отдаём через файл команду переговорной

        if wait() == 0:  # развязка (1, 2, 3, 4)
            edit_main('Bot__admin', 1, 'Но он к ней часто приходил')
            if wait() == 0:  # развязка (2, 3, 4)
                edit_main('Bot__admin', 2, 'Возможно часам к 8.30')
                if wait() == 0:  # развязка (3, 4)
                    edit_main('Bot__admin', 3, 'Через какое-то время я услышала крики')
                    wait()
                    edit_main('Bot__admin', 4, 'Дальше уже не слышала, ушла')
                    wait()
                else:
                    edit_main('Bot__admin', 4, 'Нет, в этот момент я ушла...')
                    wait()
            else:
                edit_main('Bot__admin', 4, 'Я бы на Вашем месте опросила его и не спускала глаз!')
                wait()
        # развязка (4, 5, 6, 7, 8, 9)
        else:
            edit_main('Bot__admin', 5, 'Но я не уверена')
            if wait() == 0:  # развязка (4, 6, 7)
                edit_main('Bot__admin', 6, 'Она кричала на кого-то, что не любит его, но я не уверена')
                if wait() == 0:  # развязка (4, 7)
                    edit_main('Bot__admin', 7, 'Я с ней мало знакома')
                    if wait() == 0:  # развязка (4)
                        edit_main('Bot__admin', 4, 'В этот момент я ушла...')
                        wait()
                else:
                    edit_main('Bot__admin', 4, 'В этот момент я ушла...')
                    wait()
            else:  # развязка (4, 8, 9)
                edit_main('Bot__admin', 8, 'Мне кажется, тогда она сильно ссорилась со своим парнем')
                if wait() == 0:  # развязка (4, 9)
                    edit_main('Bot__admin', 9, 'и «мне страшно одной, вдруг он придет.»')
                    if wait() == 0:
                        edit_main('Bot__admin', 4, 'Я в этот момент ушла')
                        wait()
                    else:
                        edit_main('Bot__admin', 4, 'На вашем бы месте я бы его только и проверила')
                        wait()
                else:
                    edit_main('Bot__admin', 4, 'Не знаю')
                    wait()

    elif count == 2:  # диалог - сосед этажом ниже (10 - 16)
        sleep(3)
        edit_main('Bot__admin', 10, 'Здравствуйте, я сосед проживающий этажом ниже')  # отдаём через файл команду

        if wait() == 0:  # развязка (11, 12, 13 )
            edit_main('Bot__admin', 11, 'Она мне никогда не нравилась')  # отдаём через файл команду
            if wait() == 0:   # развязка (12)
                edit_main('Bot__admin', 12, 'Однажды видел её накаченной наркотой')
                wait()
            else:   # развязка (12, 13 )
                edit_main('Bot__admin', 13, 'Иногда оры стоят в квартире и подобное')
                if wait() == 0:
                    edit_main('Bot__admin', 12, 'Оры стояли на весь этаж!')
                    wait()
                else:
                    edit_main('Bot__admin', 12, 'Больше ничего не знаю')
                    wait()
        else:  # развязка (12, 14, 15, 16)
            edit_main('Bot__admin', 14, 'Стояли сильные оры на всём этаже')
            if wait() == 0:  # развязка (12, 15)
                edit_main('Bot__admin', 15, 'Кричала плохие слова кому-то')
                if wait() == 0:
                    edit_main('Bot__admin', 12, 'Больше ничего скзаать не могу')
                    wait()
                else:
                    edit_main('Bot__admin', 12, 'Однажды она была под наркотой, может быть из-за этого')
                    wait()
            else:  # развязка (12, 16)
                edit_main('Bot__admin', 16, 'Точно, точно')
                if wait() == 0:
                    edit_main('Bot__admin', 12, 'Но вроде он ушёл от неё часов в 8')
                    wait()
                else:
                    edit_main('Bot__admin', 12, 'Это не точно, слух у меня плохой')
                    wait()

    elif count == 3:  # диалог - лучшая подруга (17 - 23)
        sleep(3)
        edit_main('Bot__admin', 17, 'Доброе утро,  я её лучшая подруга Алина')
        if wait() == 0:  # развязка (18, 19, 20)
            edit_main('Bot__admin', 18, 'Она изменилась')
            if wait() == 0:
                edit_main('Bot__admin', 19, 'С синяками под глазами и сильно похудела. Будто сильно заболела')
                wait()
            else:  # развязка (19, 20)
                edit_main('Bot__admin', 20, 'Не знаю...')
                if wait() == 0:
                    edit_main('Bot__admin', 19, 'Но врагов у неё не было')
                    wait()
                else:
                    edit_main('Bot__admin', 19, 'Но я спрашивала у неё, что с ней, но она говорила всё окей')
                    wait()

        else:  # развязка (19, 21, 22, 23)
            edit_main('Bot__admin', 21, 'Но в какой-то момент у неё были прорблемы с парнем')
            if wait() == 0:  # развязка (19, 22)
                edit_main('Bot__admin', 22, 'И очень сильно')
                if wait() == 0:
                    edit_main('Bot__admin', 19, 'Не знаю')
                    wait()
                else:
                    edit_main('Bot__admin', 19, 'Вполне это мог быть и он...')
                    wait()
            else:   # развязка (19, 23)
                edit_main('Bot__admin', 23, 'Также говорила, что она кого-то боиться, и он хочет убить её')
                if wait() == 0:
                    edit_main('Bot__admin', 19, 'У них всё было хорошо...')
                    wait()
                else:
                    edit_main('Bot__admin', 19, 'Она мало с кем контактировала')
                    wait()

    else:  # диалог - Парень (24)
        sleep(4)
        edit_main('Bot__admin', 24, 'Добрый день, детектив. Я парень Лены, Олег')
        if wait() == 0:
            edit_main('Bot__admin', 25, 'И мне пришлось растаться с ней')
            if wait() == 0:
                edit_main('Bot__admin', 26, 'Но я так и не узнал, что')
                if wait() == 0:
                    edit_main('Bot__admin', 27, 'Я устал и ушёл')
                    wait()
                else:
                    edit_main('Bot__admin', 27, 'Только это')
                    wait()

            else:
                edit_main('Bot__admin', 28, 'Потом сказала, что ей страшно одной, ведь он её убьет')
                if wait() == 0:
                    edit_main('Bot__admin', 27, 'Где-то так')
                    wait()
                else:
                    edit_main('Bot__admin', 27, 'Поэтому не хотел')
                    wait()

        else:
            edit_main('Bot__admin', 29, 'Всегда любил её')
            if wait() == 0:
                edit_main('Bot__admin', 27, 'Мне это не понравилось')
                wait()
            else:
                edit_main('Bot__admin', 30, 'Говорила мне, что кто-то хочет её убить, хах')
                if wait() == 0:
                    edit_main('Bot__admin', 27, 'Поэтому и не поверил')
                    wait()
                else:
                    edit_main('Bot__admin', 27, ' У неё не было врагов')
                    wait()

sleep(3)

# выбор подзреваемого
loop_m('Мы узнали много нового и перед нами есть пару подозрительных личностей. '
       'Это парень и подруга. Тебе стоит сделать выбор, кого задержать')
edit_main('Bot__police', 7, 'Если сделаешь неправильный выбор, это может сказаться на расследовнии')

# подсказка при хороших отношениях с криминалистом
if relationships_Bot__criminalist > 0:
    sleep(2)
    loop_m('Просмотрев место происшествия ещё раз, мы обнаружили улику.'
           ' Под ногтями есть кожный эпителий неизвестного мужчины..'
           ' Возможно это что-то значит', None, config.TOKEN_CRIMINALIST)

if wait() == 0:
    sleep(3)
    loop_m('Парень задержан\nЕго Алиби - "Я пришел к ней в восьмом часу, может, в 7:10. Ушел от нее в 7:40.'
           '  Я не убивал ее, я ее любил, несмотря вообще ни на что!" Вам решать, врёт он или нет, но проверить '
           'мы сможем его только потом', None, config.TOKEN_POLICE)
    suspect.append('Парень')
else:
    sleep(3)
    loop_m('Подруга задержана\nЕё Алиби - "Я виделась с ней вчера вечером, все было хорошо. В 9 утра я была на другом'
           ' конце города, в универе сдавала долги, можете спросить преподавателя по математике" Вам решать,'
           ' врёт она или нет, но сообщить правду мы смоежм только позже', None, config.TOKEN_POLICE)
    suspect.append('Подруга, Алина')

# сообщения о новом убийстве
loop_m_admin('Начинается второе убийство')

sleep(6)
loop_m('Так, сейчас нам сообщили о новом происшествие')
sleep(3)
loop_m('Убит мужчина, 40 лет. Тело найдено в загородном доме района Н. Предположительна причина смерти: самоубийство, '
       'застрелился, пуля прошла навылет с правой стороны висков')
sleep(1)
edit_main('Bot__police', 8, 'Время смерти: 07.07.2020, 11:30')

time_relationships = wait()
relationships_Bot__police += time_relationships

if time_relationships == -1:
    edit_main('Bot__police', 9, 'Второе убийство не может быть хорошим...')
    relationships_Bot__police += wait()


sleep(300)  # перед отправкой досье, 300cек = 5мин
loop_m('Досье готово, Держи', None, config.TOKEN_CRIMINALIST)
loop_m_photo('AgACAgIAAxkDAAIBcl8QPvfIUXWjneqA4r78pJjMLBdBAAJlrjEbPNiBSDGYrVxwYlWZ5k71lC4AAwEAAwIAA3kAA')

sleep(180)  # перед отправкой новостей, 180сек = 3 мин
# Вторые новости, bot__journalist
Bot__journalist.news_2()


# ВТОРОЕ УБИЙСВТО

count = 0  # подсчёт улик

# считает улики и видёт подсчёт времени
for i in range(900):  # 900сек = 15 мин
    if i == 900 or i == 600 or i == 300 or i == 60:  # оповещение для админа
        loop_m_admin(str(i / 60) + 'мин')
    f = open('text.txt', 'r+', encoding='utf8')
    text = [str(i) for i in f.read().split('|')]
    f.close()
    if text[0] == 'main':
        open('text.txt', 'w').close()
        count += 1
    if count == 5:
        break
    sleep(1)

sleep(15)

# переход к подозреваемым
loop_m('К нам уже приближаются, пора уходить', None, config.TOKEN_POLICE)
sleep(5)
loop_m('Теперь пришло время опросить свидетелей и знакомых. Времени у нас также немного,'
       ' поэтому давай быстрее, кого успеешь опросить')


# разговор с подозреваемыми
for _ in range(2):
    edit_main('Bot__police', 10, 'Выбирай, кого вызвать')  # отдаём через файл команду полицаю
    count = wait()  # выбираем кого опрашиваем

    # диалоги с подозреваемыми
    if count == 1:  # диалог - соседка загородного дома (31 - 35)
        edit_main('Bot__admin', 31, 'Добрый день, я соседка живущая напротив')
        if wait() == 0:  # (32, 33, 34)
            edit_main('Bot__admin', 32, 'Вроде чтобы побыть одному')
            if wait() == 0:
                edit_main('Bot__admin', 33, 'это было странно')
                if wait() == 0:
                    edit_main('Bot__admin', 34, 'Мы с ним мало общаемся')
                    wait()
                else:
                    edit_main('Bot__admin', 34, 'всё было тихо')
                    wait()
            else:
                edit_main('Bot__admin', 34, 'Больше ничего такого')
                wait()
        else:   # (34, 35)
            edit_main('Bot__admin', 35, 'Решили постучаться, но квартира была открыта. Зашли, а там он')
            if wait() == 0:
                edit_main('Bot__admin', 34, 'Мы с ним мало общаемся')
                wait()
            else:
                edit_main('Bot__admin', 34, ' Только вот, что он приезжал один раз в два месяца, чтобы побыть одному')
                wait()

    elif count == 2:  # диалог - Жена (36 - 40)
        edit_main('Bot__admin', 36, 'Здравствуйте. Я Алёна, жена Арсения')
        if wait() == 0:
            edit_main('Bot__admin', 37, 'Я не могу сказать, кто это мог сделать')
            if wait() == 0:
                edit_main('Bot__admin', 38, 'Обычно он этого не делает')
                if wait() == 0:
                    edit_main('Bot__admin', 39, 'По типу «это все он...», а кто-он, я не знаю...')
                    wait()
                else:
                    edit_main('Bot__admin', 39, 'Зачем ему это?')
                    wait()
            else:
                edit_main('Bot__admin', 39, 'Это было странно, он никогда себя так вел.')
                wait()
        else:
            edit_main('Bot__admin', 40, 'Ужас...')
            if wait() == 0:
                edit_main('Bot__admin', 39, 'Может, совсем с ума сошла?')
                wait()
            else:
                edit_main('Bot__admin', 39, 'Не думаю что именно сечас он решил сделать это')
                wait()

    else:  # диалог - Хозяйка мертвой собаки, жертва неудачной операции (41 - 45)
        edit_main('Bot__admin', 41, 'Привет. Я хозяйка той самой мертвой собаки')
        if wait() == 0:
            edit_main('Bot__admin', 42, 'Да..Точно')
            if wait() == 0:
                edit_main('Bot__admin', 45, 'И только')
                wait()
            else:
                edit_main('Bot__admin', 45, 'Но я не буду опускаться до убийства')
                wait()

        else:
            edit_main('Bot__admin', 43, 'Не общаюсь')
            if wait() == 0:
                edit_main('Bot__admin', 45, 'Но я не буду опускаться до убийства')
                wait()
            else:
                edit_main('Bot__admin', 44, 'Но если возврощаться к моей собаке, то до меня дошли слухи,'
                                            ' что он был под кайфом во время операции')
                if wait() == 0:
                    edit_main('Bot__admin', 45, 'т.к. это была большая ошибка')
                    wait()
                else:
                    edit_main('Bot__admin', 45, 'Верить ли...')
                    wait()

sleep(3)

# выбор подозреваемого
loop_m('Я думаю тут есть  пара подозритекльных личностей.  Жена и Хозяйка собаки')
edit_main('Bot__police', 11, 'Что думаешь, кто из них?')  # отдаём через файл команду полицаю

if wait() == 0:
    loop_m('Хм... Хорошо\nЕё алиби:  В это время я была на кладбище, мне было тяжело, я волновалась, поэтому'
           ' пошла на могилу матери. Я всегда там бываю, когда мне плохо. И вообще, как вы смеете меня подозревать?'
           ' Я любила его, а вовсе не желала ему смерти!»')

else:
    loop_m('Я тоже так считаю\nЕё алиби: Я была на приёме у стоматолога, с 10:40 до 11:50 включительно.»')

    sleep(4)
    # диалог с криминалистом, если отношения >= -1 (2 - )
    if relationships_Bot__criminalist >= -1:
        edit_main('Bot__криминалист', 2, 'Почему ты решил выбрать её?')
        time_relationships = wait()
        relationships_Bot__criminalist += time_relationships
        if time_relationships == 0:  # (3, 4, 5, 6)
            edit_main('Bot__криминалист', 3, 'Чем именно?')
            time_relationships = wait()
            if time_relationships == 1:
                edit_main('Bot__криминалист', 4, 'Хочу узнать, почему ты выбрал её')
                time_relationships = wait()
                if time_relationships == 1:
                    edit_main('Bot__криминалист', 5, 'Мне показалось, что такая женщина и не может врать. Она знает'
                                                     ', что дело серьёзное и как-бы она не было зла на него, она не '
                                                     'врала бы')
                    time_relationships = wait()
                    relationships_Bot__criminalist += time_relationships
                    if time_relationships == 0:
                        edit_main('Bot__криминалист', 6, 'Но она наговорила за чем-то на эту женщину. Возможно из-за'
                                                         ' страха, но выглядело это как отвод подозрения')
                        relationships_Bot__criminalist += wait()

                elif time_relationships == 2:
                    edit_main('Bot__криминалист', 5, 'Нам важны любые данные. Не думаю, что она это сделала для себя, '
                                                     'а не для нас. Как по мне, муж более подозрительный')
                    time_relationships = wait()
                    relationships_Bot__criminalist += time_relationships
                    if time_relationships == 0:
                        edit_main('Bot__криминалист', 6, 'Но она наговорила за чем-то на эту женщину. Возможно из-за'
                                                         ' страха, но выглядело это как отвод подозрения')
                        relationships_Bot__criminalist += wait()
                elif time_relationships == 3:
                    edit_main('Bot__криминалист', 6, 'На твоём бы месте я поменял подозреваемого')
                    relationships_Bot__criminalist += wait()

                else:
                    loop_m('Я бы на твоём месте поменял мнение', None, config.TOKEN_CRIMINALIST)

            elif time_relationships == 2:
                loop_m('Мне показалось, что такая женщина и не может врать. Она знает, что дело серьёзное и как-бы'
                       ' она не было зла на него, она не врала бы', None, config.TOKEN_CRIMINALIST)
            elif time_relationships == 3:
                loop_m('Нам важны любые данные. Не думаю, что она это сделала для себя, а не для нас', None,
                       config.TOKEN_CRIMINALIST)
            else:
                relationships_Bot__criminalist += -1
                loop_m('Я хотел только помочь... Мне кажется это не она и всё... Ладно')
        elif time_relationships == 1:
            edit_main('Bot__криминалист', 7, 'Только интуиция?')
            time_relationships = wait()
            relationships_Bot__criminalist += time_relationships
            if time_relationships == 1:
                edit_main('Bot__криминалист', 8, 'Я конечно не эксперт и тд, но подумай ещё раз')
                time_relationships += wait()

    sleep(20)

    # мини диалог (12, 13, 14)
    edit_main('Bot__police', 12, 'Мне тут сообщили, что ты сомвневался в своём выборе. Желаешь его поменять?')
    time_relationships = wait()
    relationships_Bot__criminalist += time_relationships
    if time_relationships == 0:
        edit_main('Bot__police', 13, '???')
        time_relationships = wait()
        if time_relationships == 1:
            edit_main('Bot__police', 14, 'Но выбор за тобой')
            relationships_Bot__police += wait()
            time_relationships = wait()
            if time_relationships == -1:
                suspect.append("Жена")
                relationships_Bot__police += time_relationships
            else:
                suspect.append('Хозяйка собаки')
                relationships_Bot__police += time_relationships
        elif time_relationships == 2:
            suspect.append('Жена')
        else:
            suspect.append('Хозяйка собаки')
    else:
        suspect.append('Хозяйка собаки')

# сообщения о новом убийстве
loop_m_admin('Началось третье убийство')

sleep(7)
loop_m('Сообщаю о новом убийстве', None, config.TOKEN_POLICE)
sleep(5)
loop_m('Убита женщина 39 лет, тело найдено возле дома, в районе Батурина Предположительная причина смерти:'
       ' случайно выпала из окна во время мойки окна. Перелом 80% костей, травмы, несовместимые с жизнью.')
sleep(2)
loop_m('Время смерти: 07.07.2020, 14:00')
sleep(4)
loop_m('Без вяских разговоров выдвигайся по адресу улица Батурина, 15. У нас не так много времени, всего 15 мин')

sleep(180)  # 3мин = 180сек
loop_m('Готово, я сделал для тебя досье', None, config.TOKEN_CRIMINALIST)
loop_m_photo('AgACAgIAAxkDAAIBc18QPvf3QXgY7CHgfaCLfWvzvXfgAAJmrjEbPNiBSIrzaHZbLVRcLP7ski4AAwEAAwIAA3kAAzHXAwABGgQ')

# новости 3
sleep(300)  # 5мин = 300сек
Bot__journalist.news_3()


# ТРЕТЬЕ УБИЙСТВО

count = 0  # подсчёт улик

# считает улики и видёт подсчёт времени
for i in range(900):  # 900сек = 15 мин
    if i == 900 or i == 600 or i == 300 or i == 60:  # оповещение для админа
        loop_m_admin(str(i / 60) + 'мин')

    f = open('text.txt', 'r+', encoding='utf8')
    text = [str(i) for i in f.read().split('|')]
    f.close()
    if text[0] == 'main':
        open('text.txt', 'w').close()
        count += 1
    if count == 5:
        break
    sleep(1)

sleep(15)

# переход к подозреваемым
loop_m('Федералы уже тут, пора уходить', None, config.TOKEN_POLICE)

# подсказка
if relationships_Bot__criminalist >= 2:
    loop_m('Пока федералы не приехали, мы успели обнаружить ещё одну улику', None, config.TOKEN_CRIMINALIST)
    loop_m('Видны замыленные капли крови на ножках стула. Судя по всему, '
           'убийца ударил стулом жертву, затем подстроил все как несчастный случай.')

# разговор с подозреваемыми
for i in range(3):
    # помощь
    if i == 2:
        if relationships_Bot__criminalist >= 2:
            loop_m('Я смог отвлечь федералов, давай быстрей последенего опрашивай', None, config.TOKEN_CRIMINALIST)
        else:
            break

    edit_main('Bot__police', 15, 'Кого выбираем на опрос?')  # отдаём через файл команду полицаю
    count = wait()  # выбираем кого опрашиваем

    # диалоги с подозреваемыми
    if count == 1:  # диалог - свидетильница смерти жертвы (46 - 49)
        edit_main('Bot__admin', 46, 'Здравствуйте, я Свидетильница. В тот момент я проходила мимо')
        if wait() == 0:
            edit_main('Bot__admin', 47, 'Но мне кажется, это не случайная смерть')
            if wait() == 0:
                edit_main('Bot__admin', 48, 'Больше ничего не могу сказать')
                wait()
            else:
                edit_main('Bot__admin', 48, 'Только уже само падение')
                wait()
        else:
            edit_main('Bot__admin', 49, 'Я естественно перепугалась и вызвала полицию')
            if wait() == 0:
                edit_main('Bot__admin', 48, 'Я больше ничего не видела и не знаю')
                wait()
            else:
                edit_main('Bot__admin', 48, 'Больше я ничего не знаю')
                wait()

    elif count == 2:  # диалог - муж (50 - 54)
        edit_main('Bot__admin', 50, 'Добрый день, Детектив. Я муж погибшей')
        if wait() == 0:
            edit_main('Bot__admin', 51, 'Но уже возвращался, когда мне позвонила полиция')
            if wait() == 0:
                edit_main('Bot__admin', 52, 'Ничего не знаю')
                wait()
            else:
                edit_main('Bot__admin', 53, 'Это очень сильная потеря для меня...')
                wait()
        else:
            edit_main('Bot__admin', 54, 'Всегда была аккуратной')
            if wait() == 0:
                edit_main('Bot__admin', 53, 'Но то что вернусь я, она не знала')
                wait()
            else:
                edit_main('Bot__admin', 53, 'Но в тот день она не должна была прийти')
                wait()

    else:  # диалог - Подруга (55 - 60)
        edit_main('Bot__admin', 55, 'Хай, я подруга Инна. Вызывали?')
        if wait() == 0:
            edit_main('Bot__admin', 56, 'Я вообще удивлина что она полезламыть окна'
                                        ', так что это точно подстава от своих')
            if wait() == 0:
                edit_main('Bot__admin', 57, 'но она стала покупать какие-то препараты и гворила то'
                                            ' если скажет гле покупает, она будет мертва ')
                if wait() == 0:
                    edit_main('Bot__admin', 58, 'Она слово закон, на неё можно положиться')
                    wait()
                else:
                    edit_main('Bot__admin', 58, 'Ничего такого, обычное дело понимаешь?')
                    wait()
            else:
                edit_main('Bot__admin', 59, 'Говорила, что это из-за своей дурацкой работы. Такая вот она рабочая')
                if wait() == 0:
                    edit_main('Bot__admin', 58, 'Я не интересовалась')
                    wait()
                else:
                    edit_main('Bot__admin', 58, 'Я конечно хотела узнать где она берёт эту дрянь, но так и не узнала')
                    wait()
        else:
            edit_main('Bot__admin', 60, 'Она не была из тех, кто любил тусить или тем более изменять')
            if wait() == 0:
                edit_main('Bot__admin', 58, 'Она не отдыхала. Больше я ничего не знаю')
                wait()
            else:
                edit_main('Bot__admin', 58, 'Больше не знаю')
                wait()

edit_main('Bot__police', 16, 'Ну что скажешь, есть ли подозреваемые?')

if wait() == 0:
    loop_m('Мы задердали ее до конца расследования\nВот её алиби: Я с ней разговаривала по телефону утром, сказала, '
           'что еду к маме. Больше мы не связывались. От мамы я выехала где-то в 13:25-13:30, ехать около часа', None,
           config.TOKEN_POLICE)
    suspect.append('Подруга, Инна')

else:
    loop_m('Мы задержали его, до конца расследования\nЕго алиби: Да, не спорю, это странно, что я вернулся раньше.'
           ' Но это правда. Командировка закончилась раньше, я сменил билеты, взял новые, и раньше вылетел. '
           'Когда подъезжал к цветочному магазину мне позвонили и сказали, что моя жена мертва. Я сразу же поехал '
           'сюда. Клянусь, это был не я.»', None, config.TOKEN_POLICE)
    suspect.append('Муж')


sleep(10)

loop_m('Так, ну пока у нас затишье можете взглянуть на всё происходящие и подумать')

sleep(120)  # 120сек = 2мин

# незнакомец
loop_m('Я знаю, кто убийца', None, config.TOKEN_HELP)
sleep(3)
loop_m('Это не просто самоубийства или случайности')
sleep(4)
loop_m('Есть один человек, торгует наркотой, вот это сделал он. Я у него какое-то время брал дозу,'
       ' но потом закончил...')
sleep(4)
edit_main('Bot__help', 0, 'Имя вроде бы Стас, рост под 178-180, тусуется всегда в баре на Молокова. Там найдете')

if wait() == 0:
    edit_main('Bot__help', 1, 'Я буду мёртв')
    if wait() == 0:
        edit_main('Bot__help', 2, 'Абсолютно')
        wait()
    else:
        edit_main('Bot__help', 2, 'Но я правда хочу Вам помочь')
        wait()
else:
    edit_main('Bot__help', 3, 'Абсолютно')
    if wait() == 1:
        edit_main('Bot__help', 2, 'Но я правда хочу Вам помочь')
        wait()


sleep(5)

# спрашивает про новсоти, диалог
edit_main('Bot__police', 17, 'Новостей пока нет, у вас есть что-нибудь, детектив?')
time_relationships = wait()
if time_relationships == 1:
    loop_m('Пока криминалист отправит вам досье', None, config.TOKEN_POLICE)
elif time_relationships == 3:
    loop_m('Хорошо, сейчас всё сделем', None, config.TOKEN_POLICE)
elif time_relationships == 2:
    edit_main('Bot__police', 18, 'Даже если он наврал, то нам это никак не навредит')
    if wait() == 1:
        loop_m('Скидываю досье', None, config.TOKEN_CRIMINALIST)
        loop_m_photo('AgACAgIAAxkDAAIBsV8QTNpMgQgJVhLl2hTFU_7lYbKJAAJ'
                     '-rjEbPNiBSJFGvLUqu6ZgyQABUZEuAAMBAAMCAAN5AANn9gUAARoE')
        sleep(10)
        loop_m('Детектив, мои люди задержали подозреваемого. Как и говорилось, он был в баре Н', None,
               config.TOKEN_POLICE)
else:
    edit_main('Bot__police', 18, 'У тебя есть какая-то информация?')
    if wait() == 1:
        loop_m('Скидываю досье', None,config.TOKEN_CRIMINALIST)
        loop_m_photo('AgACAgIAAxkDAAIBsV8QTNpMgQgJVhLl2hTFU_7lYbKJAAJ'
                     '-rjEbPNiBSJFGvLUqu6ZgyQABUZEuAAMBAAMCAAN5AANn9gUAARoE')
        sleep(10)
        loop_m('Детектив, мои люди задержали подозреваемого. Как и говорилось, он был в баре', None,
               config.TOKEN_POLICE)

suspect.append("Совкин Станислав Максимович")
sleep(5)
# разговор с подозреваемым 61 - 63
edit_main('Bot__admin', 61, 'Я ничего не делал, за что вы меня задержали!?')
if wait() == 0:
    edit_main('Bot__admin', 62, 'Клянусь!')
    if wait() == 0:
        edit_main('Bot__admin', 63, 'Но я никого не убивал!')
        wait()
else:
    edit_main('Bot__admin', 63, 'Но я никого не убивал!')
    wait()

sleep(2)
# заявление о новом убийстве
loop_m_admin('Начинается четвёртое убийство')

loop_m('Детектив! нет времени , пора выезжать', None, config.TOKEN_POLICE)
sleep(2)
loop_m('У нас произошло новое убийство.', None, config.TOKEN_POLICE)
sleep(3)
loop_m('4.	Убита юная девушка 19 лет в районе Весны города Красноярска. '
       'Предположительная причина смерти: асфиксия дыхательных путей.', None, config.TOKEN_POLICE)
sleep(1)
loop_m('Время смерти: 07.07.2020, 17:30', None, config.TOKEN_POLICE)
sleep(3)
loop_m('Вам надо срочно выезжать на улица Весны, 6. У нас как всегда нет много времени.'
       ' Вам также скоро скинут досье на жертву',
       None, config.TOKEN_POLICE)

sleep(60)  # 1мин - 60сек
# досье
loop_m('Ваше досье, детектив', None, config.TOKEN_CRIMINALIST)
loop_m_photo('AgACAgIAAxkDAAIBdF8QPvjbnwmpwXUxXmL3AUIlE8YpAAJnrjEbPNiBSC4S9kk5zc1Ka_zski4AAwEAAwIAA3kAA2rSAwABGgQ')

sleep(180)  # 3мин = 180сек
# Новости
Bot__journalist.news_5()


# ЧЕТВЁРТОЕ УБИЙСТВО

count = 0  # подсчёт улик

# считает улики и видёт подсчёт времени
for i in range(10):  # 900сек = 10 мин
    if i == 900 or i == 600 or i == 300 or i == 60:  # оповещение для админа
        loop_m_admin(str(i / 60) + 'мин')
    f = open('text.txt', 'r+', encoding='utf8')
    text = [str(i) for i in f.read().split('|')]
    f.close()
    if text[0] == 'main':
        open('text.txt', 'w').close()
        count += 1
    if count == 5:
        break
    sleep(1)

sleep(15)

edit_main('Bot__police', 18, 'Всё, пора уходит. Сам понимаешь почему...\nНенавижу их. Всегда мешают работать!')
relationships_Bot__police += wait()

sleep(2)
loop_m('Пришло время опрашивать людей', None, config.TOKEN_POLICE)

# разговор с подозреваемыми
for i in range(3):
    # помощь
    if i == 2:
        if relationships_Bot__police >= 3:
            loop_m('Давай опросим последнего. Я смог его забрать у них. Только тихо, иначе вставят',
                   None, config.TOKEN_POLICE)
        else:
            break

    edit_main('Bot__police', 20, 'Кого опросим?')  # отдаём через файл команду полицаю
    count = wait()  # выбираем кого опрашиваем

    # диалоги с подозреваемыми
    if count == 1:  # диалог - тётя (64 - 677)
        edit_main('Bot__admin', 64, 'Я тётя Софии. Готова отвечать на ваши вопросы')
        if wait() == 0:
            edit_main('Bot__admin', 65, 'Но особо не придавала этому значения')
            if wait() == 0:
                edit_main('Bot__admin', 66, 'Она ведь уже далеко не маленькая девочка. Больше ничего такого')
                wait()
            else:
                edit_main('Bot__admin', 66, 'Всё, больше не знаю')
                wait()

        else:
            edit_main('Bot__admin', 67, 'Я знала о том, что она далеко не пай-девочка, '
                                         'но не могла ей ничего запрещать, она ведь уже далеко не маленькая девочка')
            if wait() == 0:
                edit_main('Bot__admin', 66, 'Всё, больше не знаю')
                wait()
            else:
                edit_main('Bot__admin', 66, 'Больше ничего')
                wait()

    elif count == 2:  # диалог - лучшая подруга (68 - 72), 66
        edit_main('Bot__admin', 68, 'Приветсвую, я лучшая подруга Сони')
        if wait() == 0:
            edit_main('Bot__admin', 69, 'Вот постоянно отшивает парней')
            if wait() == 0:
                edit_main('Bot__admin', 66, 'Больше ничего не знаю')
            else:
                edit_main('Bot__admin', 70, 'Но где-то с полгода назад она начала тесно с кем-то общаться')
                if wait() == 0:
                    edit_main('Bot__admin', 66, 'Скажу точно, он мне не понравился, лицо его. Не доброе оно')
                    wait()
                else:
                    edit_main('Bot__admin', 66, 'Особо о нём она не говорила, и тем более не показывала')
                    wait()
        else:
            edit_main('Bot__admin', 71, 'Но в последенее время стала тесно общаться с кем-то')
            if wait() == 0:
                edit_main('Bot__admin', 66, 'Особо о нём она не говорила, и тем более не показывала.'
                                            ' А катался на тонированой машине')
                wait()
            else:
                edit_main('Bot__admin', 66, 'Вид у него не добрый')
                wait()

    else:  # диалог - свидетильница (72 - 73)
        edit_main('Bot__admin', 72, 'Так, здравствуйте, я свидетильница. Была поблизости')
        if wait() == 0:
            edit_main('Bot__admin', 73, 'Больше я ничего не знаю... Это было быстро')
            wait()
        else:
            edit_main('Bot__admin', 73, 'Тут же позвонила в скорую. Больше я ничего не знаю')
            wait()

sleep(3)

# мини диалог (21, 22), выбор подозреваемого
loop_m('Хм, тут всё странно...', None, config.TOKEN_POLICE)
edit_main('Bot__police', 21, 'Думаешь тут есть вообще подозреваемые?')
time_relationships = wait()
relationships_Bot__police += time_relationships
if time_relationships == 0:
    edit_main('Bot__police', 22, 'Ну как знаешь, делай выбор')
elif time_relationships == 1:
    edit_main('Bot__police', 22, 'Ага... Но всё равно выбор за тобой')
else:
    edit_main('Bot__police', 22, 'Ещё  дурак... ну да, да\nДелай выбор уже давай')

time_relationships = wait()
if time_relationships == 1:
    loop_m('Алиби: Мне так сложно говорить, простите. Я была на работе,'
           ' проверяла наличие товара на складе, работала с самого утра')
    suspect.append('Тётя')
elif time_relationships == 2:
    loop_m('Подругу выбрал... Хорошо, мы задержим её\nАлиби: Я её любила даже больше, чем просто подругу. Она была мне '
           'гораздо ближе, это была какая-то любовь. Но я её не убивала, клянусь. '
           'Я была в спортзале с 4х часов, в течение двух часов')
    suspect.append('Подруга, Алиса')
else:
    loop_m('Мне кажется, ты сделал правильный выбор. Молодец')

sleep(8)

# Секретный чат, ккримналист
loop_m('Мы нашли символы на руке. Пока ты разговаривал, я разгадал шифр. Это секретный чат. '
       'Я его сейчас активирую и тебе должен кто-то написать.  Жди', None, config.TOKEN_CRIMINALIST)

# гадалка
loop_m('Привет', None, config.TOKEN_FORTUNETELLER)
sleep(2)
edit_main('Bot__fortuneteller', 0, 'Ты разгадал мою загадку')

if wait() == 0:
    edit_main('Bot__fortuneteller', 1, 'Другой вопрос, кто ты такой')
    wait()

edit_main('Bot__fortuneteller', 2, 'Допустим')
wait()

loop_m('Но это имя мне знакомо')
sleep(1)
loop_m('Что-то не так?')
sleep(3)
edit_main('Bot__fortuneteller', 4, 'Будьте честны со мной, и я буду честна с вами')
if wait() == 0:
    loop_m('Не могу рассказать всё, иначе сама буду в опасности, но могу сказать точно, что это не тот,'
           ' кого вы подозреваете')
    edit_main('Bot__fortuneteller', 5, 'Будьте честны со мной, и я буду честна с вами')
    wait()
else:
    edit_main('Bot__fortuneteller', 6, 'Мы давно не общались')
    wait()

sleep(3)

# криминалист
loop_m('Я вижу, что чат закрыт. Хотелось бы спросить что было, но нам уже сообщилио о новом убийстве',
       None, config.TOKEN_CRIMINALIST)
loop_m('Пойду готовить досье')

# полицай о новом убийстве
loop_m_admin('Начинается пятое убийство')

loop_m('Произолшо очередное убийство! Это уже 5, пора заканчивать дело!!!', None, config.TOKEN_POLICE)
sleep(2)
loop_m('Убит мужчина 27 лет в собственной квартире, в районе Весны Предположительная причина смерти:'
       ' передозировка инсулином.')
sleep(1)
loop_m('Время смерти: 07.07.2020, 19:00')
sleep(2)
loop_m('Выдвигайся к 149 школе на спортивную площадку')
loop_m('На этот раз у нас 10 мин')

sleep(60)  # 50сек = 1мин
# досье
loop_m('Досье для ятого убийства')
loop_m_photo('AgACAgIAAxkDAAIBdV8QPvlyIi-B0on72v1mbaq2UtH2AAJorjEbPNiBSCHUwW0WJPT2dvHpki4AAwEAAwIAA3kAA_jWAwABGgQ')

sleep(180)  # 180сек = 3мин
# 5 новости
Bot__journalist.news_5()


# ПЯТОЕ УБИЙСТВО

count = 0  # подсчёт улик

# считает улики и видёт подсчёт времени
for i in range(600):  # 600сек = 10 мин
    if i == 600 or i == 300 or i == 60:  # оповещение для админа
        loop_m_admin(str(i / 60) + 'мин')

    f = open('text.txt', 'r+', encoding='utf8')
    text = [str(i) for i in f.read().split('|')]
    f.close()
    if text[0] == 'main':
        open('text.txt', 'w').close()
        count += 1
    if count == 5:
        break
    sleep(1)

sleep(5)

loop_m('Снова федералы...', None, config.TOKEN_POLICE)
sleep(2)
loop_m('Ну что, идём разговаривать и снова с ограничением и-за федералов...')

# разговор с подозреваемыми
for i in range(2):
    edit_main('Bot__police', 24, 'Кого берёшь?')  # отдаём через файл команду полицаю
    count = wait()  # выбираем кого опрашиваем

    # диалоги с подозреваемыми
    if count == 1:  # диалог - Невеста (74 - 76)
        edit_main('Bot__admin', 74, 'День добрый, я невеста Влада, Кира')
        if wait() == 1:
            edit_main('Bot__admin', 75, 'Меня охватила паника, ужас, шок!')
            if wait() == 1:
                edit_main('Bot__admin', 76, 'Всегда был абсолютно адекватен, я..я не знаю, что могло произойти и '
                                            'что он мог принимать, как мог спутать дозы…')
                wait()
            else:
                edit_main('Bot__admin', 76, 'Он очень ответственный человек')
                wait()
        else:
            edit_main('Bot__admin', 75, 'Всё как обычно')
            if wait() == 1:
                edit_main('Bot__admin', 76, 'Всегда был абсолютно адекватен, я..я не знаю, что могло произойти и '
                                            'что он мог принимать, как мог спутать дозы…')
                wait()
            else:
                edit_main('Bot__admin', 76, 'Он очень ответственный человек')
                wait()

    elif count == 2:  # диалог - лучший друг (77 - 80)
        edit_main('Bot__admin', 77, 'Всем привет. Илья, лучший друг Влада')
        if wait() == 1:
            edit_main('Bot__admin', 78, 'Но толком ничего не сказал... Это всё пожалуй')
            if wait() == 1:
                edit_main('Bot__admin', 79, 'Он очень ответственный')
                wait()
            else:
                edit_main('Bot__admin', 79, 'Но парой может что-то утаить')
                wait()
        else:
            edit_main('Bot__admin', 80, 'При этом всегда доставал дозу он')
            if wait() == 1:
                edit_main('Bot__admin', 79, 'Нам это не собо понравилось')
                wait()
            else:
                edit_main('Bot__admin', 79, 'Та ещё дрянь')
                wait()

    else:  # диалог - 	Отец (81 - 85)
        edit_main('Bot__admin', 81, 'Здравствуйте. Я отец Влада')
        if wait() == 1:
            edit_main('Bot__admin', 82, 'Я с ним был ближе чем мать')
            if wait() == 1:
                edit_main('Bot__admin', 83, 'Также отвесным и серьёзным')
                wait()
            else:
                edit_main('Bot__admin', 85, 'Вот...')
                if wait() == 0:
                    edit_main('Bot__admin', 83, 'То показалось странным и даже подозрительным')
                    wait()
                else:
                    edit_main('Bot__admin', 83, 'Да и он не говорил ничего')
                    wait()
        else:
            edit_main('Bot__admin', 84, 'Это показалось странным и даже подозрительным')
            if wait() == 0:
                edit_main('Bot__admin', 83, 'Да и он не говорил ничего')
                wait()
            else:
                edit_main('Bot__admin', 83, 'Также отвесным и серьёзным')
                wait()

sleep(4)
loop_m('Ну что скажаешь?', None, config.TOKEN_POLICE)
edit_main('Bot__police', 25, 'Кто подозреваемый?')  # отдаём через файл команду полицаю

if wait() == 0:
    loop_m('Её алиби: «Я вернулась домой от подруги, зашла, а там лежит он… Меня охватила паника, ужас, шок. '
           'Как только чуть успокоилась, вызвала полицию. Он никогда не пропускал приём инсулина, и тем более, '
           'не могу случайно спутать дозы. Это невозможно, он относился к этому с полной ответственностью. Всегда '
           'был абсолютно адекватен, я..я не знаю, что могло произойти и что он мог принимать, как мог спутать дозы…»')
    suspect.append('Кира, невеста')

else:
    loop_m('Его Алиби: «По приколу пару раз употребляли, но мы лишь баловались, при этом всегда доставал'
           ' дозу он. Но всегда был в себе, а лекарство тем более не пропускал. После пары раз больше не пробовали. В'
           ' последнее время он стал более скрытный, говорил, что переживает за Киру, да и за свою жизнь. Но толком'
           ' ничего не сказал.»')
    suspect.append('Друг, Илья')


sleep(3)
loop_m('Думаю пришло время уже что-то делать. У нас 5 убийство и есть подозреваемые')
loop_m('Предлогаяю сопоставить все данные и выбрать убийцу...')
sleep(2)
loop_m('Сейчас тебе криминалист скинет по всем подозреваемым досье\nТы должен подумать. '
       'Скоро я тебе напишу и спрошу что ты думаешь...')

sleep(3)
loop_m('Сейчас отправлю досье всех подозреваемых, кого ты задержал', None, config.TOKEN_CRIMINALIST)
for i in suspect:
    sleep(5)
    loop_m('---')
    if i == 'Подруга, Инна':
        loop_m('Подруга убитой, Маниулина Инна Владимировна,38 лет, 24.05.1982. Уроженка города Красноярск. Окончила 9 классов городской школы и поступила в медицинский колледж на медсестру. Закончив колледж, нашла работу медсестры в частной клинике. Родителей нет. Бабушка и дедушка живут на окраине города, с девушкой видятся редко. Не замужем, детей нет. Отсутствуют судимости, братья и сестры.')
    elif i == 'Муж':
        loop_m('Муж убитой, Эйснер Антон Антонович,39 лет, 01.12.1981. Уроженец города Москва. Родители живы, проживают в Красноярске. В возрасте 3х лет был вынужден переехать с родителями в Красноярск в связи с работой отца, после чего так и не вернулся обратно в родной город. Отучился в красноярском лицее, после чего, уйдя после 11 класса, поступил на бухгалтера. Стал работать в Красноярской Мебельной Компании, после чего был повышен до директора фирмы. Со своей женой познакомился во время поездки в Германию. После сыграли свадьбу в Германии, затем переехали в Красноярск. Детей нет, судимостей нет, периодически уезжает в командировки по работе. ')
    elif i == 'Хозяйка собаки':
        loop_m('Хозяйка собаки, Ищенко Дарья Игнатовна, 26 лет, 26.05.1994. Уроженка города Красноярск. Окончила среднюю школу, ушла после 9 класса в колледж на тренера по дзюдо. Отучилась, в данный момент работает тренером в детском центре. Была собака, но та умерла из-за конфуза во время операции в ветеринарной клинике. Единственный ребенок в семье, родители умерли, родных и близких нет. Живет в однокомнатной квартире. Судимостей нет.')
    elif i == 'Жена':
        loop_m('Жена убитого, Авдеева (Бойкина) Алена Ярославовна, 35 лет, 08.07.1985. Уроженка города Красноярск. Есть двое детей-близнецов 5 лет. Единственный ребенок в семье, родители живы, проживают в загородном доме за Красноярском. Образование девушка получила в Гимназии города Красноярск, окончила 11 классов, затем поступила в университет на психолога, выпустилась из университета с отличием. В скором времени познакомилась со своим будущим мужем. В 29 лет вышла замуж, спустя год родила двух детей. Работает психологом крупной конторе.')
    elif i == 'Подруга, Алина':
        loop_m('Подруга убитой, Зейненко Алина Ивановна, 22 года, 21.10.1998. Уроженка города Красноярск, родилась в многодетной семье, была самым младшим ребенком. Обучалась в одной из школ до 10 лет, из-за травли пришлось перевестись в другую, где девушка доучилась до 11 класса. Окончила школу с одной четверкой по математике, затем поступила на повара-кондитера. Ранее состояла в отношениях с молодым человеком по имени Вячеслав, но прекратили отношения спустя долгое время. Родители живы, проживают в Красноярске. Сама девушка проживает в общежитии, где и познакомилась с убитой. Являлась соседкой по комнате убитой. Есть сестра Ирина-16 лет, проживает с родителями.')
    elif i == 'Парень':
        loop_m('Парень убитой, Ханин Олег Богданович, 24 года, 13.01.1996. Уроженец города Саяногорск. Получал образование все 11 лет в Саяногорской школе, окончил школу с красным аттестатом, затем поступил в Красноярский университет на экономиста. Мать умерла, когда мальчику было 10, отец ушел из семьи при рождении Олега, всю оставшуюся жизнь мальчика воспитывала бабушка, в данный момент живущая в Саяногорске. Со своей девушкой Еленой Олег познакомился в кафе, долгое время состояли в отношениях. Снимает квартиру в центре города, каждые три месяца приезжает к бабушке в Саяногорск, подрабатывает доставщиком еды в распространённой фирме, чем зарабатывает себе на жизнь. Братьев и сестер нет.')
    elif i == 'Совкин Станислав Максимович':
        loop_m('Совкин Станислав Максимович, 25 лет, 15.12.1995 г.р. Нет родных, все близкие мертвы. Был отправлен в детский дом в возрасте пяти лет. Имел знакомство с курением и проблемами с алкоголем. Стоял долгое время на учете в милиции за алкоголь и воровство. В 18 лет покинул пределы детского дома, начал развивать собственную торговлю незаконными веществами. Стал мелким дилером, занимался этим долгое время, после чего завязал из-за неудачной ситуации. Не имеет образования помимо окончания 9 классов. Никаких заболеваний в медицинской карте нет. Братьев и сестер нет, семью не видел с детства.')
    elif i == 'Тётя':
        loop_m('Тетя убитой, Шашина Марианна Кирилловна, 50 лет, 06.09.1970. Уроженка поселка Песчанка, окончила сельскую школу и поступила в Красноярский колледж на предпринимателя.  Есть двое детей, 25 и 23 года, обе девочки. После окончания колледжа какое-то время проходила практику в городе, затем устроилась на работу. Проживает одна на окраине города. С недавних пор жила в одной квартире с племянницей. Муж умер от инфаркта в возрасте 45 лет. Судимостей нет, братья и сестры отсутствуют.')
    elif i == 'Лучшая подруга, Алиса':
        loop_m('Лучшая подруга убитой, Осипова Алиса Витальевна,19 лет, 15.04.2000. Уроженка города Красноярск. Родители живы, есть младшая сестра 10 лет и брат 13 лет, все живут в центре города. Окончила Красноярскую школу, после 9го класса выбрала биохимическое направление в 10-11 класс. После окончания школы поступила в университет, выбрав профессию микробиолога. С убитой познакомилась на лекциях, сильно сдружились. Личная жизнь отсутствуют, судимости отсутствуют.')
    elif i == 'Кира, невеста':
        loop_m('Невеста убитого, Зоева Кира Алексеевна, 27 лет, 15.09.1993. Уроженка города Красноярска. Родители живы, бабушка и дедушка тоже, есть старший брат Даниил. Родители проживают в Нижнем Новгороде, переехали туда около года назад. Старший брат 29 лет живет в Москве. Кира окончила Красноярский лицей, затем поступила на фармацевта. Спустя год после обучения в университете нашла свою любовь, спустя несколько лет вышла замуж. Семья была обеспечена, поэтому Кира не стала работать по профессии, став домохозяйкой. Часто контактирует с братом, несмотря на большое расстояние. Отсутствуют судимости, дети.')
    elif i == 'Друг, Илья':
        loop_m('Друг убитого, Миронов Илья Данилович, 28 лет, 06.07.1992. Уроженец города Екатеринбург. В возрасте 7 лет переехал с матерью от отца в Красноярск, где и остался жить и учиться. Получал обучение в обычной средней школе. Ушел после 11 класса дабы обучиться на химика. От его лица было подано 4 заявления в разные институты., приняли только в один. Со своим лучшим другом Илья познакомился на вечеринке у их общего знакомого, с тех пор сдружились. Мать Ильи проживает в Красноярске, отец в Екатеринбурге. Сам Илья снимает квартиру недалеко от института. Также Илья работает на полставки в одной из фирм, делающих поставки определенных товаров в больницы, аптеки и т.д. В детстве увлекался мифологией, верующий. Считает, что у всего есть карма, ангелы и демоны, а также ад и сам Сатана. Никаких заболеваний в медицинской карте нет. Имеет хорошее химическое образование, победитель многих олимпиад по химии и органике.')


sleep(120)  # 2 мин = 120сек

# отрытия решения
edit_main('Bot__police', 26, 'Всё, время пришло. Готов?')  # отдаём через файл команду полицаю
wait()

# концовка
loop_m('Напиши, кто по твоему убийца?')

if wait() == 1:
    loop_m('XXX', None, config.TOKEN_POLICE)
    loop_m('XXX', None, config.TOKEN_CRIMINALIST)
    loop_m('XXX', None, config.TOKEN_HELP)
    loop_m('XXX', None, config.TOKEN_FORTUNETELLER)
    loop_m('XXX', None, config.TOKEN_ADMIN)
    loop_m('XXX', None, config.TOKEN_POLICE)
    loop_m('XXX', None, config.TOKEN_CRIMINALIST)
    loop_m('XXX', None, config.TOKEN_HELP)
    loop_m('XXX', None, config.TOKEN_FORTUNETELLER)
    loop_m('XXX', None, config.TOKEN_ADMIN)
    sleep(5)
    Bot__journalist.news_end1()

else:
    loop_m('XXX', None, config.TOKEN_POLICE)
    loop_m('XXX', None, config.TOKEN_CRIMINALIST)
    loop_m('XXX', None, config.TOKEN_HELP)
    loop_m('XXX', None, config.TOKEN_FORTUNETELLER)
    loop_m('XXX', None, config.TOKEN_ADMIN)
    loop_m('XXX', None, config.TOKEN_POLICE)
    loop_m('XXX', None, config.TOKEN_CRIMINALIST)
    loop_m('XXX', None, config.TOKEN_HELP)
    loop_m('XXX', None, config.TOKEN_FORTUNETELLER)
    loop_m('XXX', None, config.TOKEN_ADMIN)
    sleep(5)
    Bot__journalist.news_end2()