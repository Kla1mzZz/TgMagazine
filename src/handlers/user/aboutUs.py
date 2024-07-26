from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text == '📃About Us')
async def about_us(message: Message):
    await message.answer('Telegram store resemberov store\nDelivery across worldwide shipping')
