from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



accept_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Подтвердить', callback_data='accept')
                ],
                [
                    InlineKeyboardButton(text='Отмена', callback_data='cancel')
                ]              
            ]
        )
