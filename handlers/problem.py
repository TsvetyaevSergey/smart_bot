from aiogram import Router, F
from aiogram.types import Message

from keyboards.back_menu import get_back

router = Router()  # [1]


@router.message(F.text.lower() == "проблема с товаром")
async def start_select(message: Message):
    await message.answer(
        "Чтобы мы смогли Вам помочь пришлите, пожалуйста, следующее:\n"
        "1. Скриншот из раздела покупок, чтобы мы могли идентифицировать товар;\n"
        "2. Фото/видео брака или вопрос - чтобы мы разобрались в чем дело.",
        reply_markup=get_back()
    )