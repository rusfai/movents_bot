from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



start_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='❗Выберите Нейросети:❗', callback_data=f"11"),],
                [
                    InlineKeyboardButton(text='Chat GPT 4.1', callback_data=f"11"),
                    InlineKeyboardButton(text='OpenAI o4-mini', callback_data=f"11")
                ],

                [
                    InlineKeyboardButton(text='Chat GPT 4.1-min (Поиск в интернете)', callback_data=f"11")
                ],


                [
                    InlineKeyboardButton(text='Midjoyrney', callback_data=f"11")
                ],
                [
                    InlineKeyboardButton(text='Продолжить ⬇️', callback_data=f"1")
                ]
        ])




start_kb2 = InlineKeyboardMarkup(
            inline_keyboard=[

                [
                    InlineKeyboardButton(text='✅Chat GPT 4.1', callback_data=f"1"),
                    InlineKeyboardButton(text='OpenAI o4-mini', callback_data=f"1")
                ],

                [
                    InlineKeyboardButton(text='✅Chat GPT 4.1-min (Поиск в интернете)', callback_data=f"1")
                ],


                [
                    InlineKeyboardButton(text='Midjoyrney', callback_data=f"1")
                ],

                [InlineKeyboardButton(text='❗Выберите план:❗', callback_data=f"15"),],
                [
                    InlineKeyboardButton(text='Mini', callback_data=f"2"),
                    InlineKeyboardButton(text='Starter', callback_data=f"2"),
                ],
                [
                    InlineKeyboardButton(text='Premium', callback_data=f"2"),
                    InlineKeyboardButton(text='Ultima', callback_data=f"2")
                ]

                # [InlineKeyboardButton(text='Выберите дни ⬇️', callback_data=f"12"),],
                # [
                #     InlineKeyboardButton(text='7', callback_data=f"1"),
                #     InlineKeyboardButton(text='30', callback_data=f"1"),
                #     InlineKeyboardButton(text='180', callback_data=f"1"),
                #     InlineKeyboardButton(text='365', callback_data=f"1")
                # ],

                # [InlineKeyboardButton(text='Нейросети ⬇️', callback_data=f"1"),],
                # [
                #     InlineKeyboardButton(text='Chat GPT 4.1', callback_data=f"1"),
                #     InlineKeyboardButton(text='OpenAI o4-mini', callback_data=f"1")
                # ],

                # [
                #     InlineKeyboardButton(text='Chat GPT 4.1-min (Поиск в интернете)', callback_data=f"1")
                # ],


                # [
                #     InlineKeyboardButton(text='Midjoyrney', callback_data=f"1")
                # ]
            ]
        )




start_kb3 = InlineKeyboardMarkup(
            inline_keyboard=[

                [
                    InlineKeyboardButton(text='✅Chat GPT 4.1', callback_data=f"12"),
                    InlineKeyboardButton(text='OpenAI o4-mini', callback_data=f"21")
                ],

                [
                    InlineKeyboardButton(text='✅Chat GPT 4.1-min (Поиск в интернете)', callback_data=f"21")
                ],


                [
                    InlineKeyboardButton(text='Midjoyrney', callback_data=f"12")
                ],

                [
                    InlineKeyboardButton(text='Mini', callback_data=f"22"),
                    InlineKeyboardButton(text='Starter', callback_data=f"22")
                ],
                [
                    InlineKeyboardButton(text='✅Premium', callback_data=f"22"),
                    InlineKeyboardButton(text='Ultima', callback_data=f"22")
                ],

                [InlineKeyboardButton(text='❗Выберите дни:❗', callback_data=f"12"),],
                [
                    InlineKeyboardButton(text='7 - 180р', callback_data=f"3"),
                    InlineKeyboardButton(text='30 - 180р', callback_data=f"3")
                ],
                [
                    InlineKeyboardButton(text='180 - 180р', callback_data=f"3"),
                    InlineKeyboardButton(text='365 - 180р', callback_data=f"3")
                ],

            ]
        )

