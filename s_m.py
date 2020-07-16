import logging
import config
import asyncio

from aiogram import Bot
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN_POLICE)
bot_a = Bot(token=config.TOKEN_POLICE)


async def start(m, k=None):
    await bot.send_message(config.ID_PERSON, m, reply_markup=k)


# для отправки сообщения
def loop_m(message, k=None, bot_t=None):
    global bot
    if bool(bot_t):
        bot = Bot(token=bot_t)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start(message, k))


async def photo(m, k=None):
    await bot.send_photo(config.ID_PERSON, m, reply_markup=k)


# для отправки фото
def loop_m_photo(message, k=None, bot_t=None):
    global bot
    if bool(bot_t):
        bot = Bot(token=bot_t)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(photo(message, k))


# для отправи сообщения админу. оповещение
async def admin(m):
    await bot_a.send_message(config.MY_ID, m)


def loop_m_admin(message, bot_t=None):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(admin(message))