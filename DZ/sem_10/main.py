###   Файл входа

from aiogram.utils import executor
from creat_bot import dp


async def on_startup(_):
    print('Бот начал работать')

from handlers import menu, bot

menu.register_handlers_menu(dp)
bot.register_handlers_add(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
