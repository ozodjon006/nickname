# handlers/start.py

from aiogram import types, Dispatcher
from keyboards.default import main_menu
from data.dp import set_user_human


async def cmd_start(message: types.Message):
    # Odam ekanligini anglash (oddiy)
    if not message.from_user.is_bot:
        await set_user_human(message.from_user.id, True)
        text = "👋 Salom! Men Nickname botiman.\nQuyidan tanlang:"
    else:
        await set_user_human(message.from_user.id, False)
        text = "🤖 Siz bot ekansiz. Cheklangan funksiya."

    await message.answer(text, reply_markup=main_menu)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
