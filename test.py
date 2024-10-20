import datetime
from aiogram.types import CallbackQuery, User, Message

from aiogram import F

from data import dp, jsonData
from keyboardBuilder import *
import data
import asyncio

async def call_callback(user, message, chat_id, callback_data):
    fake_callback_query = CallbackQuery(
        id="123",
        from_user=user,
        message=message,
        chat_instance=chat_id,
        data=callback_data
    )
    await callback_button(callback_query = fake_callback_query)

@dp.callback_query(F.data == "base_of_exercises")
async def callback_button(callback_query):
    keyboard = getBaseOfExercisesKeyboard()
    await callback_query.message.answer("База упражнений:", reply_markup=keyboard)
