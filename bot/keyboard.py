from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

kb = [
    [KeyboardButton(text='Cмотреть')],
    [KeyboardButton(text='Не смотреть')]
      ]

keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)