import asyncio
import io

from aiogram import Bot, Dispatcher,types
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
    item = await parser_movies.create_date_movie()
    image = item['poster']
    await message.answer_photo(types.InputFile(io.BytesIO(image),
                                               filename='poster.jpg'),
                                               caption=f'Название: {item["name"]}'
                                                       f'\nГод: {item["year"]}'
                                                       f'\nОписание: {item["description"]}'
                               )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
