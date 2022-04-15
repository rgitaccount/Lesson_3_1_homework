from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_next = KeyboardButton('/next')
button_cancel = KeyboardButton('/cancel')

admin_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button_next, button_cancel)