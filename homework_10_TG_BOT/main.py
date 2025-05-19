import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import user_handler

from homework_10_TG_BOT.bot_config import bot

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(user_handler.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())