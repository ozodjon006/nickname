from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers import start, nickname, saved, settings, info
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Handlerlarni ro‘yxatdan o‘tkazamiz
start.register_handlers(dp)
nickname.register_handlers(dp)
saved.register_handlers(dp)
settings.register_handlers(dp)
info.register_handlers(dp)

async def on_startup(dp):
    print("✅ Bot ishga tushdi!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
