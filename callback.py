from aiogram import F
from aiogram.types import CallbackQuery

from data import dp, jsonData
from keyboardBuilder import *
import data

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

@dp.callback_query(F.data == "training")
async def callback_button(callback_query):
    keyboard = getTrainingKeyboard()
    await callback_query.message.answer("Тренировки:", reply_markup=keyboard)

@dp.callback_query(F.data == "knowledge_base")
async def callback_button(callback_query):
    await callback_query.message.answer("База знаний")

@dp.callback_query(F.data == "necessary_equipment")
async def callback_button(callback_query):
    await callback_query.message.answer("Необходимое оборудование")

@dp.callback_query(F.data == "gym_training")
async def callback_button(callback_query):
    await callback_query.message.answer("Тренировки в зале")

@dp.callback_query(F.data == "home_training")
async def callback_button(callback_query):
    await callback_query.message.answer("Тренировки в домашних условиях")

@dp.callback_query(F.data == "training_profile")
async def callback_button(callback_query):
    keyboard = getTrainingProfileKeyboard()
    await callback_query.message.answer("Тренировочный профиль", reply_markup=keyboard)

@dp.callback_query(F.data == "legs")
async def callback_button(callback_query):
    await callback_query.message.answer("Ноги и ягодицы")

@dp.callback_query(F.data == "breast")
async def callback_button(callback_query):
    await callback_query.message.answer("Грудные")

@dp.callback_query(F.data == "back")
async def callback_button(callback_query):
    await callback_query.message.answer("Спина")

@dp.callback_query(F.data == "shoulders")
async def callback_button(callback_query):
    await callback_query.message.answer("Плечи")

@dp.callback_query(F.data == "biceps")
async def callback_button(callback_query):
    await callback_query.message.answer("Бицепс")

@dp.callback_query(F.data == "triceps")
async def callback_button(callback_query):
    await callback_query.message.answer("Трицепс")

@dp.callback_query(F.data == "press")
async def callback_button(callback_query):
    await callback_query.message.answer("Пресс")

@dp.callback_query(F.data == "stretching")
async def callback_button(callback_query):
    await callback_query.message.answer("Растяжка")

@dp.callback_query(F.data == "MFR")
async def callback_button(callback_query):
    await callback_query.message.answer("МФР")

@dp.callback_query(F.data == "change_profile")
async def callback_button(callback_query):
    keyboard = getChangeSexKeyboard()
    await callback_query.message.answer("Выберите пол", reply_markup=keyboard)

@dp.callback_query(F.data == "add_training_record")
async def callback_button(callback_query):
    await callback_query.message.answer("Добавить запись подхода")

@dp.callback_query(F.data == "get_training_record")
async def callback_button(callback_query):
    await callback_query.message.answer("Посмотреть запись подхода")

@dp.callback_query(F.data == "male")
async def callback_button(callback_query):
    keyboard = getChangePurposeKeyboard()
    await callback_query.message.answer("Цель тренировок", reply_markup=keyboard)

@dp.callback_query(F.data == "female")
async def callback_button(callback_query):
    keyboard = getChangePurposeKeyboard()
    await callback_query.message.answer("Цель тренировок", reply_markup=keyboard)

@dp.callback_query(F.data == "gain_muscle_mass")
async def callback_button(callback_query):
    keyboard = getWorkoutsPerWeekKeyboard()
    await callback_query.message.answer("Количество тренировок в неделю", reply_markup=keyboard)

@dp.callback_query(F.data == "weight_loss")
async def callback_button(callback_query):
    keyboard = getWorkoutsPerWeekKeyboard()
    await callback_query.message.answer("Количество тренировок в неделю", reply_markup=keyboard)

@dp.callback_query(F.data == "maintaining_muscle_mass")
async def callback_button(callback_query):
    keyboard = getWorkoutsPerWeekKeyboard()
    await callback_query.message.answer("Количество тренировок в неделю", reply_markup=keyboard)

@dp.callback_query(F.data == "workouts_2")
async def callback_button(callback_query):
    keyboard = getTrainingProfileKeyboard()
    await callback_query.message.answer("Тренировочный профиль", reply_markup=keyboard)

@dp.callback_query(F.data == "workouts_3")
async def callback_button(callback_query):
    keyboard = getTrainingProfileKeyboard()
    await callback_query.message.answer("Тренировочный профиль", reply_markup=keyboard)

@dp.callback_query(F.data == "tariff_1")
async def callback_button(callback_query):
    keyboard = getPayTariffKeyboard()
    await callback_query.message.answer("Тариф 1", reply_markup=keyboard)

@dp.callback_query(F.data == "tariff_2")
async def callback_button(callback_query):
    keyboard = getPayTariffKeyboard()
    await callback_query.message.answer("Тариф 2", reply_markup=keyboard)

@dp.callback_query(F.data == "pay_tariff")
async def callback_button(callback_query):
    keyboard = getMainKeyboard()
    await callback_query.message.answer("Главная страница", reply_markup=keyboard)

@dp.callback_query(F.data)
async def callback_button(callback_query):
    print(data.file)
    await callback_query.message.answer_video(video=data.file, caption='Моя <u>отформатированная</u> подпись к <b>файлу</b>')
