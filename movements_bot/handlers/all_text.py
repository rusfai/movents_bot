import asyncio
from aiogram import types, F, Router

from keyboards.start_keyboard import start_kb


all_text_router= Router()

@all_text_router.message(F.text)
async def all_text_handler(message: types.Message):

    await message.answer('Нажми, чтобы начать поиск', reply_markup=start_kb)

