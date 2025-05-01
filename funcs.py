import asyncio

async def dell_inline_keyboards(event, user_data, dell_list):
    
    for key in dell_list:
        
        if key in user_data:
        
            await event.bot.edit_message_reply_markup(
                chat_id=event.from_user.id,
                message_id=user_data[key], 
                reply_markup=None
            )

            user_data.pop(key, None)

    return user_data