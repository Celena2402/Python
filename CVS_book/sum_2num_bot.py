import telebot
from telebot import types
from telebot import apihelper
import config

bot = telebot.TeleBot('config.token')
apihelper.proxy = {'https': 'socks5h://LOGIN:PASS@IP:1080'}
storage = {}

def init_storage(user_id):
  storage[user_id] = dict(first_number=None, second_number=None)

def store_number(user_id, key, value):
  storage[user_id][key] = dict(value=value)

def get_number(user_id, key):
  return storage[user_id][key].get('value')

@bot.message_handler(func=lambda m: True)
def start(message):
  init_storage(message.from_user.id)
  bot.reply_to(message, "Введите + чтобы прибавить два числа ")
  bot.register_next_step_handler(message, plus)

def plus(message):
      if message.text == "+":
         bot.reply_to(message,"Enter number 1: ")
         bot.register_next_step_handler(message, plus_one)
      else:
         bot.reply_to(message, "Введите + чтобы прибавить два числа ")
         bot.register_next_step_handler(message, plus)

def plus_one(message):
        first_number = message.text

        if not first_number.isdigit():
            msg = bot.reply_to(message, 'Enter only digits!')
            bot.register_next_step_handler(message, plus_one)
            return

        store_number(message.from_user.id, "first_number", first_number)
        bot.reply_to(message, "Enter number 2: ")
        bot.register_next_step_handler(message, plus_two)

def plus_two(message):
       second_number = message.text

       if not second_number.isdigit():
            msg = bot.reply_to(message, 'Enter only digits!')
            bot.register_next_step_handler(message, plus_two)
            return

       store_number(message.from_user.id, "second_number", second_number)

       number_1 = get_number(message.from_user.id, "first_number")
       number_2 = get_number(message.from_user.id, "second_number")

       result_plus = int(number_1) + int(number_2)
       bot.reply_to(message, f"Ответ: {result_plus}")

if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
    #bot.infinity_polling()
