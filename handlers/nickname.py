# handlers/nickname.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.inline import gender_inline, nickname_variants_inline
from services.generator import generate_variants
from data.dp import add_nickname
from keyboards.default import main_menu

class NicknameStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_gender = State()
    waiting_for_variant = State()

async def new_nickname(message: types.Message):
    await message.answer("Ismni yuboring:")
    await NicknameStates.waiting_for_name.set()

async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(base_word=message.text.strip())
    await message.answer("Qaysi turdagi bezak?", reply_markup=gender_inline())
    await NicknameStates.waiting_for_gender.set()

async def process_gender(call: types.CallbackQuery, state: FSMContext):
    style = call.data.split("_")[1]
    data = await state.get_data()
    base_word = data['base_word']
    variants = generate_variants(base_word, style)
    await state.update_data(variants=variants)

    await call.message.answer(
        "Variantni tanlang:",
        reply_markup=nickname_variants_inline(variants)
    )
    await NicknameStates.waiting_for_variant.set()
    await call.answer()

async def process_variant(call: types.CallbackQuery, state: FSMContext):
    idx = int(call.data.replace("select_", ""))
    data = await state.get_data()
    variant = data['variants'][idx]

    await add_nickname(call.from_user.id, variant)
    await call.message.answer(
        f"✅ Saqlandi:\n<b>{variant}</b>",
        parse_mode="HTML",
        reply_markup=main_menu
    )
    await state.finish()
    await call.answer()

def register_handlers_nickname(dp: Dispatcher):
    dp.register_message_handler(new_nickname, lambda m: m.text == "🆕 Yangi Nickname")
    dp.register_message_handler(process_name, state=NicknameStates.waiting_for_name)
    dp.register_callback_query_handler(process_gender,
                                       lambda c: c.data.startswith("gender_"),
                                       state=NicknameStates.waiting_for_gender)
    dp.register_callback_query_handler(process_variant,
                                       lambda c: c.data.startswith("select_"),
                                       state=NicknameStates.waiting_for_variant)
