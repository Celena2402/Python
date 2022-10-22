import datetime as dt
from datetime import datetime 
from distutils.file_util import write_file
from time import time
import csv
from csv import writer

# 1. ввод данных
def add_view():
    global name
    global surname
    global birthday
    global class_number
    global phone

    name=input("Введите Имя: ")
    surname=input("Введите Фамилию: ")
    birthday = dt.datetime.strptime(input("Введите дату рождения (dd/mm/yyyy): "), '%d/%m/%Y').date()
    class_number = input("Введите класс: ")
    phone = input('Введите телефоны через запятую: ')

    print('-' * 50)
    print('Данные внесены правильно, теперь нужно сохранить')
    print('-' * 50)
    return name, surname, birthday, class_number, phone
    

# 2. сохранение
def save_view():
    global name
    global surname
    global birthday
    global class_number
    global phone

    time=datetime .now().strftime('%d/%m/%Y %H:%M')
    
    with open('DZ\sem_8\children_1.csv','a', newline='',encoding='utf-8') as file:
        writer_fail = csv.writer(file, delimiter='|', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer_fail.writerow([time] + [name] + [surname] + [birthday] + [class_number] + [phone])
        print()
       
        file.close()
    print('-' * 50)
    print('Ученик добавлен')
    print('-' * 50)

    return name, surname, birthday, class_number, phone

# 3. просмотр
def output_view():
    with open('DZ\sem_8\children_1.csv',encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|', quotechar='|')
        
        for index, line in enumerate(file, start=1):
            print(index, ''.join(line))
        file.close()    
    
    print('-' * 50)
    print('---Вы просмотрели весь список учеников.----')
    print('-' * 50)
    



