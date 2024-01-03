from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_start_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Получить бонус (за отзыв)")
    kb.button(text="Проблема с товаром")
    kb.button(text="Связаться с поддержкой")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
