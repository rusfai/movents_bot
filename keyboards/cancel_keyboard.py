from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



cancel_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Отмена', callback_data='cancel')
                ]
            ]
        )
