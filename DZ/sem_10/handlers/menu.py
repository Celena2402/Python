from aiogram import types, Dispatcher
from creat_bot import *

# @dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.text=="/start":
        await bot.send_message(message.from_user.id,'''Добро пожаловать в справочник учеников, 
        Список команд:
        /add - добавить
        /save - сохранить
        /output - просмотр
        /del - удалить
        /help - помощь
        '''        
                                                '')
      

#@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    if message.text=="/help":
        await bot.send_message(message.from_user.id,'''Список команд:
        /add - добавить
        /save - сохранить
        /output - просмотр
        /del - удалить        
        /help - помощь
        '''        
                                                '')

def register_handlers_menu(dp:Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])

