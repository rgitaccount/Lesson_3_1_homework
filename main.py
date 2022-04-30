from aiogram.utils import executor
from config import bot, dp, URL
from handlers import client, callback, extra, fsmadmin, notification
from database import bot_db
import asyncio
from decouple import config

"""
heroku ps:scale worker=1
heroku ps:scale worker=0

heroku logs --tail --app (app name)
homework>heroku ps -a homework-month3-tbot

"""


async def on_startup(_):
    await bot.set_webhook(URL)
    bot_db.sql_create()
    asyncio.create_task(notification.scheduler())
    print("Bot db is online")


async def on_shutdown(dp):
    await bot.delete_webhook()


fsmadmin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_client(dp)
notification.register_handler_notification(dp)
extra.register_handlers_other(dp)


if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(config("PORT", default=5000))
    )
