from aiogram.filters.state import State, StatesGroup


class UserState(StatesGroup):
    user_add_db_state = State()
