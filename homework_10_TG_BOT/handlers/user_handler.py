import asyncio

from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from homework_10_TG_BOT.keyboard import reply_kb
from homework_10_TG_BOT.keyboard.inline_kb import keyboard_inline, kb
from homework_10_TG_BOT.states.state_bot import MenuState

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
    print(await state.get_data())


@router.callback_query(lambda cb: cb.data == 'add')
async def add_note_callback(cb: CallbackQuery, state: FSMContext):
    await cb.answer('Введите текст вашей заметки:')
    await state.set_state(MenuState.add_note)


@router.message(StateFilter(MenuState.add_note))
async def process_add_note(message: Message, state: FSMContext):
    notes.append(message.text)
    await message.answer('Заметка добавлена')
    await asyncio.sleep(2)
    await message.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data in ['juice', 'tea'], StateFilter('MenuState:drink_state'))
async def get_drink(cb: CallbackQuery, state: FSMContext):
    await cb.answer()
    await cb.message.answer('Спасибо')
    print(await state.get_data())
    print(await state.get_state())
    await state.clear()
    await state.set_data({})
    print(await state.get_data())
    print(await state.get_state())