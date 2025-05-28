from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton(text='Добавить заметку', callback_data='add')
btn2 = InlineKeyboardButton(text='Просмотреть заметки', callback_data='get_list')
btn3 = InlineKeyboardButton(text='Удалить заметку', callback_data='delete')

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [btn1], [btn2], [btn3]
])


def create_keyboard_inline(notes: list):
    key_list = []
    for note in notes:
        key_list.append([InlineKeyboardButton(text=note, callback_data=f'delete_{note}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=key_list)

    return keyboard
