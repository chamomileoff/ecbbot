from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command


from filters.chat_types import ChatTypeFilter



# user private router
up_router = Router()
up_router.message.filter(ChatTypeFilter(['private']))

@up_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я бот двадцатичетырехдекабьской компании!🫶\nВыберите опцию по кнопке ниже ⬇️ (мне пока что впадлу)")
    

@up_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer('Да')
    

# @up_router.message(F.from_user.id == )