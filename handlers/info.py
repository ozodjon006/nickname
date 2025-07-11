# handlers/info.py

from aiogram import types, Dispatcher
from keyboards.default import main_menu

async def show_info(message: types.Message):
    await message.answer("ℹ️ Bu bot sizga random nickname yaratishda yordam beradi.", reply_markup=main_menu)

def register_handlers_info(dp: Dispatcher):
    dp.register_message_handler(show_info, lambda msg: msg.text == "ℹ️ Ma'lumot")
