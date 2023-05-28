import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

# Создание объектов бота и диспетчера
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Подключение обработчиков команд и событий
from .handlers import start_handler, message_handler

# Подключение промежуточного программного обеспечения
from .middlewares import logging_middleware

# Подключение клавиатур
from .keyboards import main_keyboard




