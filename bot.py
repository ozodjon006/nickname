# bot.py
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

from handlers import start, nickname, saved, settings, info
from data.dp import init_db

import asyncio

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)

# FSM uchun storage
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

start.register_handlers_start(dp)
nickname.register_handlers_nickname(dp)
saved.register_handlers_saved(dp)
settings.register_handlers_settings(dp)
info.register_handlers_info(dp)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
    executor.start_polling(dp, skip_updates=True)
