import asyncio
import requests

from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from intermediate_certification_3.tg_bot.keyboards.inline_kb import keyboard_inline, create_keyboard_inline
from intermediate_certification_3.tg_bot.states.state_bot import MenuState
from intermediate_certification_3.tg_bot.bot_config import bot

router = Router()


@router.message(CommandStart())
async def start_bot(m: Message):
    await m.answer('Привет я бот! Введи команду /go для показа меню действий. Помощь /help')


@router.message(Command('help'))
async def help_bot(m: Message):
    await m.answer('''Я могу показать список твоих задач
    Сохранить новую задачу 
    Либо удалить уже не нужную задачу ''')


@router.message(Command('go'))
async def main_func(m: Message, state: FSMContext):
    await m.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data == 'add', StateFilter(MenuState.main_start_state))
async def add_task_callback(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer('Введите текст вашей задачи:')
    await state.set_state(MenuState.add_task)


@router.message(StateFilter(MenuState.add_task))
async def process_add_task_name(message: Message, state: FSMContext):
    task_name = message.text
    await state.update_data(task_name=task_name)
    await message.answer('Введите дэдлайн для задачи (в формате ГГГГ-ММ-ДД):')
    await state.set_state(MenuState.add_task_deadline)


@router.message(StateFilter(MenuState.add_task_deadline))
async def add_task_deadline_callback(message: Message, state: FSMContext):
    task_deadline = message.text
    task = await state.get_data()
    task_name = task.get('task_name')

    payload = {
        'name': task_name,
        'deadline': task_deadline
    }

    try:
        response = requests.post('http://127.0.0.1:8000/tasks', json=payload)
        response.raise_for_status()
        await message.answer(f'Задача {task_name} добавлена на сервер')
    except requests.exceptions.RequestException as e:
        await message.answer(f'Ошибка при создании задачи: {e}')

    await asyncio.sleep(1)
    await message.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data == 'get_list', StateFilter(MenuState.main_start_state))
async def process_get_notes(cb: CallbackQuery, state: FSMContext):
    try:
        response = requests.get('http://127.0.0.1:8000/tasks')
        response.raise_for_status()
        tasks = response.json()

        if tasks:
            tasks_list = "\n".join(
                [f"ID: {task['id']}, Задача: {task['name']}, Дэдлайн: {task['deadline']}" for task in tasks])
            await bot.send_message(cb.from_user.id, tasks_list)
        else:
            await cb.answer("Заметок нет.", show_alert=True)

    except requests.exceptions.RequestException as e:
        await cb.answer(f"Ошибка при получении задач: {e}", show_alert=True)

    await asyncio.sleep(1)
    await bot.send_message(cb.from_user.id, 'Что вы хотите сделать: ', reply_markup=keyboard_inline)
    await state.set_state(MenuState.main_start_state)


@router.callback_query(lambda cb: cb.data == 'delete', StateFilter(MenuState.main_start_state))
async def delete_task(cb: CallbackQuery, state: FSMContext):
    await cb.answer('Какую заметку вы хотите удалить?')

    try:
        response = requests.get('http://127.0.0.1:8000/tasks')
        response.raise_for_status()
        tasks = response.json()

        if tasks:
            keyboard = create_keyboard_inline(tasks)
            await bot.send_message(cb.from_user.id, "Выберите заметку для удаления:", reply_markup=keyboard)

        else:
            await bot.send_message(cb.from_user.id, "Заметок нет.")

    except requests.exceptions.RequestException as e:
        await cb.answer(f"Ошибка при получении задач: {e}", show_alert=True)

    await state.set_state(MenuState.delete_task)


@router.callback_query(lambda cb: cb.data.startswith('delete_'))
async def handle_delete_task_callback(cb: CallbackQuery, state: FSMContext):
    task_to_delete = cb.data[len('delete_'):]
    try:
        response = requests.get('http://127.0.0.1:8000/tasks')
        response.raise_for_status()
        tasks = response.json()

        if tasks:
            task_for_delete = [f"{task['id']}" for task in tasks]
        else:
            task_for_delete = []

        if task_to_delete in task_for_delete:
            try:
                response = requests.delete(f'http://127.0.0.1:8000/tasks/{task_to_delete}')
                response.raise_for_status()

                await cb.answer(f'Задача "{task_to_delete}" была удалена.')
            except requests.exceptions.RequestException as e:
                await cb.answer(f'Ошибка при удалении задачи: {e}')

        else:
            await cb.answer('Заметка не найдена.')

    except requests.exceptions.RequestException as e:
        await cb.answer(f"Ошибка при получении задач: {e}", show_alert=True)

    await asyncio.sleep(1)
    await state.set_state(MenuState.main_start_state)
    await cb.message.answer('Что вы хотите сделать: ', reply_markup=keyboard_inline)

