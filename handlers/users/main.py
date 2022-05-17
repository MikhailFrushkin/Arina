from pathlib import Path

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, File, Message
import requests
import bot
from data.config import ADMINS, BOT_TOKEN
from loader import dp, bot


@dp.message_handler(commands=['start'], state='*')
async def bot_start(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer('Добро пожаловать в Админ-Панель! Выберите действие на клавиатуре')
    else:
        await message.answer('Добро пожаловать, {}!')


async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = r"C:\Users\Arina\files"

    await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)


@dp.message_handler(content_types=['text'], state='*')
async def bot_message(message: types.Message, state: FSMContext):
    if message.text == 'Привет':
        await bot.send_message(message.from_user.id, 'И тебе привет')
    else:
        await bot.send_message(message.from_user.id, message.text)
