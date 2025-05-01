import asyncio
from aiogram import types, F, Router
from aiogram.filters import Command
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from db import check_db_cars

inline_search_router = Router()

@inline_search_router.inline_query()
async def show_user_links(inline_query: InlineQuery):

    query_offset = int(inline_query.offset) if inline_query.offset else 0

    query_text = inline_query.query or ''
    db_result = await check_db_cars(query_text, offset=query_offset, limit=50)
 
    results = []
    for car in db_result:
        info = db_result[car]

        if info[0].split()[0].lower() == 'lada':
            thumbnail_url = 'https://www.sostav.ru/app/public/images/news/2015/03/30/compressed/Lada_logo.jpg'

        elif info[0].split()[0].lower() == 'volkswagen' or info[0].split()[0].lower() == 'solaris':
            thumbnail_url = 'https://koleso.ru/articles/wp-content/uploads/2023/08/%D0%9E%D0%B1%D0%BB%D0%BE%D0%B6%D0%BA%D0%B0-5.jpg'

        elif info[0].split()[0].lower() == 'nissan':
            thumbnail_url = 'https://a.d-cd.net/LuyleZpD_CZZnWzs5d9qH0vwUrQ-960.jpg'

        elif info[0].split()[0].lower() == 'hyundai':
            thumbnail_url = 'https://main-cdn.sbermegamarket.ru/big2/hlr-system/-21/503/474/761/916/19/600018773092b0.jpg'

        elif info[0].split()[0].lower() == 'renault':
            thumbnail_url = 'https://storage.googleapis.com/wp-resources/srovnator.cz/ng/2022/06/renault-og.jpg'

        elif info[0].split()[0].lower() == 'skoda':
            thumbnail_url = 'https://avatars.mds.yandex.net/i?id=dedda1dd57c13556d9820e9d0a1cfc19_l-5906106-images-thumbs&n=13'
        
        elif info[0].split()[0].lower() == 'haval':
            thumbnail_url = 'https://avatars.mds.yandex.net/get-altay/10261179/2a0000019058b5b07126e35fddd11f5cce59/XXXL'

        elif info[0].split()[0].lower() == 'datsun':
            thumbnail_url = 'https://w220301-4481.webasyst.cloud/wa-data/public/photos/69/01/169/169.970.jpg'

        elif info[0].split()[0].lower() == 'kia':
            thumbnail_url = 'https://cdn1.flamp.ru/e26056117ee3a4954b9261434b488006.png'

        elif info[0].split()[0].lower() == 'cherry':
            thumbnail_url = 'https://avangard-avto.com/wp-content/uploads/2022/12/Chery-%D0%A7%D0%B5%D1%80%D0%B8.png'


        else:
            thumbnail_url = ''
    
        
        results.append(
            InlineQueryResultArticle(
                id=car,  # ссылки у нас уникальные, потому проблем не будет
                title=car,
                description=f"{info[0]} {info[1]} {info[2]} {info[3]}",
                input_message_content=InputTextMessageContent(
                    message_text=car),
                thumbnail_url=thumbnail_url
                    )
                

        )

    if results:
        if len(results) < 50:
    
            # Результатов больше не будет, next_offset пустой
            await inline_query.answer(results, is_personal=True, next_offset="")
        else:
        
            # Ожидаем следующую пачку
            await inline_query.answer(results, is_personal=True, next_offset=str(query_offset+50))