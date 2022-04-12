from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

help_button = KeyboardButton("/help")
quiz_button = KeyboardButton("/quiz")
location_button = KeyboardButton("Share Location", request_location=True)
info_button = KeyboardButton("Share Info", request_contact=True)
python_button = InlineKeyboardButton("🐍", callback_data="python_quiz")
history_button = InlineKeyboardButton("📔", callback_data="history_quiz")
cancel_button = InlineKeyboardButton("No, thanks", callback_data="cancel_quiz")


start_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
quiz_menu_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_markup.row(help_button, quiz_button, location_button, info_button)
quiz_menu_markup.row(python_button, history_button, cancel_button)