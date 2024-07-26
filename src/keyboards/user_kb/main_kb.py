from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🛒Catalog')],
        [KeyboardButton(text='📜Orders')],
        [KeyboardButton(text='📱Contacts'), KeyboardButton(text='📃About Us')],
    ], resize_keyboard=True
)
