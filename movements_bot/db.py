import asyncio
import aiosqlite
from index import PATH

async def transliterate(word):

   # Слоаврь с заменами
   slovar = {'A':'А', 'B':'В', 'E':'Е', 'K':'К', 'M':'М', 'H':'Н', 'O':'О', 'P':'Р', 'C':'С', 'T':'Т', 'Y':'У', 'X':'Х', }
        
   # Циклически заменяем все буквы в строке
   for key in slovar:
      word = word.replace(key, slovar[key])
   return word

async def init_db():
    # Подключаемся к базе (файл создастся автоматически, если не существует)
    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        # Создаём таблицу car, если она ещё не существует
        await db.execute("""
            CREATE TABLE IF NOT EXISTS car (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT    NOT NULL,
                model  TEXT    NOT NULL,
                year   INTEGER NOT NULL,
                color  TEXT    NOT NULL,
                department TEXT NOT NULL
            );
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS movents (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                number TEXT    NOT NULL,
                from_department TEXT NOT NULL,
                to_department TEXT NOT NULL,
                date TEXT NOT NULL,
                price INTEGER NOT NULL
            );
        """)

        # Сохраняем изменения
        await db.commit()

async def update_cars_from_1c(car_list_1c):

    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        resp = await db.execute("""SELECT number FROM car""")
        cars_db_list = await resp.fetchall()
        filtt_db_cars = []

        for car in cars_db_list:
            filtt_db_cars.append(car[0].upper())

        for car_1c in car_list_1c.keys():
            car_1c = await transliterate(car_1c.upper())

            if car_1c not in filtt_db_cars:
                car_info = car_list_1c[car_1c]
                await db.execute("""INSERT INTO car (number, model, year, color, department) VALUES (?, ?, ?, ?, ?)""", (car_1c, car_info[0], car_info[1], car_info[2], car_info[3]))

        await db.commit()

        return True
    

async def check_db_cars(user_str, offset, limit):
    user_str = await transliterate(user_str.upper())
    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        resp = await db.execute("""SELECT * FROM car WHERE number LIKE (?) LIMIT (?) OFFSET (?)""", (f'{user_str}%', str(limit), str(offset)))
        cars_db_list = await resp.fetchall()
        filtt_db_cars = {}

        for car in cars_db_list:
            filtt_db_cars[car[1]] = [car[2], car[3], car[4], car[5]]


 
        return filtt_db_cars
    
async def check_departments():
    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        resp = await db.execute("""SELECT DISTINCT department FROM car""")
        all_department = await resp.fetchall()
        filtt_department = []

        for department in all_department:
            filtt_department.append(department[0])


        print(filtt_department)
        return filtt_department
    

async def check_car(car_number):
    car_number = await transliterate(car_number.upper())
    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        resp = await db.execute("""SELECT * FROM car WHERE number = (?)""", (car_number,))
        car = await resp.fetchone()

        return car
    
async def change_department(car_number, from_department, new_department, date, price):
    car_number = await transliterate(car_number.upper())
    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        await db.execute("""UPDATE car SET department = (?) WHERE number = (?)""", (new_department, car_number,))
        await db.execute("""INSERT INTO movents (number, from_department, to_department, date, price) VALUES (?, ?, ?, ?, ?)""", (car_number, from_department, new_department, date, price,))

        await db.commit()

        return None
    

async def change_car_year(car_number, year):
    car_number = await transliterate(car_number.upper())
    async with aiosqlite.connect(f'{PATH}\car.db') as db:
        await db.execute("""UPDATE car SET year = (?) WHERE number = (?)""", (year, car_number))

        await db.commit()

        return None
    
async def check_cars_movents(date):
    async with aiosqlite.connect(f'{PATH}\car.db') as db:

        all_movents_list = []

        resp = await db.execute("""SELECT * FROM movents WHERE date = (?)""", (date,))
        cars_db_list = await resp.fetchall()

        a = 1
        for car_mov in cars_db_list:
            print(car_mov)
            all_cars_info = await check_db_cars(car_mov[1], 0, 1)
            car_info = all_cars_info[car_mov[1]]
            all_movents_list.append([a, car_mov[1], car_info[0], car_info[1], car_info[2], car_mov[2], car_mov[3], car_mov[5]])

            a += 1

        return all_movents_list
    
