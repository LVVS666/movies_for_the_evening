# Телеграм Бот для Подбора Фильмов

Этот бот для Телеграма создан для двух пользователей. Он предлагает случайные фильмы с КиноПоиска и позволяет пользователям решить, хотят ли они смотреть этот фильм вместе или нет.

## Особенности

- Получение случайных фильмов с КиноПоиска.
- Возможность пользователей выбрать "Смотреть" или "Не смотреть" фильм.
- Подсчет совпадающих выборов пользователей для принятия решения о просмотре фильма.

## Требования

Для работы бота необходимы следующие библиотеки Python:

- aiogram==3.0.0b7
- kinopoisk-dev==0.2.0
- requests~=2.28.2
- Pillow~=9.4.0
- python-dotenv~=1.0.0

## Установка и Использование

Установите необходимые библиотеки, используя pip:

- pip install -r requirements.txt

Создайте файл .env в корневой директории проекта и укажите в нем токен вашего Телеграм бота и Токен КиноПоиска:
- BOT_TOKEN = YOUR_TOKEN
- KINO_TOKEN = YOUR_TOKEN

Запустите бота с помощью следующей команды:

- python3 bot_add_movies.py
