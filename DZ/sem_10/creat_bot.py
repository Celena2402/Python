from config import TOKEN
from aiogram.dispatcher import Dispatcher
from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)