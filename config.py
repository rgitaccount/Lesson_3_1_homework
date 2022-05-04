from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "https://homework-month3-tbot.herokuapp.com/"
URI = "postgres://ovpuzynzdobyzd:16b7d5aad6415d6f44201d853c18bbb3dbd3dace96cc46743b924757012e4240@ec2-52-5-110-35.compute-1.amazonaws.com:5432/d3hm5smerkaq3b"
