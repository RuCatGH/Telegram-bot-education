import logging
from aiogram import executor
from bot import dp

# Настройка уровня логирования
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)