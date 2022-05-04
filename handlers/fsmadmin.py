from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import admin_kb
from config import bot
from database import psql_db, bot_db



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


async def load_firstname(message: types.Message, state: FSMContext):
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
    await bot_db.sql_insert(state)
    await state.finish()
    await message.reply('Thanks for your time.')


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_delete(call.data.replace('delete', ''))
    await call.answer(text=f'{call.data.replace("delete", "")} deleted', show_alert=True)


async def delete_data(message: types.Message):
    selected_data = await bot_db.sql_select_all()
    for user in selected_data:
        await bot.send_message(message.chat.id,
                               text=f'UserID: {user[0]}\n'
                                    f'Username: {user[1]}\n'
                                    f'Firstname: {user[2]}\n'
                                    f'Lastname: {user[3]}\n',
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f'delete user {user[0]}', callback_data=f'delete {user[0]}')
                               ))


async def registration(message: types.Message):
    id = message.from_user.id
    username = message.from_user.username
    fullname = message.from_user.full_name

    psql_db.cursor.execute(
        'INSERT INTO users (id, username, fullname) VALUES (%s, %s, %s)',
        (id, username, fullname),
    )
    psql_db.db.commit()
    await message.reply("Registration successful")


async def get_all_users(message: types.Message):
    all_users = psql_db.cursor.execute("SELECT * FROM users")
    result = psql_db.cursor.fetchall()

    for row in result:
        await message.reply(
            f"ID: {row[0]}\n"
            f"Username: {row[1]}\n"
            f"Fullname": {row[2]}
        )


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(start_poll, commands=['poll'])
    dp.register_message_handler(cancel_command, commands=['cancel'], state='*')
    dp.register_message_handler(load_id, content_types=['text'], state=FSMAdmin.user_id)
    dp.register_message_handler(load_username, state=FSMAdmin.username)
    dp.register_message_handler(load_firstname, state=FSMAdmin.first_name)
    dp.register_message_handler(load_lastname, state=FSMAdmin.last_name)
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete"))
    dp.register_message_handler(delete_data, commands=['delete'])
    dp.register_message_handler(registration, commands=['register'])
    dp.register_message_handler(get_all_users, commands=['get'])
