from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile, InputFile


from filters.chat_types import ChatTypeFilter
from random import choice, randint
import os
from common.artur_replies import replies
from common.artur import poshel


# user group router 
FOLDER = 'media'
TARGET_USER_ID = 1823399849
ug_router = Router()
ug_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

@ug_router.message(Command('start'))
async def start_group(message: types.Message):
    await message.answer('Как я попал в эту дырень... 😢\nНу ладно, вы можете опробовать мои функции с помощью команд! 😊')



@ug_router.message(Command('mem', ignore_case=True))
async def mem_cmd(message: types.Message):
    await message.answer('Смотрите все, какой смешной мем нашел! 🤣')
    files = os.listdir(FOLDER)
    if not files:
        await message.reply("В папке нет файлов!")
        return

    file_name = choice(files)
    file_path = os.path.join(FOLDER, file_name)

    # Используем FSInputFile вместо InputFile
    file = FSInputFile(file_path)

    if file_name.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
        await message.answer_video(file)
    elif file_name.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp")):
        await message.answer_photo(file)
    else:
        await message.reply("Файл не поддерживается!")
    
@ug_router.message(Command('artur', ignore_case=True))
async def artur_cmd(message: types.Message):
    await message.answer(choice(poshel))

# Счётчик сообщений
user_message_count = 0

@ug_router.message()
async def message_makake(message: types.Message):
    global user_message_count

    if message.from_user.id == TARGET_USER_ID:
        user_message_count += 1  # Увеличиваем счётчик

        # Если достигли случайного числа от 7 до 10
        if user_message_count >= randint(7, 10):
            await message.answer(choice(replies))  # Текст можно поменять
            user_message_count = 0  # Сбрасываем счётчик

@ug_router.message(Command('about', ignore_case=True))
async def about_cmd(message: types.Message):
    await message.reply('Состав нашей дружной компании:\n\n👩 @llinniss - Starosta\n🧔‍♂️ @pisun28 - писюн28 подпивом\
            \n🐒 @I9thfloor - Արտուր ջան\n🧔‍♂️ @wakluv - машуня\n👩 @mashnkkkk - ваня\
            \n🧔‍♂️ @gonok7 - Максим гонок\n👩‍🏫 @alllls_ss - Алла Станиславовна\
                \n🔫 @Liptonggggggo - ваньк калаш\n🔪@NowEverybodyHateMe - Patrick Bateman')
    
    
@ug_router.message((F.text.lower() == 'смотрите как умею') & (F.from_user.id == 1214449387))
async def secret_cmd(message: types.Message):
    await message.answer("Рот @I9thfloor ебал")