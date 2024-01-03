from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from keyboards.start_menu import get_start_menu

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Выберите подходящий вариант",
        reply_markup=get_start_menu()
    )

@router.message(F.text.lower() == "назад")  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Выберите подходящий вариант",
        reply_markup=get_start_menu()
    )
