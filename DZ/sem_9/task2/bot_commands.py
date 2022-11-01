from email import message
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    if update.message.text == "/start":
        await update.message.reply_text(f'Привет {update.effective_user.first_name}')
        await update.message.reply_text(f'Выберите операцию и введите 2 любых числа через пробел:\nНачнем с начала /start\nСумма 2-х чисел (х+у) /sum\nРазница 2-х чисел (х-у) /subt\nУмножение 2-х чисел (х*у) /mult\nДеление 2-х чисел (х/у) /del\nВозведение в степень (х^у) /degree\nПомощь /help')
        return


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'Сумма чисел {x} + {y} = {x + y}')


async def subt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'Разница чисел {x} - {y} = {x - y}')


async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'Умножение чисел {x} * {y} = {x * y}')


async def del_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'Деление чисел {x} / {y} = {x / y}')


async def degree_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Возведение в степень числа {x} ^ {y} = {x ** y}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)

    await update.message.reply_text(f'Выберите операцию и введите 2 любых числа через пробел:\nНачнем с начала /start\nСумма 2-х чисел (х+у) /sum\nРазница 2-х чисел (х-у) /subt\nУмножение 2-х чисел (х*у) /mult\nДеление 2-х чисел (х/у) /del\nВозведение в степень (х^у) /degree\nПомощь /help')
