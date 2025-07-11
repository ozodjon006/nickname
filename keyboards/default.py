# keyboards/default.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🆕 Yangi Nickname"),
            KeyboardButton("📂 Saqlanganlar")
        ],
        [
            KeyboardButton("⚙️ Sozlamalar"),
            KeyboardButton("ℹ️ Ma'lumot")
        ]
    ],
    resize_keyboard=True
)
