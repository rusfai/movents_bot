from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class movent_states(StatesGroup):
    year = State()
    department = State()
    movent_price = State()
    wait_photo = State()