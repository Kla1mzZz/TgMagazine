import asyncio
from aiogram import Bot, Dispatcher

from dotenv import dotenv_values

from app.handlers import commands
from app.handlers.user import catalog, aboutUs, buying, contacts, orders
from app.handlers.admin import admin_panel

import logging


async def main():
    token = dotenv_values('.env').get('TOKEN')
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_routers(catalog.router, aboutUs.router, buying.router, admin_panel.router, commands.router, contacts.router,orders.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Бот запущен')
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())  
    except KeyboardInterrupt:
        print('Бот выключен')