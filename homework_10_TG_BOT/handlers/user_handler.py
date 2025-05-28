import asyncio

from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from homework_10_TG_BOT.keyboard.inline_kb import keyboard_inline, create_keyboard_inline
from homework_10_TG_BOT.states.state_bot import MenuState
from homework_10_TG_BOT.bot_config import bot

router = Router()

notes = []

@router.message(CommandStart())
async def start_bot(m: Message):
    await m.answer('Привет я бот! Введи команду /go для старта. Помощь /help')

@router.message(Command('help'))
async def help_bot(m: Message):
    await m.answer('''Я могу показать список твоих заметок
    Сохранить новую заметку
    Либо удалить уже не нужную заметку''')


@router.message(Command('go'))
async def main_func(m: Message, state: FSMContext):
    await m.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data == 'add', StateFilter(MenuState.main_start_state))
async def add_note_callback(cb: CallbackQuery, state: FSMContext):
    await cb.answer('Введите текст вашей заметки:')
    await state.set_state(MenuState.add_note)


@router.message(StateFilter(MenuState.add_note))
async def process_add_note(message: Message, state: FSMContext):
    notes.append(message.text)
    await message.answer('Заметка добавлена')
    await asyncio.sleep(1)
    await message.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data == 'get_list', StateFilter(MenuState.main_start_state))
async def process_get_notes(cb: CallbackQuery, state: FSMContext):
    if notes:
        await bot.send_message(cb.from_user.id, "\n\n".join(notes))
    else:
        await cb.answer("Заметок нет.", show_alert=True)
    await asyncio.sleep(1)
    await bot.send_message(cb.from_user.id, 'Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data == 'delete', StateFilter(MenuState.main_start_state))
async def process_delete_note(cb: CallbackQuery, state: FSMContext):
    await cb.answer('Какую заметку вы хотите удалить?')
    await state.set_state(MenuState.delete_note)
    if notes:
        keyboard = create_keyboard_inline(notes)
        await bot.send_message(cb.from_user.id, "Выберите заметку для удаления:", reply_markup=keyboard)
    else:
        await bot.send_message(cb.from_user.id, "Заметок нет.")
    await state.set_state(MenuState.delete_note)


@router.callback_query(lambda cb: cb.data.startswith('delete_'))
async def handle_delete_note_callback(cb: CallbackQuery, state: FSMContext):
    note_to_delete = cb.data[len('delete_'):]

    if note_to_delete in notes:
        notes.remove(note_to_delete)
        await cb.answer(f'Заметка "{note_to_delete}" была удалена.')
    else:
        await cb.answer('Заметка не найдена.')
    await cb.message.answer("Обновленный список заметок:", reply_markup=create_keyboard_inline(notes))
    await asyncio.sleep(1)
    await state.set_state(MenuState.main_start_state)
    await cb.message.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)
