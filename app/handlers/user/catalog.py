from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards.user_kb import buying_kb, catalog_kb
from ...db.orm import Orm


router = Router()
orm = Orm()

@router.message(F.text == '🛒Catalog')
async def catalog(message: Message):
    await message.answer('Brand catalog', reply_markup=catalog_kb.catalog_brands_kb())


@router.callback_query(F.data.startswith('brand_'))
async def callback_brand(callback: CallbackQuery):
    brand = callback.data.split('_')[1]

    await callback.answer(f'You selected {brand} clothing')
    await callback.message.answer(f'{brand} clothing', reply_markup=catalog_kb.select_items(brand))


@router.callback_query(F.data.startswith('sneakers_'))
async def callback_sneakers_item(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    items = orm.get_items_for_brand_and_item(brand, 'sneakers')
    
    await callback.answer(f'{brand} sneakers')
    await callback.message.answer(f'{brand} sneakers')

    if items != None:
        for item in items:
            item_id = orm.get_id('sneakers', brand, item.modelName)
            await callback.message.answer_photo(
                item.photo,
                f'Brand: {brand}\nModel: {item.modelName}\nSize: {item.size}\nPrice: <b>{item.price}$</b>',
                reply_markup=buying_kb.buy_btn(str(item_id), str(callback.inline_message_id)),
                parse_mode='HTML'
            )
    else:
        await callback.message.answer('Such things do not exist yet😔')


@router.callback_query(F.data.startswith('t-shirts_'))
async def callback_tshirts_item(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    items = orm.get_items_for_brand_and_item(brand, 't-shirts')

    await callback.answer(f'{brand} t-shirts')
    await callback.message.answer(f'{brand} t-shirts')

    if items != None:
        for item in items:
            item_id = orm.get_id('t-shirts', brand, item.modelName)
            await callback.message.answer_photo(
                item.photo,
                f'Brand: {brand}\nModel: {item.modelName}\nSize: {item.size}\nPrice: <b>{item.price}$</b>',
                reply_markup=buying_kb.buy_btn(str(item_id), str(callback.inline_message_id)),
                parse_mode='HTML'
            )
    else:
        await callback.message.answer('Such things do not exist yet😔')


@router.callback_query(F.data.startswith('hoodies_'))
async def callback_hoodies_item(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    items = orm.get_items_for_brand_and_item(brand, 'hoodies')

    await callback.answer(f'{brand} hoodies')
    await callback.message.answer(f'{brand} hoodies')

    if items != None:
        for item in items:
            item_id = orm.get_id('hoodies', brand, item.modelName)
            await callback.message.answer_photo(
                item.photo,
                f'Brand: {brand}\nModel: {item.modelName}\nSize: {item.size}\nPrice: <b>{item.price}$</b>',
                reply_markup=buying_kb.buy_btn(str(item_id), str(callback.inline_message_id)),
                parse_mode='HTML'
            )
    else:
        await callback.message.answer('Such things do not exist yet😔')


@router.callback_query(F.data.startswith('jackets_'))
async def callback_jackets_item(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    items = orm.get_items_for_brand_and_item(brand, 'jackets')

    await callback.answer(f'{brand} jackets')
    await callback.message.answer(f'{brand} jackets')

    if items != None:
        for item in items:
            item_id = orm.get_id('jackets', brand, item.modelName)
            await callback.message.answer_photo(
                item.photo,
                f'Brand: {brand}\nModel: {item.modelName}\nSize: {item.size}\nPrice: <b>{item.price}$</b>',
                reply_markup=buying_kb.buy_btn(str(item_id), str(callback.inline_message_id)),
                parse_mode='HTML'
            )
    else:
        await callback.message.answer('Such things do not exist yet😔')


@router.callback_query(F.data.startswith('longsleeves_'))
async def callback_longsleeves_item(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    items = orm.get_items_for_brand_and_item(brand, 'longsleeves')

    await callback.answer(f'{brand} longsleeves')
    await callback.message.answer(f'{brand} longsleeves')

    if items != None:
        for item in items:
            item_id = orm.get_id('longsleeves', brand, item.modelName)
            await callback.message.answer_photo(
                item.photo,
                f'Brand: {brand}\nModel: {item.modelName}\nSize: {item.size}\nPrice: <b>{item.price}$</b>',
                reply_markup=buying_kb.buy_btn(str(item_id), str(callback.inline_message_id)),
                parse_mode='HTML'
            )
    else:
        await callback.message.answer('Such things do not exist yet😔')