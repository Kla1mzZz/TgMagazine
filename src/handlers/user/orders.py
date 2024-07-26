from aiogram import Router, F
from aiogram.types import Message

from ...db.orm import Orm

router = Router()
orm = Orm()

@router.message(F.text == '📜Orders')
async def orders(message: Message):
    orders = orm.get_orders(f'@{message.from_user.username}')


    if orders:
        for order in orders:
            await message.answer_photo(order.photo, f'Order\nBrand: {order.brand}\nModel: {order.modelName}\nSize: {order.size}\n\nInformation:\nFullname: {order.fullName}\nPhone number: {order.phoneNumber}\nAddress: {order.address}'
                                                , parse_mode='HTML')
    else:
        await message.answer('You have no orders yet')