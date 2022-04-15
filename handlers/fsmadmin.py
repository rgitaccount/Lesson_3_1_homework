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


def write_data(message: types.Message,
               values_dict):
    real_data = dict()
    real_data['real_id'] = message.from_user.id
    real_data['real_username'] = message.from_user.username
    real_data['real_first_name'] = message.from_user.first_name
    real_data['real_last_name'] = message.from_user.last_name

    with open(f'{message.from_user.id}.txt', mode='w') as file:
        text = ''
        for (i, j), (i1, j1) in zip(real_data.items(), values_dict.items()):
            text += f'{i} is {j}, and user entered {i1} as {j1}\n'
        file.write(text)


async def start_poll(message: types.Message):
    global CURRENT_ID
    CURRENT_ID = message.from_user.id
    await bot.send_message(message.from_user.id,
                           "You will be asked to send your personal information.\n"
                           "Please send your ID number.",
                           reply_markup=admin_kb.admin_keyboard_markup)
    await FSMAdmin.user_id.set()


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
    await message.reply('Please send your username.')


async def load_username(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMAdmin.next()
    await message.reply('Please send your first name.')


async def load_firstname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMAdmin.next()
    await message.reply('Please send your last name.')


async def load_lastname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
        user_input_data = data.as_dict()
    write_data(message, user_input_data)
    await state.finish()
    await message.reply('Thanks for your time.')


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(start_poll, commands=['poll'])
    dp.register_message_handler(cancel_command, commands=['cancel'], state='*')
    dp.register_message_handler(load_id, content_types=['text'], state=FSMAdmin.user_id)
    dp.register_message_handler(load_username, state=FSMAdmin.username)
    dp.register_message_handler(load_firstname, state=FSMAdmin.first_name)
    dp.register_message_handler(load_lastname, state=FSMAdmin.last_name)
