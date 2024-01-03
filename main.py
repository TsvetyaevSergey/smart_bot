import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import select_question,bonus,problem,support
logging.basicConfig(level=logging.INFO)

# Запуск бота
async def main():
    bot = Bot(token="6536590955:AAEAkDiMSx-MY275clOkjv-p2WukRUw8R3Y")
    dp = Dispatcher()
    dp.include_routers(select_question.router,bonus.router,problem.router,support.router)
    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
