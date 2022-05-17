from aiogram.dispatcher.filters.state import StatesGroup, State


class Search(StatesGroup):
    sklad = State()
    art = State()
    order = State()
    show_all = State()

