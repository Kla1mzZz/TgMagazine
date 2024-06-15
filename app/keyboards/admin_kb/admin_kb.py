from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from ...db.orm import Orm


adminPanel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить новый бренд'), KeyboardButton(text='Все Бренды'), KeyboardButton(text='Удалить бренд')],
        [KeyboardButton(text='Добавить новую вещь')],
        [KeyboardButton(text='Админ-панель')]
        
    ], resize_keyboard=True, is_persistent=True
)

addItemKb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Да'),KeyboardButton(text='Нет')]
    ]
)

nameItemKb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='T-shirts'), KeyboardButton(text='Longsleeves'),KeyboardButton(text='Hoodies'),],
        [KeyboardButton(text='Jackets'),KeyboardButton(text='Sneakers'),]
    ], resize_keyboard=True
)

def brandItemKb():
    btns = [[KeyboardButton(text=brand)] for brand in Orm().get_brands()]

    return ReplyKeyboardMarkup(keyboard=btns,resize_keyboard=True, is_persistent=True)


def verefication_payment(user_id):
    btns = [[InlineKeyboardButton(text='Подтвердить✅', callback_data='confirm_'+str(user_id)), 
             InlineKeyboardButton(text='Не подтверждать❌', callback_data='cancel'+str(user_id))]]
    
    return InlineKeyboardMarkup(inline_keyboard=btns)


def webapp_builder():
    btns = [[InlineKeyboardButton(text='Админ-панель', web_app=WebAppInfo(url='https://0658-91-242-199-38.ngrok-free.app/'))]]

    return InlineKeyboardMarkup(inline_keyboard=btns)