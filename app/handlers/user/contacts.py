from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text == '📱Contacts')
async def about_us(message: Message):
    await message.answer('Our support account @ResemberovSupport')
