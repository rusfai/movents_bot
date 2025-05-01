import asyncio
from aiogram import types, F, Router
from aiogram.filters import Command
from db import check_cars_movents
from excel import create_excel_report
from aiogram.types import FSInputFile
import datetime

excel_router = Router()

@excel_router.message(Command("excel"))
async def start_handler(message: types.Message):
    await message.answer('Отправка отчета')

    movents_list = await check_cars_movents(datetime.date.today())

    file_path = await create_excel_report(movents_list)
    document = FSInputFile(file_path)
    await message.bot.send_document(message.from_user.id, document)
