import asyncio
import logging
from datetime import datetime, timedelta

from aiogram import executor

from bot import dp
from bot.handlers.message_handler import send_advice

# Настройка уровня логирования
logging.basicConfig(level=logging.INFO)


# Запуск отправки каждые 24 часа совета
async def schedule_jobs():
    starting_time = datetime.utcnow()
    interval = timedelta(hours=24)
    while True:
        await asyncio.sleep(interval.total_seconds())
        await send_advice()
        starting_time += interval


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_jobs())
    executor.start_polling(dp, skip_updates=True)
