from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ...db.orm import Orm


items = [('👕T-shirts', 't-shirts'), ('👘Hoodies', 'hoodies'), ('👟Sneakers', 'sneakers'), ('🧥Jackets', 'jackets'),('👘Longsleeves','longsleeves')]


def catalog_brands_kb():
    btns = [[InlineKeyboardButton(text=brand, callback_data='brand_' + brand)] for brand in Orm().get_brands()]

    return InlineKeyboardMarkup(inline_keyboard=btns)


def select_items(brand: str):
    btns = [[InlineKeyboardButton(text=item[0], callback_data=f'{item[1]}_{brand}') ]for item in items]

    return InlineKeyboardMarkup(inline_keyboard=btns)
