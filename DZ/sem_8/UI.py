import datetime as dt
from datetime import datetime 
from time import time
import csv
from csv import writer

# 1. ввод данных
def add_view():
    global children

    children=[]
    name=input("Введите Имя: ")
    surname=input("Введите Фамилию: ")
    birthday = dt.datetime.strptime(input("Введите дату рождения (dd/mm/yyyy): "), '%d/%m/%Y').date()
    class_number = input("Введите класс: ")
    phone = input('Введите телефоны через запятую: ')
    
    children=[name, surname,str(birthday), str(class_number), str(phone)]
    print('-' * 50)
    print('Вы внесли данные нового ученика(цы): ')
    print(' '.join(children))

    print('-' * 50)
    print('Данные внесены правильно, теперь нужно сохранить. Нажмите - 2')
    print('-' * 50)
    
    return children
    

# 2. сохранение
def save_view():
    global children

    time=datetime .now().strftime('%d/%m/%Y %H:%M')
    
    with open('DZ\sem_8\children.csv','a', newline='',encoding='utf-8') as file:
        writer_fail = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer_fail.writerow([time] + children)
               
        print()
               
    print('-' * 50)
    print('Ученик(ца) добавлен(а)')
    print('-' * 50)

    return children

# 3. просмотр
def output_view():
    
    with open('DZ\sem_8\children.csv',encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')    

        for index, reader in enumerate(file, start=0):
            print(index, ''.join(reader))  
    
    print('-' * 50)
    print('---Вы просмотрели весь список учеников.----')
    print('-' * 50)
    

# 4. Удаление

def del_view():
       # просмотр списка перед удалением
    with open('DZ\sem_8\children.csv',encoding='utf-8') as file:
        file_preview = csv.reader(file, delimiter='|', quotechar='|')    

        for index, file_preview in enumerate(file, start=0):
            print(index, ''.join(file_preview))
   
    # удаление
    with open("DZ/sem_8/children.csv","r",encoding="utf-8") as file_in:
        reader=file_in.readlines()
        
        print('-' * 50)
        data= str(input('Введите Фамилию ученика, которого(ую) нужно удалить: '))
        flag = 1
        with open("DZ/sem_8/children.csv","w", encoding="utf-8") as file_out:
            for line in reader:
                if data not in line:
                    file_out.write(line)
            
            if flag: print('Данные не найдены')             

    print('-' * 50)
    print('---Вы удалили данные ученика----')  
    print('-' * 50)
    print('Просмотр нового списка:')
    print('-' * 50)

    # просмотр нового списка
    with open('DZ\sem_8\children.csv',encoding='utf-8') as file:
        file_preview = csv.reader(file, delimiter='|', quotechar='|')    

        for index, file_preview in enumerate(file, start=0):
            print(index, ''.join(file_preview))
    return data

# редактирование
def editing_view():
    # просмотр списка перед редактированием
    with open('DZ\sem_8\children.csv',encoding='utf-8') as file:
        file_preview = csv.reader(file, delimiter='|', quotechar='|')    

        for index, file_preview in enumerate(file, start=0):
            print(index, ''.join(file_preview))

    # редактирование
    with open("DZ/sem_8/children.csv","r",encoding="utf-8") as file_in:
        reader=file_in.readlines()
        
        print('-' * 50)
        data= str(input('Введите Фамилию/Имя ученика, данные которого нужно изменить: '))
        flag = 1
        time=datetime .now().strftime('%d/%m/%Y %H:%M')
        with open("DZ/sem_8/children.csv","w", encoding="utf-8") as file_out:
            new_children=[]
            for line in reader:
                if data in line:
                    flag=0
                    print(line)
                    print('Введите исправленные данные')
                    name=input("Введите Имя: ")
                    surname=input("Введите Фамилию: ")
                    birthday = dt.datetime.strptime(input("Введите дату рождения (dd/mm/yyyy): "), '%d/%m/%Y').date()
                    class_number = input("Введите класс: ")
                    phone = input('Введите телефоны через запятую: ')    
                    new_children=[name, surname,str(birthday), str(class_number), str(phone)]
                    
                    writer_fail = csv.writer(file_out, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    writer_fail.writerow([time] + new_children)
                   
                else:
                    file_out.write(line)
            
            if flag: print('Данные не найдены')    
    
    print('-' * 50)
    print('---Вы отредактировали данные ученика(цы)----')  
    print('-' * 50)
    print('Просмотр нового списка:')
    print('-' * 50)

    # просмотр нового списка
    with open('DZ\sem_8\children.csv',encoding='utf-8') as file:
        file_preview = csv.reader(file, delimiter='|', quotechar='|')    

        for index, file_preview in enumerate(file, start=0):
            print(index, ''.join(file_preview))
    
    return data, new_children
