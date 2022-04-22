from aiogram.utils import executor
from config import bot, dp
from handlers import client, callback, extra, fsmadmin
from database import bot_db


async def on_startup(_):
    bot_db.sql_create()
    print("Bot db is online")


fsmadmin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_client(dp)
extra.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
