from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def department_kb(all_departments):

    builder = ReplyKeyboardBuilder()

    reply_keyboard = []

    for department in all_departments:
        builder.add(KeyboardButton(text=f"{department}"))
    builder.adjust(2)

    keyboard = builder.as_markup(resize_keyboard=True)

    return keyboard
