from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import admin_kb
from config import bot


class FSMAdmin(StatesGroup):
    user_id = State()
    username = State()
    first_name = State()
    last_name = State()


async def start_poll(message: types.Message):
    global CURRENT_ID
    CURRENT_ID = message.from_user.id
    await bot.send_message(message.from_user.id,
                           "You will be asked to send your personal information.\n"
                           "Please send your ID number.",
                           reply_markup=admin_kb.admin_keyboard_markup)


async def cancel_command(message: types.Message,
                         state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return "State is None"
    await state.finish()
    await message.reply("Canceled Successfully")


async def load_id(message: types.Message,
                  state: FSMContext):
    async with state.proxy() as data:
        data['user_id'] = message.text
    await FSMAdmin.next()
    await message.reply('Please send your user name.')


async def load_username(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMAdmin.next()
    await message.reply('Please send your first name.')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(start_poll, commands=['poll'])
    dp.register_message_handler(cancel_command, commands=['cancel'], state='*')
    dp.register_message_handler(load_id, state=FSMAdmin.user_id)
    dp.register_message_handler(load_username, state=FSMAdmin.username)
