import asyncio
from aiogram import types, F, Router
from aiogram.filters import Command
from typing import Union, Dict, Any
from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
import datetime
from typing import List
from db import check_departments, check_car, change_department, change_car_year
from keyboards.department_keyboard import department_kb
from states import movent_states
from keyboards.cancel_keyboard import cancel_kb
from keyboards.accept_keyboard import accept_kb
from keyboards.start_keyboard import start_kb
from keyboards.pass_year import pass_year_kb

from funcs import dell_inline_keyboards
from index import copy_group
from aiogram_media_group import media_group_handler
#Проверка, яыляется ли номером машины
class IsItCarNumber(BaseFilter):
    async def __call__(self, message: types.Message):
        
        if len(message.text) in [7,8,9] and message.text[1].isdigit() and message.text[2].isdigit() and message.text[3].isdigit():
            return {'car_number': message.text}
        
        return False
    

movent_car_router= Router()

@movent_car_router.message(F.text, IsItCarNumber())
async def movent_handler(message: types.Message, car_number: str, state: FSMContext):

    
    car_info = await check_car(message.text)

    await state.update_data(car_number=message.text.upper())
    await state.update_data(from_department=car_info[5])

    #Чтобы потом удалить инлайн клавиатуру
    info_message = await message.answer(text=f'Номер: {car_info[1]}\nМодель: {car_info[2]}\nГод: {car_info[3]}\nЦвет: {car_info[4]}\nДепартамент: {car_info[5]}', reply_markup=cancel_kb)   

    await state.update_data(dell_keyboard_info_message_id=info_message.message_id)

    #Если год авто не выбран
    if int(car_info[3]) == 0:
        await state.set_state(movent_states.year)
        
        year_mess = await message.answer(text='Введите год выпуска автомобиля', reply_markup=pass_year_kb)

        await state.update_data(dell_keyboard_yaer_message_id=year_mess.message_id)

    else:
         
        department = await check_departments()
        department_keyboard = await department_kb(department)

        await state.set_state(movent_states.department)
        
        await message.answer(text='Выберите департамент, куда перемещается машина. Или введите свой', reply_markup=department_keyboard)   
    


@movent_car_router.message(movent_states.year)
async def choose_department(message: types.Message, state: FSMContext):

    user_data = await state.get_data()

    user_data = await dell_inline_keyboards(message, user_data, ['dell_keyboard_yaer_message_id'])
    await state.set_data(user_data)  

    if message.text.isdigit():

        car_number = user_data['car_number']

        await change_car_year(car_number, int(message.text))
        
        department = await check_departments()
        department_keyboard = await department_kb(department)

        await state.set_state(movent_states.department)
    
        await message.answer(text=f'Год машины {car_number} изменен на {message.text}')

        await message.answer(text='Выберите департамент, куда перемещается машина. Или введите свой', reply_markup=department_keyboard)

    else:

        year_mess = await message.answer(text='Введите только число', reply_markup=pass_year_kb)

        await state.update_data(dell_keyboard_yaer_message_id=year_mess.message_id)



@movent_car_router.callback_query(F.data == 'pass_year')
async def accept_handler(callback_query: types.CallbackQuery, state: FSMContext):
    
    
    user_data = await state.get_data()
    user_data = await dell_inline_keyboards(callback_query, user_data, ['dell_keyboard_yaer_message_id'])
    await state.set_data(user_data) 


    
    department = await check_departments()
    department_keyboard = await department_kb(department)

    await state.set_state(movent_states.department)

    await callback_query.message.answer(text='Выберите департамент, куда перемещается машина. Или введите свой', reply_markup=department_keyboard)
    


@movent_car_router.message(movent_states.department)
async def choose_department(message: types.Message, state: FSMContext):
        
    user_data = await state.get_data()
    user_data = await dell_inline_keyboards(message, user_data, ['dell_keyboard_info_message_id'])
    await state.set_data(user_data) 


    if 'yaer_message_id' in user_data:
        await message.bot.delete_message(chat_id=message.from_user.id, message_id=user_data['yaer_message_id'])
    
    department = message.text

    await state.update_data(to_department=department)

    await state.set_state(movent_states.movent_price)

    await message.answer(text=f"Выбранный департамент: {department}", reply_markup=ReplyKeyboardRemove())
    price_message = await message.answer(text=f"Введите цену перемещения машины", reply_markup=cancel_kb)
    await state.update_data(dell_keyboard_price_message_id=price_message.message_id)



@movent_car_router.message(movent_states.movent_price)
async def movent_price(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_data = await dell_inline_keyboards(message, user_data, ['dell_keyboard_price_message_id'])
    await state.set_data(user_data) 

    if message.text.isdigit():
        await state.update_data(movent_price=int(message.text))
        

        await message.answer(text=f"Номер машины: {user_data['car_number']}\nПеремешение: {user_data['from_department']} --> {user_data['to_department']}\nЦена перемещения: {int(message.text)}", reply_markup=accept_kb)

    else:
        price_message = await message.answer(text=f"Введите только число", reply_markup=cancel_kb)
        await state.update_data(dell_keyboard_price_message_id=price_message.message_id)



@movent_car_router.callback_query(F.data == 'accept')
async def accept_handler(callback_query: types.CallbackQuery, state: FSMContext):
    
    await callback_query.message.delete_reply_markup()

    user_data = await state.get_data()

    await change_department(user_data['car_number'], user_data['from_department'], user_data['to_department'], datetime.date.today(), user_data['movent_price'])
    

    await state.set_state(movent_states.wait_photo)

    await callback_query.message.answer(f'''Пришлите фото машины одним сообщением''')


@movent_car_router.message(F.media_group_id, movent_states.wait_photo)
@media_group_handler
async def photo(messages: List[types.Message], state: FSMContext):
    
    user_data = await state.get_data()
    
    list_id = []
    for one_message in messages:
        list_id.append(int(one_message.message_id))
        mess = one_message
    
    
    new_message = await mess.bot.copy_messages(from_chat_id=mess.from_user.id, message_ids=list_id, chat_id=copy_group)

    await mess.bot.edit_message_caption(chat_id=copy_group, message_id=new_message[0].message_id, caption=f"Номер машины: {user_data['car_number']}\nПеремешение: {user_data['from_department']} --> {user_data['to_department']}\nЦена перемещения: {user_data['movent_price']}", parse_mode='html')

    await mess.bot.send_message(chat_id=mess.from_user.id, text=f'''Департамент машины {user_data['car_number']} изменен с {user_data['from_department']} на {user_data['to_department']}''', reply_markup=start_kb)


    await state.clear()

    
@movent_car_router.message(movent_states.wait_photo)
async def no_photo(message: types.Message, state: FSMContext):
    await message.answer(f'''Пришлите несколько фото машины одним сообщением''')