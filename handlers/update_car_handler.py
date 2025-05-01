import asyncio
from aiogram import types, F, Router
from aiogram.filters import Command

from folder_1c.parse_car import get_cars
from db import update_cars_from_1c


update_router = Router()

@update_router.message(Command("update"))
async def start_handler(message: types.Message):

    all_1c_cars = await get_cars()
    await update_cars_from_1c(all_1c_cars)

    message.answer('Список машин обновлен')