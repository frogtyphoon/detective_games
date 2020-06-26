import telebot
import config
from telebot import types
import time
import asyncio


# import Bot__admin
# import Bot__help
# import Bot__гадалка
import Bot__police as police
# import Bot__журналист
import Bot__криминалист as crime

# токен для бота
bot = telebot.TeleBot(config.TOKEN_POLICE)

# первые сообщения для подготовки. Моделируем ситауацию отсутсвия
bot.send_message(config.ID_PERSON, 'Чёрт, Паша, ты где пропал?', parse_mode='html')
bot.send_message(config.ID_PERSON, 'Уже неделя прошла... Где ты пропадаешь???', parse_mode='html')
bot.send_message(config.ID_PERSON, 'Если не отвечаешь через неделю, то ты уволен!', parse_mode='html')
bot.send_message(config.ID_PERSON, 'У тебя осталось 24 часа и ты не будешь стоять рядом со мной!',
                 parse_mode='html')

# Отношения с игроком
relationships_Bot__police, relationships_Bot__criminalist = 0, 0

relationships_Bot__police += police.bot_police_main(0, 'Отвечай как можно скорей!')

print(relationships_Bot__police, relationships_Bot__criminalist)

# при плохих отношениях, майор не скажет о времени, а только потом напомнит ему
time_talk_answer = False

# Первая развязка (1, 2, 3)
if relationships_Bot__police >= 0:
    relationships_Bot__police += police.bot_police_main(1, 'Я рад, что ты снова с нами в строю')
    if relationships_Bot__police <= 0:
        if police.bot_police_main(2, 'Совсем страх потерял?') < 0:
            relationships_Bot__police += -1
            bot.send_message(config.ID_PERSON, 'Я сейчас на исходе, поэтому бегом на место преступления'
                                               ' по адресу "УЛИЦА"\nКонец связи')
            time_talk_answer = True
        else:
            relationships_Bot__police += 1
            bot.send_message(config.ID_PERSON, 'Кратко ввожу в курс дела. Рядом произошёл суицид, сходи да проверь'
                                               ' там всё')
            relationships_Bot__police += police.bot_police_main(3, 'Чтобы через 15 мин был там, понял?!')
    else:
        bot.send_message(config.ID_PERSON, 'Тебе срочно надо выезжать "УЛИЦА", ведь убийца не дремлет')
        relationships_Bot__police += police.bot_police_main(3, 'Добраться до точки и просмотреть убийтво, тебе даётся'
                                                               ' 15мин. Уяснил, Павел?')
# Вторая развязка (4)
else:
    if police.bot_police_main(4, 'Ещё раз что-то вякнишь, сниму зарплату!') < 0:
        time_talk_answer = True
        bot.send_message(config.ID_PERSON, 'Я знаю тебя очень хорошо, и если ты не хочешь, чтобы твоя карьера рухнула'
                                           ' прямо сейча, то бегом на место преступления!\n'
                                           'Вот координаты, сам разберёшься "КОООРДИНАТЫЫ"')
    else:
        bot.send_message(config.ID_PERSON, 'Значит неподалеку что-то случилось, выдвигайся туда\n'
                                           'У тебя есть 15 мин. Вот координаты "КООРЛДИНАТЫ"')


# криминалист
bot_c = telebot.TeleBot(config.TOKEN_CRIMINALIST)
bot_c.send_message(config.ID_PERSON, 'Слышал ты снова с нами\n'
                                     'Хотел напомнить, что ты не забывай про меня. А что знаю я тебя...\n',
                                     parse_mode='html')

relationships_Bot__criminalist += crime.bot_criminalist_main(0, 'Скидывай мне улики, помогу тебе с ними. Если что,'
                                                                ' они выглядят примерно так <b>"qwerty12"</b>')


print(relationships_Bot__criminalist, relationships_Bot__police)

if __name__ == '__main__':
    bot.polling(none_stop=True)