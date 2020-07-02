import logging
import config
import asyncio

from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN_POLICE)


async def start(m, k=None):
    await bot.send_message(config.ID_PERSON, m, reply_markup=k)


def loop_m(message, k=None, bot_t=None):
    global bot
    if bool(bot_t):
        bot = Bot(token=bot_t)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start(message, k))