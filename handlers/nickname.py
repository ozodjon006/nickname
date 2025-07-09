from aiogram import types, Dispatcher
from services.generator import generate_nickname

async def handle_new_nickname(message: types.Message):
    nickname = generate_nickname()
    await message.answer(f"🆕 Siz uchun nickname: `{nickname}`", parse_mode='Markdown')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_new_nickname, lambda msg: msg.text == "🆕 Yangi Nickname")
