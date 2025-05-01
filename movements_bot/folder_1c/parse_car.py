
import asyncio
from aiohttp import ClientSession, BasicAuth
import json

from index import car_1c_url, user_1c, password_1c



async def get_cars():
    # передаём BasicAuth при создании сессии
    auth = BasicAuth(login=user_1c, password=password_1c, encoding='utf-8')
    async with ClientSession(auth=auth) as session:
        async with session.get(car_1c_url) as resp:
            resp.raise_for_status()
            text = await resp.text()
            json_resp = json.loads(text)
            car_list = {}
            for car in json_resp:
                car_list[car['Number']] = [car['Model'], 0, car['BodyColor'], car['Department']]

    
            return car_list




