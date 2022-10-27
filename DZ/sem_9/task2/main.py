# чат бот в телеграмме
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import config
from bot_commands import *


app = ApplicationBuilder().token(config.token).build()


app.add_handler(CommandHandler("Start", hi_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("subt", subt_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("del", del_command))
app.add_handler(CommandHandler("degree", degree_command))
app.add_handler(CommandHandler("help", help_command))


print('server start')
app.run_polling()
