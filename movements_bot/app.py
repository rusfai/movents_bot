
import asyncio
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.methods import DeleteWebhook
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardMarkup
import datetime

from index import TOKEN
from handlers.start import start_router
from handlers.inline_search import inline_search_router
from handlers.update_car_handler import update_router
from db import init_db, update_cars_from_1c
from folder_1c.parse_car import get_cars
from handlers.movent_car import movent_car_router
from handlers.all_text import all_text_router
from handlers.cancel_handler import cancel_router
from handlers.get_movents import excel_router
from commands import set_commands

bot = Bot(token=TOKEN)

async def main():
    
    all_1c_cars = await get_cars()
    await update_cars_from_1c(all_1c_cars)

    

    await set_commands(bot)


    dp = Dispatcher()

    
    dp.include_routers(excel_router,
                       inline_search_router,
                       start_router,
                       update_router,
                       movent_car_router,
                       cancel_router,
                       all_text_router,
                       
                       )
    

    bot_info = await bot.get_me()
    print(f"https://t.me/{bot_info.username} запущен успешно! ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(init_db())
    asyncio.run(main())
    

