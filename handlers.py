from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def send_welcome(message: Message):
    await message.answer("Привет! Теперь бот запущен и периодически будет присылать несколько английских слов с переводом")


@router.message()
async def message(message: Message):
    await message.answer("Ага")