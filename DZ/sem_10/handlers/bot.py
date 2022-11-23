from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import aiogram.utils.markdown as md
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
import csv
from creat_bot import *

#--------------1. ДОБАВЛЕНИЕ---------------
# создаём форму и указываем поля
class Form(StatesGroup):
    name = State() 
    birthday = State() 
    class_number=State()
    phone=State()
    name_del=State()
    
# Начинаем наш диалог
# @dp.message_handler(commands=['add'])
async def cmd_start(message: types.Message):
    await Form.name.set()
    await message.reply("ФИО")    

# Сюда приходит ответ с именем
# @dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Form.next()
    await message.answer("Дата рождения ") 

# @dp.message_handler(state=Form.birthday)
async def process_birthday(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['birthday'] = message.text
    await Form.next()
    await message.answer("Номер класса ") 

# @dp.message_handler(state=Form.class_number)
async def process_class_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['class_number'] = message.text
    await Form.next()
    await message.answer("Номер телефона ")

# @dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
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

#@dp.message_handler(commands=['save'])
async def save_to_CSV(message: types.Message, state: FSMContext):    
	await state.update_data(crypted=message.text)
	async with state.proxy() as data:
		with open("DZ\sem_10\children.csv", 'a', newline='', encoding='utf-8') as file:            
			file.write(data['name'] +" "+data['birthday']+ " "+data['class_number']+" "+data['phone']+ '\n')     
	await message.reply(f'Пользователь успешно записан в файл:\n ' + data['name']+" "+data['birthday']+ " "+data['class_number']+" "+data['phone']+'\nВыберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/help - помощь', reply=False)
    

# #--------------3. ПРОСМОТР ---------------
#@dp.message_handler(commands=['output'])
async def output_file(message: types.Document):
    #await message.reply_document(open('DZ\sem_10\children.csv', 'r', encoding='utf-8'))

    await message.answer('Cписок учеников:')
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    data_output=file.read().split('\n')
    await message.answer(data_output) 
   
    await message.reply('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/help - помощь', reply=False)


# #--------------4. УДАЛЕНИЕ---------------
#@dp.message_handler(commands=['del'])
async def del_file(message: types.Document):
    await message.answer('Исходный список учеников:')
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    reader=file.read().split('\n')
    await message.answer(reader) 

    await message.reply("Введите Фамилию ученика, которого(ую) нужно удалить: ")

#@dp.message_handler(content_types=['text']) 
async def del_name(message: types.Document):
    name_del= message.text
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    reader=file.read().split('\n')
    
    with open('DZ\sem_10\children.csv', mode='w', encoding='utf-8') as file_out:
        for line in reader: # читаем построчно
            if name_del not in line:
                file_out.write(line+ '\n') # пишем прочитанное
   
    # просмотр нового списка
    await message.answer('Новый список учеников:')
    file=open('DZ\sem_10\children.csv', 'r', encoding='utf-8')
    reader=file.read().split('\n')
    await message.answer(reader) 

    await message.reply(f'Вы удалили данные ученика: '+ name_del +'\n')
    await message.reply('Выберите команду:\n/add - добавить\n/save - сохранить\n/output - просмотр\n/del - удалить\n/help - помощь', reply=False)



def register_handlers_add(dp:Dispatcher):
    dp.register_message_handler(cmd_start, commands=['add'])
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_birthday, state=Form.birthday)
    dp.register_message_handler(process_class_number, state=Form.class_number)
    dp.register_message_handler(process_phone, state=Form.phone)
    dp.register_message_handler(save_to_CSV, commands=['save'])
    dp.register_message_handler(output_file, commands=['output'])
    dp.register_message_handler(del_file, commands=['del'])
    dp.register_message_handler(del_name, content_types=['text'])
    
