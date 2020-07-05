import logging
import config
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=config.TOKEN_HELP)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


# ответ персонажа на ответ игрока
@dp.message_handler(commands=['aadfjr'])
async def said(message: types.Message):
    await bot.send_message()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)