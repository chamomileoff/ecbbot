from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile


from filters.chat_types import ChatTypeFilter
from random import choice
from common.artur_replies import replies
from common.artur import poshel


# user group router 
ug_router = Router()
ug_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

@ug_router.message(Command('start'))
async def start_group(message: types.Message):
    await message.answer('Как я попал в эту дырень... 😢\nНу ладно, вы можете опробовать мои функции с помощью команд! 😊')



@ug_router.message(Command('mem', ignore_case=True))
async def mem_cmd(message: types.Message):
    video = FSInputFile('media/mem.mp4')
    await message.answer('Смотрите все, какой смешной мем нашел! 🤣')
    await message.answer_video(video=video)
    
    
@ug_router.message(Command('artur', ignore_case=True))
async def artur_cmd(message: types.Message):
    await message.answer(choice(poshel))

counter = 0
@ug_router.message(F.from_user.id == 1823399849)
async def block_makaka(message: types.Message):
    counter += 1
    if counter % 6 == 0:
        await message.reply(choice(replies))

@ug_router.message(Command('about', ignore_case=True))
async def about_cmd(message: types.Message):
    await message.reply('Состав нашей дружной компании:\n\n👩 @llinniss - Starosta\n🧔‍♂️ @pisun28 - писюн28 подпивом\
            \n🐒 @I9thfloor - Արտուր ջան\n🧔‍♂️ @wakluv - машуня\n👩 @mashnkkkk - ваня\
            \n🧔‍♂️ @gonok7 - Максим гонок\n👩‍🏫 @alllls_ss - Алла Станиславовна\
                \n🔫 @Liptonggggggo - ваньк калаш\n🔪@NowEverybodyHateMe - Patrick Bateman')
    
    
@ug_router.message((F.text.lower() == 'смотрите как умею') & (F.from_user.id == 1214449387))
async def secret_cmd(message: types.Message):
    await message.answer("Рот @I9thfloor ебал")