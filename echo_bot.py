import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Configure logging
logging.basicConfig(level=logging.INFO)

# Your bot token from BotFather- telegram 
API_TOKEN = '8335555639:AAGunUL5_yF465-8EORim0Eoxz2xOBULwMM'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm Echo Bot! Send me any message and I'll echo it back.")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
   