from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from db import *

api = "7860471206:AAG6mzapA0JqhNizrXHPFHPKjmZuV8aKyIg"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

add_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Купить')
kb.add(button1)
kb.add(button2)


kb2 = InlineKeyboardMarkup(resize_keyboard=True).add(
    InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')
)


inline_menu = InlineKeyboardMarkup(inline_keyboard=
                                   [[InlineKeyboardButton(text=' Продукт1', callback_data='product_buying'),
                                     InlineKeyboardButton(text=' Продукт2', callback_data='product_buying'),
                                     InlineKeyboardButton(text=' Продукт3', callback_data='product_buying'),
                                     InlineKeyboardButton(text=' Продукт4', callback_data='product_buying')]],
                                   resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer('Список товаров и меню покупки:')
    products_data = get_all_products()
    for product in products_data:
        file_path = f'files/{product[0]}.jpeg'
        with open(file_path, 'rb') as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_menu)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула такая: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст, пожалуйста:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост, пожалуйста:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес, пожалуйста:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result_calories = 10*int(data['age']) + 6.25*int(data['growth']) - 5*int(data['weight']) - 161
    await message.answer(f"Ваша норма колорий: {result_calories}")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
