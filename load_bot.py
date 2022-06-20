from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
