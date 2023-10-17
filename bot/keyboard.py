from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

kb = [
    [KeyboardButton(text='Смотреть')],
    [KeyboardButton(text='Не смотреть')]
      ]

keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
