from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton(text='Добавить заметку', callback_data='add')
btn2 = InlineKeyboardButton(text='Просмотреть заметки', callback_data='get_list')
btn3 = InlineKeyboardButton(text='Удалить заметку', callback_data='delete')

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [btn1], [btn2], [btn3]
])


def create_keyboard_inline(notes: list):
    keyboard = InlineKeyboardMarkup()
    for note in notes:
        keyboard.add(InlineKeyboardButton(text=note, callback_data=f'delete_{note}'))

    return keyboard
