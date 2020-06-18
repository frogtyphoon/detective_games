import telebot
import config
from telebot import types
import time

# import Bot__admin
# import Bot__help
from Bot__police import bot_police_main
# import Bot__гадалка
# import Bot__журналист
# import Bot__криминалист

relationships_Bot__police, relationships_Bot__admin = 0, 0


#  отправка первого сообщения без ввода
# bot = telebot.TeleBot(config.TOKEN_POLICE)
# bot.send_message('991296393', 'Чёрт, Паша, ты где пропал?', parse_mode='html')
# bot.send_message('991296393', 'Уже неделя прошла... Где ты пропадаешь???', parse_mode='html')
# bot.send_message('991296393', 'Если не отвечаешь через неделю, то ты уволен!', parse_mode='html')
# bot.send_message('991296393', 'У тебя осталось 24 часа и ты не будешь стоять рядом со мной!', parse_mode='html')

check = bot_police_main(0)
if bool(check):
    print(0)

