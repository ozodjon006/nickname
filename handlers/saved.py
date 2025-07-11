from aiogram import types, Dispatcher
from keyboards.default import main_menu
from data.dp import get_nicknames   # << to'g'ri import

async def show_saved(message: types.Message):
    nicknames = await get_nicknames(message.from_user.id)  # << await muhim!

    if nicknames:
        text = "<b>📂 Saqlangan nickname’lar:</b>\n\n"
        for i, nick in enumerate(nicknames, start=1):
            text += f"{i}. <code>{nick}</code>\n"
        await message.answer(text, parse_mode="HTML", reply_markup=main_menu)
    else:
        await message.answer("📂 Sizda hali saqlangan nickname yo‘q!", reply_markup=main_menu)

def register_handlers_saved(dp: Dispatcher):
    dp.register_message_handler(show_saved, lambda msg: msg.text == "📂 Saqlanganlar")
