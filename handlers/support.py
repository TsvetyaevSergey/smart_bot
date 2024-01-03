from aiogram import Router, F
from aiogram.types import Message

from keyboards.back_menu import get_back

router = Router()  # [1]


@router.message(F.text.lower() == "связаться с поддержкой")
async def start_select(message: Message):
    await message.answer(
        "В ближайшее время с Вами свяжутся.",
        reply_markup=get_back()
    )