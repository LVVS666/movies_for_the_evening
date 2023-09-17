from aiogram import Bot, Dispatcher
import os

from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from .parser_movies import item

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(Command('start'))
async def start(message:Message):
    await message.answer()



