from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.handlers.message_handler import RegistrationStates
from bot.utils.text import start_message
from bot.keyboards.main_keyboard import create_message_keyboard
from bot import dp


@dp.message_handler(commands=['start', 'help'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await state.set_state(RegistrationStates.category)
    await message.answer(start_message, parse_mode=types.ParseMode.HTML, reply_markup=create_message_keyboard())

