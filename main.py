import telebot
import config
from telebot import types
import time

# import Bot__admin
# import Bot__help
import Bot__police as police
# import Bot__гадалка
# import Bot__журналист
# import Bot__криминалист

bot = telebot.TeleBot(config.TOKEN_POLICE)

bot.send_message(config.ID_PERSON, 'Чёрт, Паша, ты где пропал?', parse_mode='html')
bot.send_message(config.ID_PERSON, 'Уже неделя прошла... Где ты пропадаешь???', parse_mode='html')
bot.send_message(config.ID_PERSON, 'Если не отвечаешь через неделю, то ты уволен!', parse_mode='html')
bot.send_message(config.ID_PERSON, 'У тебя осталось 24 часа и ты не будешь стоять рядом со мной!',
                 parse_mode='html')


relationships_Bot__police, relationships_Bot__admin = 0, 0

check = police.bot_police_main(0)
if bool(check):
    print(0)

relationships_Bot__police += check[0]

bot.send_message(config.ID_PERSON, check[1], parse_mode='html')

if __name__ == '__main__':
    bot.polling(none_stop=True)