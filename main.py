import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.types import Message, ContentType

import callback
import test
from config import settings
import data
from data import dp, jsonData
from keyboardBuilder import *

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    rep_keyboard = getReplyKeyboard()
    inl_keyboard = getMainKeyboard()
    await message.answer("Ну типа привет)", reply_markup=rep_keyboard)
    await message.answer("Главная страница:", reply_markup=inl_keyboard)


@dp.message(lambda message: message.text == "Главная страница")
async def send_help(message: Message):
    keyboard = getMainKeyboard()
    await message.answer("Главная страница:", reply_markup=keyboard)
    await message.answer_video(video=open("C:/Users/ILYASLAV/Desktop/makarovBot/resources/video/Демонстрация.mp4", 'rb'))

@dp.message(lambda message: message.text == "Назад")
async def send_help(message: Message):
    await test.call_callback(
        user = message.from_user,
        message = message,
        chat_id = str(message.from_user.id),
        callback_data = 'base_of_exercises')
    await message.answer("Назад:)")

@dp.message(lambda message: message.text == "Купить тариф")
async def send_help(message: Message):
    keyboard = getTariffsKeyboard()
    await message.answer("Купить тариф:", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Инструкция по боту")
async def send_help(message: Message):
    await message.answer("Инструкция")

@dp.message(lambda message: message.text == "chatId")
async def send_help(message: Message):
    await message.answer(str(message.from_user.id))

@dp.message(lambda message: message.video is not None)
async def send_help(message: Message):
    data.file = message.video.file_id
    print(data.file)
    await message.answer("Видео")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=settings.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    jsonData["legs"] = ["22"]
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
