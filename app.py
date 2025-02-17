import asyncio, os
from dotenv import load_dotenv, find_dotenv
from handlers.user_private import up_router
from handlers.user_group import ug_router
from common.bot_cmds_list import private

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllGroupChats

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(up_router)
dp.include_router(ug_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllGroupChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    

asyncio.run(main())