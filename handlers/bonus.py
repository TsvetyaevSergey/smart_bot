from aiogram import Router, F
from aiogram.types import Message

from keyboards.back_menu import get_back

router = Router()  # [1]


@router.message(F.text.lower() == "получить бонус (за отзыв)")
async def start_select(message: Message):
    await message.answer(
        "Спасибо, что выбрали нас!\n\n"
        "У вас есть возможность получить бонус в размере 100₽ на номер телефона прямо сейчас! \n\n"
        "Для этого, пожалуйста, пришлите скриншот отзыва (с фотографией) из личного кабинета 😊",
        reply_markup=get_back()
    )