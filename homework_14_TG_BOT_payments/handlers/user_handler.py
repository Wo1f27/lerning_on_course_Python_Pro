import asyncio

from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from homework_10_TG_BOT.keyboard.inline_kb import keyboard_inline, create_keyboard_inline
from homework_10_TG_BOT.states.state_bot import MenuState
from homework_10_TG_BOT.bot_config import bot

router = Router()


