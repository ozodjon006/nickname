from aiogram import types, Dispatcher

async def show_saved(message: types.Message):
    await message.answer("📁 Saqlangan nickname’lar hozircha yo‘q.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_saved, lambda msg: msg.text == "💾 Saqlanganlar")
