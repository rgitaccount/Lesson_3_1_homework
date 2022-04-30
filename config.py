from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
URL = "https://homework-month3-tbot.herokuapp.com/"
URI = "postgres://mazfwpnlptqwgw:073ae7ac31da14324a4719714a5c682e68262f023c8a84d852a7578e814b0d5c@ec2-52-5-110-35.compute-1.amazonaws.com:5432/d1pl2cev7m7adg"
