from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



pass_year_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Пропустить', callback_data='pass_year')
                ]
            ]
        )
