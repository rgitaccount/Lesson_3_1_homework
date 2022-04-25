from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, update

from database import bot_db
from keyboards import client_kb
from config import bot, dp
from webparser import scraper


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.first_name}",
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply("1. Type /start to see main menu")


async def quiz(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"What quiz do you want to pass today? Python or History?",
                           reply_markup=client_kb.quiz_menu_markup)


async def get_all_users(message: types.Message):
    await bot_db.sql_select(message)


async def parse_tender_lots(message: types.Message):
    data = scraper.scraper_script()
    for lot in data:
        await bot.send_photo(message.chat.id,
                             photo=lot['image'],
                             caption=f"Deadline: {lot['deadline']}\n"
                                     f"{lot['header']}\n"
                                     f"{lot['link']}")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(get_all_users, commands=['users'])
    dp.register_message_handler(parse_tender_lots, commands=['tenders'])
