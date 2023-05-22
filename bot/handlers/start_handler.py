from aiogram import types
from bot import dp
from bot.utils.text import start_message   

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(start_message,  parse_mode=types.ParseMode.HTML)

