from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn1 = InlineKeyboardButton(text='Добавить заметку', callback_data='add')
btn2 = InlineKeyboardButton(text='Просмотреть заметки', callback_data='get_list')
btn3 = InlineKeyboardButton(text='Удалить заметку', callback_data='delete')

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[
    [btn1], [btn2], [btn3]
])

kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сок', callback_data='juice')],
    [InlineKeyboardButton(text='Чай', callback_data='tea')]
])