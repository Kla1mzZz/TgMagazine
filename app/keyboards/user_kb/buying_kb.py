from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ...db.orm import Orm

from ...settings.settings import create_paypal_payment


orm = Orm()

def buy_btn(id, message_id):
    btn = InlineKeyboardButton(text='Buy', callback_data='buy_' + id + '_' + message_id)
    
    return InlineKeyboardMarkup(inline_keyboard=[[btn]])


def select_size(id, message_id):
    
    sizes = orm.get_item_for_id(id)
    print(id)

    formattedSizes = sizes.size.split(',')
    print(formattedSizes)

    btns = [[InlineKeyboardButton(text=size, callback_data='id_' + id + '_' + size + '_' + message_id)] for size in formattedSizes]

    return InlineKeyboardMarkup(inline_keyboard=btns)


def order(id, size):
    btns = [[InlineKeyboardButton(text='Place Order', callback_data='order_' + id + '_' + size)]]

    return InlineKeyboardMarkup(inline_keyboard=btns)


def select_pay(id,user_id):
    item = orm.get_item_for_id(id)
    payment = create_paypal_payment(item.item, item.price)

    if payment.create():
        btns = [
            [InlineKeyboardButton(text='💳PayPal', callback_data='PayPal', url=payment['links'][1]['href']), 
             InlineKeyboardButton(text='💳MasterCard-Visa', callback_data='MasterCard-Visa', url='')],
            [InlineKeyboardButton(text='✔Paid', callback_data='Paid_'+str(user_id))]
        ]

    return InlineKeyboardMarkup(inline_keyboard=btns)