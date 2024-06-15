from aiogram import Router
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart

from app.keyboards.user_kb import main_kb
from app.keyboards.admin_kb import admin_kb

from ..settings.settings import Settings


router = Router()

settings = Settings()

@router.message(CommandStart())
async def cmd_start(message: Message):
    if message.from_user.id in settings.getAdminIds():
        await message.answer(f'Welcome {message.from_user.first_name}', reply_markup=admin_kb.adminPanel)
    else:
        await message.answer(f'Welcome to our store {message.from_user.first_name}', reply_markup=main_kb.main_kb)
