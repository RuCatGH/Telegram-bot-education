from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboards_text = ['Саморазвитие', 'Программирование', 'Космос', 'Психология', 'Спорт', 'Здоровье']


def create_message_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    # Создание кнопок
    for i in range(0, len(keyboards_text), 2):
        button1 = InlineKeyboardButton(keyboards_text[i], callback_data=f'{keyboards_text[i]}')
        if i + 1 < len(keyboards_text):
            button2 = InlineKeyboardButton(keyboards_text[i + 1], callback_data=f'{keyboards_text[i + 1]}')
            keyboard.row(button1, button2)
        else:
            keyboard.add(button1)

    return keyboard
