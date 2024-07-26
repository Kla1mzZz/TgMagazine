from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext


from ...keyboards.user_kb import buying_kb
from ...keyboards.admin_kb import admin_kb
from ...FSM.states import AddOrderForm
from ...db.orm import Orm
from ...settings.settings import Settings



router = Router()
orm = Orm()
settings = Settings()



@router.callback_query(F.data.startswith('buy_'))
async def buy(callback: CallbackQuery):
    data = callback.data.split('_')
    print(data)

    await callback.message.edit_caption(inline_message_id=data[2],  caption='Select size', reply_markup=buying_kb.select_size(data[1], data[2]))

@router.callback_query(F.data.startswith('id_'))
async def select_size(callback: CallbackQuery):
    data = callback.data.split('_')

    item = orm.get_item_for_id(data[1])

    await callback.message.edit_caption(inline_message_id=data[3], caption=f'Your order\nBrand: {item.brand}\nModel: {item.modelName}\nSize: {data[2]}\nPrice: <b>{item.price}$</b>'
                                            ,reply_markup=buying_kb.order(data[1],data[2]), parse_mode='HTML')

@router.callback_query(F.data.startswith('order_'))
async def checkout_order(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddOrderForm.fullName)
    data = callback.data.split('_')

    await state.update_data(id=data[1], size=data[2])

    await callback.message.answer('Enter full name🖊: ')

@router.message(AddOrderForm.fullName)
async def order_full_name(message: Message, state: FSMContext):
    await state.update_data(fullName=message.text, user_id=message.from_user.id,username=f'@{message.from_user.username}')
    await state.set_state(AddOrderForm.phoneNumber)

    await message.answer('Enter phone number📱:')

@router.message(AddOrderForm.phoneNumber)
async def order_phone_number(message: Message, state: FSMContext):
    await state.update_data(phoneNumber=message.text)
    await state.set_state(AddOrderForm.address)
    
    await message.answer('Enter country, city, address, postal code📫:')

@router.message(AddOrderForm.address)
async def order_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    data = await state.get_data()
    print(data)
    await state.clear()

    item = orm.get_item_for_id(data['id'])

    await message.answer('Loading...')
    await message.answer('Select payment method:', reply_markup=buying_kb.select_pay(data['id'],data['user_id']))
    orm.add_verefication_order(item.item ,item.brand,item.modelName,data['size'],
                               item.price,item.photo,data['address'],data['fullName'],data['phoneNumber'],'waiting',data['user_id'], data['username'])

@router.callback_query(F.data.startswith('Paid_'))
async def verefication_pay(callback: CallbackQuery):
    user_id = callback.data.split('_')[1]

    await callback.message.answer('We will check within 15 minutes')

    order = orm.get_verefication_order(user_id)

    for id in settings.getAdminIds():
        await callback.message.bot.send_message(id, f'Пользователь хочет проверить оплату {order.username}',reply_markup=admin_kb.verification_payment(user_id))

@router.callback_query(F.data.startswith('confirm_'))
async def confirm_pay(callback: CallbackQuery):
    user_id = callback.data.split('_')[1]

    order = orm.get_verefication_order(user_id)

    
    orm.add_order(order.item,order.brand,order.modelName,order.size,order.price,order.photo,
                  order.fullName,order.phoneNumber,order.address,order.username)
    orm.delete_verefication_order(user_id)
    await callback.message.bot.send_message(int(user_id), 'Payment was successful✅')


@router.callback_query(F.data.startswith('cancel_'))
async def cancel_pay(callback: CallbackQuery):
    user_id = callback.data.split('_')[1]
    await callback.message.bot.send_message(int(user_id), 'Payment error❌')
