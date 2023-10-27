import logging



from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5665055270:AAGERzC0yUYA0qypSDvQNjdxNJgzUGOUrm0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





