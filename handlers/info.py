from aiogram import types, Dispatcher

async def show_info(message: types.Message):
    await message.answer(
        "ℹ️ Bu bot siz uchun kreativ nickname lar yaratadi!\n\n"
        "🆕 — yangi nickname olish\n"
        "💾 — saqlanganlarni ko‘rish\n"
        "⚙ — sozlamalarni o‘zgartirish"
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_info, lambda msg: msg.text == "ℹ️ Maʼlumot")
