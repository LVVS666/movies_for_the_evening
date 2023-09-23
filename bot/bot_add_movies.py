import asyncio

from aiogram import Bot, Dispatcher
import os

from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

import parser_movies

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(Command('start'))
async def start(message: Message):
    item = parser_movies.date_movie
    await message.answer(f'{item["name"]}\n{item["year"]}\n{item["description"]}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
