from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from ...db.orm import Orm

adminPanel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Add New Brand 🆕'), KeyboardButton(text='All Brands 📋'), KeyboardButton(text='Delete Brand ❌')],
        [KeyboardButton(text='Add New Item 🛒')],
        [KeyboardButton(text='Admin Panel 🛠️')]
    ], resize_keyboard=True, is_persistent=True
)

addItemKb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Yes ✅'), KeyboardButton(text='No ❌')]
    ]
)

nameItemKb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='T-shirts 👕'), KeyboardButton(text='Longsleeves 👕'), KeyboardButton(text='Hoodies 🧥')],
        [KeyboardButton(text='Jackets 🧥'), KeyboardButton(text='Sneakers 👟')]
    ], resize_keyboard=True
)

def brandItemKb():
    btns = [[KeyboardButton(text=brand)] for brand in Orm().get_brands()]
    return ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True, is_persistent=True)

def verification_payment(user_id):
    btns = [[InlineKeyboardButton(text='Confirm ✅', callback_data='confirm_' + str(user_id)),
             InlineKeyboardButton(text='Do Not Confirm ❌', callback_data='cancel_' + str(user_id))]]
    return InlineKeyboardMarkup(inline_keyboard=btns)

def webapp_builder():
    btns = [[InlineKeyboardButton(text='Admin Panel 🛠️', web_app=WebAppInfo(url='https://787e-46-211-72-121.ngrok-free.app'))]]
    return InlineKeyboardMarkup(inline_keyboard=btns)

