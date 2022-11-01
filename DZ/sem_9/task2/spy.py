from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('DZ\sem_9\task2\db.csv', 'a')
    file.write(
        f'{update._effective_user.first_name}, {update._effective_user.id}, {update.message.text}\n')
    file.close()
