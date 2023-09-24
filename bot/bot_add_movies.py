import asyncio
import io

from aiogram import Bot, Dispatcher,types, F
import os
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
import FSM
import parser_movies
import add_date
import keyboard

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: Message, state: FSMContext):
    global user_id
    global item
    user_id = message.from_user.id
    if add_date.search_user_in_db(user_id) == False:
        add_date.users_add_to_session(user_id)
        await message.answer('Введите ID второго пользователя:')
        await state.set_state(FSM.UserState.user_add_db_state)
    else:
        item = await parser_movies.create_date_movie()
        image = item['poster']
        await message.answer_photo(types.InputFile(io.BytesIO(image),
                                                   filename='poster.jpg'),
                                   caption=f'Название: {item["name"]}'
                                           f'\nГод: {item["year"]}'
                                           f'\nОписание: {item["description"]}',
                                   reply_markup=keyboard.keyboard
                                   )

@dp.message(FSM.UserState.user_add_db_state, F.text)
async def add_to_second_users_to_bd(message: Message, state: FSMContext):
    global second_user_id
    second_user_id = message.text
    add_date.add_second_user_in_session(second_user_id)
    await message.answer('Пользователь успешно добавлен!')
    state.clear()
    item = await parser_movies.create_date_movie()
    image = item['poster']
    await message.answer_photo(types.InputFile(io.BytesIO(image),filename='poster.jpg'),
                               caption=f'Название: {item["name"]}'
                                       f'\nГод: {item["year"]}'
                                       f'\nОписание: {item["description"]}',
                               reply_markup=keyboard.keyboard
                               )




@dp.message(F.text=='Смотреть')
async def watch_movie(message:Message):
    global item
    if add_date.search_movies_in_db(second_user_id, item['name']):
        await message.answer('Фильм есть у второго пользователя!Приятного просмотра')
        item = await parser_movies.create_date_movie()
        image = item['poster']
        await message.answer_photo(types.InputFile(io.BytesIO(image),
                                                   filename='poster.jpg'),
                                   caption=f'Название: {item["name"]}'
                                           f'\nГод: {item["year"]}'
                                           f'\nОписание: {item["description"]}',
                                   reply_markup=keyboard.keyboard
                                   )
    else:
        add_date.add_movie_in_db(user_id, item['name'], item['year'])
    item = await parser_movies.create_date_movie()
    image = item['poster']
    await message.answer_photo(types.InputFile(io.BytesIO(image),
                                               filename='poster.jpg'),
                               caption=f'Название: {item["name"]}'
                                       f'\nГод: {item["year"]}'
                                       f'\nОписание: {item["description"]}',
                               reply_markup=keyboard.keyboard
                               )


@dp.message(F.text=='Не смотреть')
async def not_watch_movie(message:Message):
    item = await parser_movies.create_date_movie()
    image = item['poster']
    await message.answer_photo(types.InputFile(io.BytesIO(image),
                                               filename='poster.jpg'),
                               caption=f'Название: {item["name"]}'
                                       f'\nГод: {item["year"]}'
                                       f'\nОписание: {item["description"]}',
                               reply_markup=keyboard.keyboard
                               )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
