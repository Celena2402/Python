import logging_reference as log
import datetime as dt

#ввод данных

def name_view(number):
    data=input("Введите ваше Имя: ")
    log.name_logger(data)
    return data

def surname_view(number):
    data=input("Введите вашу Фамилию: ")
    log.surname_logger(data)
    return data

def birthday_view(number):
    date_str = input("Введите дату рождения (dd/mm/yyyy): ")
    data = dt.datetime.strptime(date_str, '%d/%m/%Y').date()
    log.birthday_logger(data)
    return data

def place_work_view(number):
    data=input("Введите место работы: ")
    log.place_work_logger(data)
    return data

def phone_view(number):
    data=[int(i) for i in input('Введите телефоны через запятую: ').split(',')]
    log.phone_logger(data)
    return data

