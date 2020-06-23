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


async def police_as():
    global relationships_Bot__police
    if relationships_Bot__police >= 0:
        relationships_Bot__police += police.bot_police_main(0, 'Я рад, что ты снова с нами в строю')
    else:
        pass


async def criminalist_as():
    global relationships_Bot__criminalist

    bot_c = telebot.TeleBot(config.TOKEN_CRIMINALIST)
    bot_c.send_message(config.ID_PERSON, 'Слышал ты снова с нами\n'
                                         'Хотел напомнить, что ты не забывай про меня. А что знаю я тебя...\n',
                                         parse_mode='html')

    relationships_Bot__criminalist += crime.bot_criminalist_main(0, 'Скидывай мне улики, помогу тебе с ними. Если что,'
                                                                    ' они выглядят примерно так <b>"qwerty12"</b>')


async def main_as():
    task1 = asyncio.create_task(police_as())
    task2 = asyncio.create_task(criminalist_as())

    await asyncio.gather(task1, task2)


asyncio.run(main_as())

print(relationships_Bot__criminalist, relationships_Bot__police)

if __name__ == '__main__':
    bot.polling(none_stop=True)