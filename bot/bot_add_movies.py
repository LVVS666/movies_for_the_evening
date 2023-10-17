import asyncio
from aiogram import Bot, Dispatcher, F
import os
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext
import FSM, parser_movies, add_date, func_answer


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher()
add_date.create_db()
coincidence = None


@dp.message(Command('start'))
async def start(message: Message, state: FSMContext):
    user_data = await state.get_data()
    id_movie = user_data.get('id_movie', 0)
    if add_date.search_user_in_db(message.from_user.id) == False:
        add_date.users_add_to_session(message.from_user.id)
        await message.answer('Введите ID второго пользователя:')
        await state.set_state(FSM.UserState.user_add_db_state)
    else:
        id_movie += 1
        item_date = await parser_movies.create_date_movie()
        add_date.create_movie_date(item_date)
        item = add_date.return_movie(id_movie)
        await func_answer.movie_answer(message, item)
        await state.update_data(id_movie=id_movie, item=item)


@dp.message(FSM.UserState.user_add_db_state, F.text)
async def add_to_second_users_to_bd(message: Message, state: FSMContext):
    user_data = await state.get_data()
    id_movie = user_data.get('id_movie', 0)
    second_user_id = int(message.text)
    add_date.add_second_user_in_session(second_user_id)
    await message.answer('Пользователь успешно добавлен!')
    await state.clear()
    id_movie += 1
    item_date = await parser_movies.create_date_movie()
    add_date.create_movie_date(item_date)
    item = add_date.return_movie(id_movie)
    await func_answer.movie_answer(message, item)
    await state.update_data(id_movie=id_movie, item=item)


@dp.message(F.text == 'Смотреть')
async def watch_movie(message: Message, state: FSMContext):
    global coincidence
    if coincidence != False:
        await func_answer.coincidence_answer(message, coincidence)
        coincidence = False
    user_data = await state.get_data()
    id_movie = user_data.get('id_movie', 0)
    item = user_data.get('item', None)
    list_users = add_date.create_list_users()
    second_user_id = list_users[1]
    if message.from_user.id == list_users[1]:
        second_user_id = list_users[0]
    if add_date.search_movies_in_db(second_user_id, item['name']):
        coincidence = item
        await func_answer.coincidence_answer(message, coincidence)
        id_movie += 1
        item_date = await parser_movies.create_date_movie()
        add_date.create_movie_date(item_date)
        item = add_date.return_movie(id_movie)
        await func_answer.movie_answer(message, item)
        await state.update_data(id_movie=id_movie, item=item)
    else:
        add_date.add_movie_in_db(message.from_user.id, item['name'], item['year'])
        id_movie += 1
        item_date = await parser_movies.create_date_movie()
        add_date.create_movie_date(item_date)
        item = add_date.return_movie(id_movie)
        await func_answer.movie_answer(message, item)
        await state.update_data(id_movie=id_movie, item=item)


@dp.message(F.text == 'Не смотреть')
async def not_watch_movie(message: Message, state: FSMContext):
    global coincidence
    if coincidence != None:
        await func_answer.coincidence_answer(message, coincidence)
        coincidence = None
    user_data = await state.get_data()
    id_movie = user_data.get('id_movie', 0)
    id_movie += 1
    item_date = await parser_movies.create_date_movie()
    add_date.create_movie_date(item_date)
    item = add_date.return_movie(id_movie)
    await func_answer.movie_answer(message, item)
    await state.update_data(id_movie=id_movie, item=item)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
