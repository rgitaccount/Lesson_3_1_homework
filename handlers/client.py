from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, update
from keyboards import client_kb

from config import bot, dp


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply("1. Type")


async def quiz(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"What quiz do you want to pass today? Python or History?",
                           reply_markup=client_kb.quiz_menu_markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(help, commands=['help'])