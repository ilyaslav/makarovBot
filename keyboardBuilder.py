from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from config import settings

def getReplyKeyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Купить тариф"),
                KeyboardButton(text="Инструкция по боту"),
            ],
            [
                KeyboardButton(text="Главная страница"),
                KeyboardButton(text="Назад"),
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

def getMainKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="База упражнений", callback_data="base_of_exercises")],
            [InlineKeyboardButton(text="Тренировки", callback_data="training")],
            [InlineKeyboardButton(text="База знаний", callback_data="knowledge_base", url=settings.CHANNEL_URL)],
            [InlineKeyboardButton(text="Необходимое оборудование", callback_data="necessary_equipment")]
        ]
    )

def getTrainingKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Тренировки в зале", callback_data="gym_training")],
            [InlineKeyboardButton(text="Тренировки в домашних условиях", callback_data="home_training")],
            [InlineKeyboardButton(text="Тренировочный профиль", callback_data="training_profile")]
        ]
    )

def getBaseOfExercisesKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ноги, ягодицы", callback_data="legs")],
            [InlineKeyboardButton(text="Грудные", callback_data="breast")],
            [InlineKeyboardButton(text="Спина", callback_data="back")],
            [InlineKeyboardButton(text="Плечи", callback_data="shoulders")],
            [InlineKeyboardButton(text="Бицепс", callback_data="biceps")],
            [InlineKeyboardButton(text="Трицепс", callback_data="triceps")],
            [InlineKeyboardButton(text="Пресс", callback_data="press")],
            [InlineKeyboardButton(text="Растяжка", callback_data="stretching")],
            [InlineKeyboardButton(text="МФР", callback_data="MFR")],
        ]
    )

def getTrainingProfileKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Изменить профиль", callback_data="change_profile")],
            [InlineKeyboardButton(text="Добавить запись подхода", callback_data="add_training_record")],
            [InlineKeyboardButton(text="Посмотреть запись подхода", callback_data="get_training_record")],
        ]
    )

def getChangeSexKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Мужской", callback_data="male")],
            [InlineKeyboardButton(text="Женский", callback_data="female")],
        ]
    )

def getChangePurposeKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Набор", callback_data="gain_muscle_mass")],
            [InlineKeyboardButton(text="Похудение", callback_data="weight_loss")],
            [InlineKeyboardButton(text="Поддержание", callback_data="maintaining_muscle_mass")],
        ]
    )

def getWorkoutsPerWeekKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="2", callback_data="workouts_2")],
            [InlineKeyboardButton(text="3", callback_data="workouts_3")],
        ]
    )

def getTariffsKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data="tariff_1")],
            [InlineKeyboardButton(text="2", callback_data="tariff_2")],
        ]
    )

def getPayTariffKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Оплатить", callback_data="22")],#, callback_data="pay_tariff")],
        ]
    )

def getLegsKeyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ноги", callback_data="pay_tariff")],
        ]
    )
