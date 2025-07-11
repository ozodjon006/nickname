# keyboards/inline.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def gender_inline():
    return InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton("👨 Erkak", callback_data="gender_male"),
        InlineKeyboardButton("👩 Ayol", callback_data="gender_female"),
        InlineKeyboardButton("👶 Bolalar", callback_data="gender_kids")
    )

def nickname_variants_inline(variants):
    markup = InlineKeyboardMarkup(row_width=1)
    for i, variant in enumerate(variants):
        markup.add(
            InlineKeyboardButton(
                variant,          # Userga ko‘rinadigan uzun nom
                callback_data=f"select_{i}"   # Faqat index
            )
        )
    return markup
