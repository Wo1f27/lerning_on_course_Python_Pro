from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton(text='Добавить задачу', callback_data='add')
btn2 = InlineKeyboardButton(text='Просмотреть задачи', callback_data='get_list')
btn3 = InlineKeyboardButton(text='Удалить задачу', callback_data='delete')

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [btn1], [btn2], [btn3]
])


def create_keyboard_inline(tasks: list):
    key_list = []
    for task in tasks:
        key_list.append([InlineKeyboardButton(text=task, callback_data=f'delete_{task}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=key_list)

    return keyboard
