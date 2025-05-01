import asyncio
from aiogram import types, F, Router
from aiogram.filters import Command
from keyboards.start_keyboard import start_kb,start_kb2, start_kb3

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):

    text = '''
Выберите нейросеть:

🔥 OpenAI o4 mini — лучшая модель для кода, математики и наук 

🚀 GPT 4o mini — умная и быстрая, для работы с текстами

⚡️ Midjourney - ИИ для создания картинок
'''
    await message.answer(text, reply_markup=start_kb)


@start_router.callback_query(F.data == '1')
async def accept_handler(callback_query: types.CallbackQuery):
    


    text = '''

Выберите план

Mini:
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки


Starter:
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки


Premium:
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки


Ultima:
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
'''

    await callback_query.message.edit_text(text=text,reply_markup=start_kb2)


@start_router.callback_query(F.data == '2')
async def accept_handler(callback_query: types.CallbackQuery):
    
    text = '''
Mini:
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
Chat gpt 4.1 - 10 текстовых, 5 фото в сутки
'''


    await callback_query.message.edit_text(text=text, reply_markup=start_kb3)

@start_router.callback_query(F.data == '3')
async def accept_handler(callback_query: types.CallbackQuery):
    

    text = '1'
    await callback_query.message.edit_text(text=text,reply_markup=start_kb3)