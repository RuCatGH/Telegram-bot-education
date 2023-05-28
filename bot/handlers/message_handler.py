from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.db.requests import check_or_update_category, get_all_id_and_categories
from bot.utils.api.api_openai import get_advice_chatgpt
from bot import dp, bot


class RegistrationStates(StatesGroup):
    category = State()


# Для отзывов
@dp.message_handler(commands=['feedback'])
async def send_message_to_group(message: types.Message):
    chat_id = -1001815446276  # Замените на ID вашей группы
    await bot.send_message(chat_id=chat_id, text=message.text)
    await message.answer('📣 Мы всегда открыты к вашим пожеланиям! Спасибо огромное за ваш отзыв! 🙌🌟')


# Отправка совета
async def send_advice():
    users = get_all_id_and_categories()
    for user in users:
        id, category = user

        advice = get_advice_chatgpt(category)
        await bot.send_message(id, advice)


@dp.callback_query_handler(state=RegistrationStates.category)
async def get_advice(callback: types.CallbackQuery):
    category = callback.data
    message = f"🔔 Вы выбрали категорию: {category}!\n\n" \
              f"Спасибо за выбор! Теперь каждый день вам будет " \
              f"отправляться совет по этой категории. Оставайтесь на " \
              f"связи и получайте полезные рекомендации! 💡💪"
    if check_or_update_category(user_id=callback.from_user.id, category_user=category):
        await bot.send_message(callback.from_user.id, message)
    else:
        await bot.send_message(callback.from_user.id, message)
        await bot.send_message(callback.from_user.id, '👋 Вот и первый совет! 😉')

        advice = get_advice_chatgpt(category)
        await bot.send_message(callback.from_user.id, advice)
