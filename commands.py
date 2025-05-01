from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault


user_commands = [
    BotCommand(command='start', description='♻️ Перезапустить бота'),
    BotCommand(command='excel', description='Отчет'),
]



async def set_commands(bot: Bot):  
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
    
