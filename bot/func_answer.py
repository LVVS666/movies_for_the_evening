from aiogram import types

import parser_movies, keyboard


async def movie_answer(message, item):
    image = parser_movies.upload_image(item["poster"])
    await message.answer_photo(
        types.BufferedInputFile(image, filename="poster.jpg"),
        caption=f'Название: {item["name"]}'
        f'\nГод: {item["year"]}'
        f'\nОписание: {item["description"]}',
        reply_markup=keyboard.keyboard,
    )


async def coincidence_answer(message, item):
    image = parser_movies.upload_image(item["poster"])
    await message.answer("Фильм есть у второго пользователя!")
    await message.answer_photo(
        types.BufferedInputFile(image, filename="poster.jpg"),
        caption=f'Название: {item["name"]}'
        f'\nГод: {item["year"]}'
        f'\nОписание: {item["description"]}',
    )
    await message.answer("Приятного просмотра")
