import telebot
import config
from telebot import types
import time

# import Bot__admin
# import Bot__help
# import Bot__гадалка
import Bot__police as police
# import Bot__журналист
import Bot__криминалист

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

relationships_Bot__police += police.bot_police_main(0)

if relationships_Bot__police > 0:
    bot.send_message(config.ID_PERSON, 'Хорошо. Я рад, что ты снова с нами в строю', parse_mode='html')
else:
    pass

bot = telebot.TeleBot(config.TOKEN_CRIMINALIST)
bot.send_message(config.ID_PERSON, 'Слышал ты снова с нами\n'
                                   'Хотел напомнить, что ты не забывай про меня. А что знаю я тебя...\n'
                                   'Скидывай мне улики, помогу тебе с ними. Если что,'
                                   ' они выглядят примерно так <b>"qwerty12"</b>', parse_mode='html')

if __name__ == '__main__':
    bot.polling(none_stop=True)