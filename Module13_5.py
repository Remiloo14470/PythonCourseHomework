from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = "7860471206:AAG6mzapA0JqhNizrXHPFHPKjmZuV8aKyIg"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=False)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button)
kb.add(button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. Нажми "Рассчитать", чтобы '
                         'узнать свою норму калорий', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer("Введите свой возраст, пожалуйста:")
    await UserState.age.set()


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
