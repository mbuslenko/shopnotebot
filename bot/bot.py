import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from API.Profile import create_profile

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    external_id = message.from_user.id
    print(external_id)
    name = message.from_user.first_name
    print(name)
    create_profile(external_id=external_id, name=name)

    await message.reply("Hi!\nTest confirmed")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
