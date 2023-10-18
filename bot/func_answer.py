from time import sleep

from aiogram import types

import keyboard
import parser_movies

MAX_LENGTH = 4096


async def movie_answer(message, item):
    image = parser_movies.upload_image(item["poster"])
    await message.answer_photo(
        types.BufferedInputFile(image, filename="poster.jpg"),
        caption=f'Название: {item["name"]}'
        f'\nГод: {item["year"]}'
        f'\nОписание: {item["description"][:MAX_LENGTH]}',
        reply_markup=keyboard.keyboard,
    )


async def coincidence_answer(message, item):
    image = parser_movies.upload_image(item["poster"])
    await message.answer("У вас совпадение!🎬")
    await message.answer_photo(
        types.BufferedInputFile(image, filename="poster.jpg"),
        caption=f'Название: {item["name"]}'
        f'\nГод: {item["year"]}'
        f'\nОписание: {item["description"][:MAX_LENGTH]}'
        f'\n'
        f'\nПриятного просмотра!🕶',
    )
    await message.answer('🍿')
    sleep(5)


