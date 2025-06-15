import datetime
import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types, BaseMiddleware
from aiogram.types import LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_activity = {}

class UserActivityMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: types.Message, data: dict):
        user_id = event.from_user.id
        # Сохраняем время последней активности
        user_activity[user_id] = datetime.datetime.now()
        # Продолжаем выполнение следующего обработчика
        return await handler(event, data)


# Пример команды для проверки активности пользователя
async def check_activity(message: types.Message):
    user_id = message.from_user.id
    last_active = user_activity.get(user_id)

    if last_active:
        # Форматируем дату и время
        last_active_str = last_active.strftime("%H:%M %d.%m.%Y")
        await message.reply(f"Ваша последняя активность была: {last_active_str}")
    else:
        await message.reply("Нет данных об активности")
# Список товаров
PRODUCTS = [
    {"title": "Товар 1", "description": "Описание товара 1", "price": 100},
    {"title": "Товар 2", "description": "Описание товара 2", "price": 200},
    {"title": "Товар 3", "description": "Описание товара 3", "price": 300},
    {"title": "Товар 4", "description": "Описание товара 4", "price": 400},
    {"title": "Товар 5", "description": "Описание товара 5", "price": 500},
]
dp.message.middleware(UserActivityMiddleware())
dp.message.register(check_activity, Command("check_activity"))
@dp.message(Command("start"))
async def start(message: types.Message):
    """Обработка команды /start с отправкой списка товаров"""
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[])  # Создаем клавиатуру с пустым списком

    for idx, product in enumerate(PRODUCTS):
        button = types.InlineKeyboardButton(
            text=product["title"],
            callback_data=f"buy_{idx}"
        )
        keyboard.inline_keyboard.append([button])  # Добавляем кнопку в виде строки

    await message.answer("Выберите товар для покупки:", reply_markup=keyboard)


@dp.callback_query(lambda c: c.data and c.data.startswith("buy_"))
async def process_buy(callback_query: types.CallbackQuery):
    """Обработка нажатия на кнопку покупки"""
    index = int(callback_query.data.split("_")[1])
    product = PRODUCTS[index]

    prices = [LabeledPrice(label=product["title"], amount=product["price"] * 100)]

    await bot.send_invoice(
        chat_id=callback_query.from_user.id,
        title=product["title"],
        description=product["description"],
        payload=f"product_{index}",
        provider_token=PROVIDER_TOKEN,
        currency="RUB",
        prices=prices,
        start_parameter="test-payment",
    )
    await callback_query.answer()


@dp.pre_checkout_query(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    """Подтверждение запроса на оплату"""
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(lambda message: message.successful_payment)
async def successful_payment(message: types.Message):
    """Обработка успешной оплаты"""
    await message.answer(
        f"Оплата прошла успешно! Спасибо за покупку")


async def main():
    """Запуск бота"""
    await dp.start_polling(bot)  # Передаем экземпляр бота в функцию


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f"Ошибка: {e}")