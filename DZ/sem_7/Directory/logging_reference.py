from datetime import datetime as dt
from time import time

# модуль отвечает за логирование. Запись информации в файл log.cvn
# хранение данных в столбце

# def name_logger(data):
#     time=dt.now().strftime('%d/%m/%Y %H:%M\n')
#     with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
#         file.write('{}Name (Имя): {}\n'.
#         format(time, data))

# def surname_logger(data):
#     with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
#         file.write('Surname (Фамилия): {}\n'.
#         format(data))

# def birthday_logger(data):
#     with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
#         file.write('Birthday (Дата рождения): {}\n'.
#         format(data))

# def place_work_logger(data):
#     with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
#         file.write('Place_work (Место работы): {}\n'.
#         format(data))

# def phone_logger(data):
#     with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
#         file.write('Phone (Телефон): {}\n\n'.
#         format(data))


# хранение данных в строке
def name_logger(data):
    time=dt.now().strftime('%d/%m/%Y %H:%M')
    with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
        file.write('{}; Name (Имя): {}; '.
        format(time, data))

def surname_logger(data):
    with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
        file.write('Surname (Фамилия): {}; '.
        format(data))

def birthday_logger(data):
    with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
        file.write('Birthday (Дата рождения): {}; '.
        format(data))

def place_work_logger(data):
    with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
        file.write('Place_work (Место работы): {}; '.
        format(data))

def phone_logger(data):
    with open('DZ\sem_7\Directory\log.cvn','a', encoding='utf-8') as file:
        file.write('Phone (Телефон): {}\n'.
        format(data))




