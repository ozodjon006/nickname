from aiogram import types, Dispatcher

async def show_settings(message: types.Message):
    await message.answer("⚙ Sozlamalar hali faol emas.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_settings, lambda msg: msg.text == "⚙ Sozlamalar")
