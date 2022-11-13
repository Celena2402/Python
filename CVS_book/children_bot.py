from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
#from aiogram.types import InputFile
import csv


####################################
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
    print('Бот начал работать')

#---------------------МЕНЮ----------
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    #await bot.send_message(message.from_user.id, f"Добро пожаловать, {message.from_user.first_name} в справочник учеников!  ")
    if message.text=="/start":
        await bot.send_message(message.from_user.id,'''Добро пожаловать в справочник учеников, 
        Список команд:
        /add - добавить
        /save - сохранить
        /output - просмотр
        /del - удалить
        /edit - редактировать
        /help - помощь
        '''        
                                                '')
    
        #await bot.send_message(message.from_user.id, f"Добро пожаловать, {message.from_user.first_name} в справочник учеников!")
        #await bot.send_message(f'Выберите операцию:\n/add - добавить\n/save - сохранить\n/del - удалить\n/edit - редактировать\n/help - помощь')
        #return

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    if message.text=="/help":
        await bot.send_message(message.from_user.id,'''Список команд:
        /add - добавить
        /save - сохранить
        /output - просмотр
        /del - удалить
        /edit - редактировать
        /help - помощь
        '''        
                                                '')

#--------------1. ДОБАВЛЕНИЕ---------------
# создаём форму и указываем поля
class Form(StatesGroup):
    name = State() 
    birthday = State() 
    class_number=State()
    phone=State()
    name_del=State()
    
# Начинаем наш диалог
@dp.message_handler(commands=['add'])
async def cmd_start(message: types.Message):
    #global name, birthday, class_number, phone
    #global children
    await Form.name.set()
    await message.reply("ФИО")    

# Сюда приходит ответ с именем
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    #global name, birthday, class_number, phone
    #global children
    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    #await message.reply("Дата рождения ")    
    await message.answer("Дата рождения ") 

@dp.message_handler(state=Form.birthday)
async def process_birthday(message: types.Message, state: FSMContext):
    #global name, birthday, class_number, phone
    #global children
    async with state.proxy() as data:
        data['birthday'] = message.text
    await Form.next()
    #await state.update_data(birthday=message.text)
    #await message.reply("Номер класса ")
    await message.answer("Номер класса ") 

@dp.message_handler(state=Form.class_number)
async def process_class_number(message: types.Message, state: FSMContext):
    #global name, birthday, class_number, phone
    #global children
    async with state.proxy() as data:
        data['class_number'] = message.text
    await Form.next()
    #await message.reply("Номер телефона ")
    await message.answer("Номер телефона ")

@dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    #global name, birthday, class_number, phone
    #global children
    #children=[]
    async with state.proxy() as data:
        data['phone'] = message.text
        await bot.send_message(
            message.chat.id,
            md.text(                
                md.text('Вы ввели,\nФИО:', md.bold(data['name'])),
                md.text('Дата рождения:', md.code(data['birthday'])),
                md.text('Номер класса:', md.code(data['class_number'])),
                md.text('Номер телефона:', md.code(data['phone'])),
                sep='\n',
            ),            
            parse_mode=ParseMode.MARKDOWN,
        )
        await message.answer("Данные успешно внесены! Не забудьте их сохранить, команда /save или вызов меню /help")
        await message.answer('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)
        await state.finish()

#--------------2. СОХРАНЕНИЕ---------------

@dp.message_handler(commands=['save'])
async def save_to_CSV(message: types.Message, state: FSMContext):
    
	await state.update_data(crypted=message.text)

	async with state.proxy() as data:
		with open("DZ\sem_10\children.csv", 'a', newline='', encoding='utf-8') as file:            
			file.write(data['name'] +" "+data['birthday']+ " "+data['class_number']+" "+data['phone']+ '\n')     
	await message.reply(f'Пользователь успешно записан в файл:\n ' + data['name']+" "+data['birthday']+ " "+data['class_number']+" "+data['phone']+'\nВыберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)
    #await message.answer(f'Пользователь успешно записан в файл:\n ' + data['name']+" "+data['birthday']+ " "+data['class_number']+" "+data['phone']+'\n', reply=False)
    #await message.reply('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)

#--------------3. ПРОСМОТР ---------------
@dp.message_handler(commands=['output'])
async def output_file(message: types.Document):
    #await message.reply_document(open('DZ\sem_10\children.csv', 'r', encoding='utf-8'))

    await message.answer('Cписок учеников:')

    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    data_output=file.read().split('\n')
    await message.answer(data_output) 
   
    #await message.reply('Выберите команду. Вызов меню /start или /help', reply=False)
    await message.reply('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)


#--------------4. УДАЛЕНИЕ---------------
@dp.message_handler(commands=['del'])
async def output_file(message: types.Document):
    #global name, reader
    # просмотр файла
    await message.answer('Исходный список учеников:')
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    reader=file.read().split('\n')
    await message.answer(reader) 

    await message.reply("Введите Фамилию ученика, которого(ую) нужно удалить: ")

@dp.message_handler(state=Form.name_del)                 #content_types=['text']
#async def output_file(message: types.Document):
async def output_file(message: types.Document, state: FSMContext):
    async with state.proxy() as data_del:
        data_del['name_del'] = message.text
    #await Form.next()   
    #await message.reply("Введите Фамилию ученика, которого(ую) нужно удалить: ")
    #name_del= message.text
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    reader=file.read().split('\n')
    
    with open('DZ\sem_10\children.csv', mode='w', encoding='utf-8') as file_out:
        for line in reader: # читаем построчно
            if data_del['name_del'] not in line:
                file_out.write(line+ '\n') # пишем прочитанное
   
    # просмотр нового списка
    await message.answer('Новый список учеников:')
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    reader=file.read().split('\n')
    await message.answer(reader) 

    #await message.reply('Вы удалили данные.\nВыберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)
    await message.reply(f'Вы удалили данные ученика: '+ data_del['name_del'] +'\n')
    await message.reply('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)

#--------------5. РЕДАКТИРОВАНИЕ---------------
# class Form_in(StatesGroup):
#     name_in = State() 
#     birthday_in = State() 
#     class_number_in=State()
#     phone_in=State()
#     name_edit=State()

# @dp.message_handler(commands=['edit'])
# async def output_file_in(message: types.Document):
#     #global name, reader
#     # просмотр файла
#     await message.answer('Исходный список учеников:')
#     file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
#     reader=file.read().split('\n')
#     await message.answer(reader) 

#     await message.reply("Введите Фамилию ученика, которого(ую) нужно редактировать: ")

# @dp.message_handler(state=Form_in.name_edit)
# async def output_file_in(message: types.Document, state: FSMContext):
#     global name_edit
#     async with state.proxy() as data_edit:
#         data_edit['name_edit'] = message.text
#     #name_edit= message.text

#     file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
#     reader=file.read().split('\n')
    
#     with open('DZ\sem_10\children.csv', mode='w', encoding='utf-8') as file_in:
#         for line in reader: # читаем построчно
#             if data_edit['name_edit'] in line:
#                 file_in.write(line+ '\n') # пишем прочитанное
#                 await message.answer('Введите исправленные данные:')

# @dp.message_handler(state=Form_in)
# async def cmd_start_in(message: types.Message):
#     await Form_in.name_in.set()
#     await message.reply("ФИО") 

# # Сюда приходит ответ с именем
# @dp.message_handler(state=Form_in.name_in)
# async def process_name_in(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name_in'] = message.text
#     await Form_in.next()     
#     await message.answer("Дата рождения ") 

# @dp.message_handler(state=Form_in.birthday_in)
# async def process_birthday_in(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['birthday_in'] = message.text
#     await Form_in.next()   
#     await message.answer("Номер класса ") 

# @dp.message_handler(state=Form_in.class_number_in)
# async def process_class_number_in(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['class_number_in'] = message.text
#     await Form_in.next()
#     await message.answer("Номер телефона ")

# @dp.message_handler(state=Form_in.phone_in)
# async def process_phone_in(message: types.Message, state: FSMContext):
#     global name_edit

#     async with state.proxy() as data:
#         data['phone_in'] = message.text
#         await bot.send_message(
#             message.chat.id,
#             md.text(                
#                 md.text('Вы ввели,\nФИО:', md.bold(data['name_in'])),
#                 md.text('Дата рождения:', md.code(data['birthday_in'])),
#                 md.text('Номер класса:', md.code(data['class_number_in'])),
#                 md.text('Номер телефона:', md.code(data['phone_in'])),
#                 sep='\n',
#             ),            
#             parse_mode=ParseMode.MARKDOWN,
#         )
#         await message.answer("Данные успешно отредактированы! Не забудьте их сохранить, команда /save или вызов меню /help")
#         #await message.answer('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)
#         await state.finish()  

#     # просмотр нового списка
#     await message.answer('Новый список учеников:')
#     file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
#     reader=file.read().split('\n')
#     await message.answer(reader) 

#     #await message.reply('Вы удалили данные.\nВыберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)
#     await message.reply(f'Вы отредактировали данные ученика: '+ name_edit +'\n')
#     await message.reply('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/edit - редактировать\n/help - помощь', reply=False)



####################################
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




# import logging
# from config import TOKEN
# import bot
# from bot import *
# from keyboards import *
# import aiogram.utils.markdown as md
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# #from aiogram.dispatcher import FSMContext
# #from aiogram.dispatcher.filters import Text
# #from aiogram.dispatcher.filters.state import State, StatesGroup
# #from aiogram.types import ParseMode
# from aiogram.utils import executor

# #from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # pip install aiogram
# from aiogram import Dispatcher, Bot, executor, types
# #from random import randint, choice
# #from string import ascii_letters, digits, punctuation

# # bot = Bot(token=TOKEN)
# # storage = MemoryStorage()
# # dp = Dispatcher(bot, storage=storage)
# # # #dispatcher = Dispatcher(bot)
# # #dp = Dispatcher(bot)
# # # # Включаем логирование, чтобы не пропустить важные сообщения
# # logging.basicConfig(level=logging.INFO)
# bot = Bot(token=TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

# #-----------------МЕНЮ-------------------
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await bot.send_message(message.from_user.id, f"Добро пожаловать, {message.from_user.first_name} в справочник учеников! Выберите команду: ", reply_markup=main_menu)


# @dp.message_handler()
# async def messages(message: types.Message):
#     if message.text == 'Добавить':
#         #await bot.send_message(message.from_user.id, reply_markup=types.ReplyKeyboardRemove(btn_add))
#         await message.answer('Добавьте ученика',reply_markup=btn_add.as_markup(resize_keyboard=True))

#         #await bot.send_message(message.from_user.id, cmd_start=True)
#         #await bot.send_message(btn_add.as_markup(resize_keyboard=True))
#     elif message.text == 'Сохранить':
#         #password = "".join([choice(str(digits + ascii_letters + punctuation)) for _ in range(24)])
#         await bot.send_message(message.from_user.id, f'Вы сохранили данные ученика ')
#     elif message.text == 'Просмотр':
        
#         await bot.send_message(message.from_user.id, 'Открываю...', reply_markup=main_menu)
#     elif message.text == 'Удаление':
#         await bot.send_message(message.from_user.id, f'Вы удалили данные')
#     elif message.text == 'Редактирование':
#         await bot.send_message(message.from_user.id, 'Вы отредактировали данные', reply_markup=main_menu)
#     else:
#         await bot.send_message(message.from_user.id, f'😐 Ботик вас не понял... :(')


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

# ----------------------------------

# States

# class Form(StatesGroup):
#     name = State()  
#     birthday = State()
#     class_number=State()
#     phone=State()

# @dp.message_handler(commands='start')
# async def cmd_start(message: types.Message):  #  Точка входа в разговор
#         # Set state-Установить состояние
#     await Form.name.set()
#     #await message.reply("ФИО ученика")
#     #await message.answer("ФИО ученика")
#     await message.answer("ФИО / Дата рождения / Класс / Телефон ученика")
#     #name=message.text

# async def process_name(message: types.Message, state: Form): 
#     #print(message.text)
#     async with state.proxy() as data:
#         data['name']=message.text
#     await Form.next()
#     #await Form.birthday.set()
#     async with state.proxy() as data:
#         await message.answer(str(data))
#     await message.answer('Данные введены')
#     await state.finish()
    #await message.reply("Дата рождения: ")
    #await message.answer("Дата рождения: ")

# async def process_birthday(message: types.Message, state: Form): 
#     #print(message.text)
#     async with state.proxy() as data:
#         data['birthday']=message.text
#     #await Form.birthday.set()
#     await Form.next()
#     await message.reply("Номер класса ")
#     #await message.answer("Номер класса ")   

# async def process_class_number(message: types.Message, state: Form): 
#     #print(message.text)
#     async with state.proxy() as data:
#         data['class_number']=message.text
#     #await Form.birthday.set()
#     await Form.next()
#     await message.reply("Номер телефона ")
#     #await message.answer("Номер телефона ")  

# async def process_phone(message: types.Message, state: Form): 
#     #print(message.text)
#     async with state.proxy() as data:
#         data['phone']=message.text
#     #await Form.birthday.set()
#     #await Form.next()
#     #await message.reply("birthday ")
#     #await message.answer("Номер телефона ")  
#     async with state.proxy() as data:
#         await message.answer(str(data))
#     await message.answer('Данные введены')
#     await state.finish()
   #-----------------------------------------------------------------
#     await Form.next()
#     await message.reply("День рождение ученика:")
    # bot.send_message(chat_id=message.chat.id, text='Привет, как твое имя?')
    # bot.register_next_step_handler(message, get_name)

# @dp.message_handler(commands='start')
# async def cmd_start(message: types.Message):  #  Точка входа в разговор
#         # Set state-Установить состояние
#     await Form.name.set()
#     await message.reply("ФИО ученика")

# # # You can use state '*' if you need to handle all states - 
# # # Вы можете использовать состояние '*', если вам нужно обрабатывать все состояния
# # @dp.message_handler(state='*', commands='cancel')

# # @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
# # async def cancel_handler(message: types.Message, state: FSMContext):
# #     # Разрешить пользователю отменять любое действие
    
# #     current_state = await state.get_state()
# #     if current_state is None:

# #         return

# #     logging.info('Cancelling state %r', current_state)
# #     # Cancel state and inform user about it
# #     await state.finish()
# #     # And remove keyboard (just in case)
# #     await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


# @dp.message_handler(state=Form.name)  # ИМЯ
# async def process_name(message: types.Message, state: FSMContext):
#     # Имя пользователя процесса
    
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await Form.next()
#     await message.reply("День рождение ученика:")

# # # Check age. Age gotta be digit - Проверьте возраст. Возраст должен быть цифрой
# # @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.age)
# # async def process_age_invalid(message: types.Message):
# #     # Если возраст неверный 
# #     # Возраст должен быть числом.\nСколько вам лет? (только цифры)   
# #     return await message.reply("Возраст должен быть числом.\nСколько вам лет? (только цифры)")

# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.birthday)
# async def process_birthday(message: types.Message, state: FSMContext):   # День рождения
#     # Update state and data - Обновление состояния и данных
#     async with state.proxy() as data:
#         data['birthday'] = message.text
#     await Form.next()
#     await state.update_data(birthday=message.text)
#     await message.reply("Номер класса:")

#     # # Configure ReplyKeyboardMarkup - Настройка ReplyKeyboardMarkup
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
#     # markup.add("Male", "Female")
#     # markup.add("Other")
#     # await message.reply("What is your gender?", reply_markup=markup)

# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.class_number)
# async def process_class_number(message: types.Message, state: FSMContext):   # День рождения
#     # Update state and data - Обновление состояния и данных
#     async with state.proxy() as data:
#         data['class_number'] = message.text
#     await Form.next()
#     await state.update_data(class_numbe=message.text)
#     await message.reply("Номер класса:")

# @dp.message_handler(lambda message: message.text.isdigit(), state=Form.phone)
# async def process_class_number(message: types.Message, state: FSMContext):   # День рождения
#     # Update state and data - Обновление состояния и данных
#     async with state.proxy() as data:
#         data['phone'] = message.text
#     await Form.next()
#     await state.update_data(phone=int(message.text))
#     await message.reply("Номер телефона:")

#     # async def process_gender(message: types.Message, state: FSMContext):
#     #     async with state.proxy() as data:
#     #         data['gender'] = message.text

#     #     # Remove keyboard -Удалить клавиатуру
#     #     markup = types.ReplyKeyboardRemove()

#         # And send message - И отправить сообщение
#     await bot.send_message(
#         message.chat.id,
#         md.text(
#             md.text('Вы добавили ученика:', md.bold(data['name'])),
#             md.text('Дата рождения:', md.code(data['birthday'])),
#             md.text('Номер класса:', md.code(data['class_number'])),
#             md.text('Телефон: ', md.code(data['phone'])),
#             #md.text('Gender:', data['gender']),
#             sep='\n',
#         ),
#         #reply_markup=markup,
#         parse_mode=ParseMode.MARKDOWN,
#     )

#     # Finish conversation - Завершить разговор
#     await state.finish()

# @dp.message_handler(lambda message: message.text not in ["Male", "Female", "Other"], state=Form.gender)
# async def process_gender_invalid(message: types.Message):
#     # В этом примере пол должен быть одним из: Мужской, Женский, Другой.
    
#     return await message.reply("Bad gender name. Choose your gender from the keyboard.")



#@dp.message_handler(state=Form.gender)
# async def process_gender(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['gender'] = message.text

#         # Remove keyboard -Удалить клавиатуру
#         markup = types.ReplyKeyboardRemove()

#         # And send message - И отправить сообщение
#         await bot.send_message(
#             message.chat.id,
#             md.text(
#                 md.text('Hi! Nice to meet you,', md.bold(data['name'])),
#                 md.text('Age:', md.code(data['age'])),
#                 md.text('Gender:', data['gender']),
#                 sep='\n',
#             ),
#             reply_markup=markup,
#             parse_mode=ParseMode.MARKDOWN,
#         )

#     # Finish conversation - Завершить разговор
#     await state.finish()

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # pip install aiogram
# from aiogram import Dispatcher, Bot, executor, types
# from random import randint, choice
# from string import ascii_letters, digits, punctuation
# from main import *

# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await bot.send_message(message.from_user.id, f"👋 Добро пожаловать, {message.from_user.first_name} в справочник учеников! Выберите команду: ", reply_markup=main_menu)


# @dp.message_handler()
# async def messages(message: types.Message):
#     if message.text == 'Добавить':
#         await bot.send_message(message.from_user.id, f'Добавить нового ученика: ')
#     elif message.text == 'Сохранить':
#         #password = "".join([choice(str(digits + ascii_letters + punctuation)) for _ in range(24)])
#         await bot.send_message(message.from_user.id, f'Вы сохранили данные ученика ')
#     elif message.text == 'Просмотр':        
#         await bot.send_message(message.from_user.id, 'Вы открыли просмотр списка', reply_markup=main_menu)
#     elif message.text == 'Удаление':
#         await bot.send_message(message.from_user.id, f'Вы удалили данные')
#     elif message.text == 'Редактирование':
#         await bot.send_message(message.from_user.id, 'Вы отредактировали данные', reply_markup=main_menu)
#     else:
#         await bot.send_message(message.from_user.id, f'😐 Ботик вас не понял... :(')

# # from aiogram import types
# # #from aiogram.dispatcher import Dispatcher
# # from aiogram.utils import executor
# # from aiogram.dispatcher.filters import Text
# # #from config import TOKEN
# # from aiogram.dispatcher.filters.state import StatesGroup, State
# # from aiogram import Bot, Dispatcher, executor, types
# # from aiogram.dispatcher import FSMContext
# # from main import *
# # from aiogram.contrib.fsm_storage.memory import MemoryStorage
# # import logging
# # from config import TOKEN


# # bot = Bot(token=TOKEN)
# # storage = MemoryStorage()
# # dp = Dispatcher(bot, storage=storage)
# # # #dispatcher = Dispatcher(bot)
# # #dp = Dispatcher(bot)
# # # # Включаем логирование, чтобы не пропустить важные сообщения
# # logging.basicConfig(level=logging.INFO)

# # class Form(StatesGroup):
# #     name = State()  
# #     birthday = State()
# #     class_number=State()
# #     phone=State()

# # @dp.message_handler(commands='Добавить')
# # async def cmd_start(message: types.Message):  #  Точка входа в разговор
# #         # Set state-Установить состояние
# #     await Form.name.set()
# #     await message.reply("ФИО ученика")
# #     #await message.answer("ФИО ученика")
# #     #await message.answer("ФИО / Дата рождения / Класс / Телефон ученика")
# #     #name=message.text

# # async def process_name(message: types.Message, state: Form): 
# #     #print(message.text)
# #     async with state.proxy() as data:
# #         data['name']=message.text
# #     await Form.next()
# #     #await Form.birthday.set()
# #     async with state.proxy() as data:
# #         await message.answer(str(data))
# #     await message.answer('Данные введены')
# #     await state.finish()

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # pip install aiogram
# #from aiogram import Dispatcher, Bot, executor, types
# #from random import randint, choice
# #from string import ascii_letters, digits, punctuation

# # Создание клавиатуры
# btn_add = KeyboardButton('Добавить')
# btn_save = KeyboardButton('Сохранить')
# btn_output = KeyboardButton('Просмотр')
# btn_del= KeyboardButton('Удаление')
# btn_editing = KeyboardButton('Редактирование')

# main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_add, btn_save, btn_output, btn_del,btn_editing)

