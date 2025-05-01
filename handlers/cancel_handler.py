import asyncio
from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from keyboards.start_keyboard import start_kb
from aiogram.types import ReplyKeyboardRemove

cancel_router = Router()

@cancel_router.callback_query(F.data == 'cancel')
async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.delete_reply_markup()
    user_data = await state.get_data()
    print(user_data)
    for key in user_data:
        print(key)
        if key.split('_')[0] == 'dell':
            
            try:
                await callback_query.bot.edit_message_reply_markup(
                    chat_id=callback_query.from_user.id,
                    message_id=user_data[key], 
                    reply_markup=None
                )

            except:
                pass
    await state.clear()

    await callback_query.message.answer('Действие отменено', reply_markup=ReplyKeyboardRemove())
    await callback_query.message.answer('Нажмите, чтобы начать поиск', reply_markup=start_kb)
   
    
