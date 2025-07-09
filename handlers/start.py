from aiogram import types, Dispatcher
from keyboards.default import main_menu

async def cmd_start(message: types.Message):
    await message.answer("👋 Salom! Men Nickname botiman.\nQuyidan tanlang:", reply_markup=main_menu)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
