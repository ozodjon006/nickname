# handlers/settings.py

from aiogram import types, Dispatcher
from keyboards.default import main_menu

async def show_settings(message: types.Message):
    text = "⚙️ Sozlamalar:\n"
    text += "- Til: 🇺🇿 O'zbek\n"
    text += "- Bezak turi: Jenskiy/Mujskoy/Detskiy\n"
    text += "- Is_human flag: ✅\n"
    text += "- Keyin professional variantlar qo‘shiladi!"
    await message.answer(text, reply_markup=main_menu)

def register_handlers_settings(dp: Dispatcher):
    dp.register_message_handler(show_settings, lambda msg: msg.text == "⚙️ Sozlamalar")
