# чат бот в телеграмме
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token('5769528527:AAH_1K1J8vwUsg8troNZk2IICxZKOd9Wq0w').build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()


# import matplotlib.pyplot as plt
# import numpy as np

# list=[1,2,3,2,7]
# plt.plot(list)

# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# plt.style.use('_mpl-gallery')

# # make data:
# np.random.seed(3)
# x = 0.5 + np.arange(8)
# y = np.random.uniform(2, 7, len(x))

# # plot
# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()


# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))



# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)  # происходит типа загрузка с задержклй в 1 сек
#     # Do some work
#     bar.next()
# bar.finish()





# from isOdd import isOdd

# #print(isOdd('1')) //=> true
# #print(isOdd('5')) //=> true

# print(isOdd(1)) 
# print(isOdd(4)) 