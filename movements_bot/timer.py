
import asyncio

from aiogram import types, F, Router
from aiogram.filters import Command
from db import check_cars_movents
from excel import create_excel_report
from aiogram.types import FSInputFile
import datetime
from app import bot
from index import copy_group


async def main():
    a = 0
    while True:

        movents_list = await check_cars_movents(datetime.date.today())

        file_path = await create_excel_report(movents_list)
        document = FSInputFile(file_path)
        await bot.send_document(copy_group, document)



        print(a)
        
        a+=1
        await asyncio.sleep(86400)
        

if __name__ == "__main__":
    asyncio.run(main())

