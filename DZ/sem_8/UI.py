import datetime as dt
import loggin as log

def add_view():
    #data=input('Введите через пробел Имя / Фамилия / Дата рождения / Номер класса / Телефон')
    global name
    global surname
    global birthday
    global class_number
    global phone

    name=input("Введите Имя: ")
    surname=input("Введите Фамилию: ")
    # birthday = dt.datetime.strptime(input("Введите дату рождения (dd/mm/yyyy): "), '%d/%m/%Y').date()
    # class_number = input("Введите класс: ")
    # phone = input('Введите телефоны через запятую: ')
    # data = [name, surname,birthday, class_number, phone]
    #data.append([name],[surname])
    # #phone = [int(i) for i in input('Введите телефоны через запятую: ').split(',')]
    #log.save_data(data)
    log.save_data(name , surname)
    # #list_data=data.split(" ")
    # #data.append(name, surname, birthday, class_number, phone)
    return name, surname
    #, surname, birthday, class_number, phone
    #return data

# def save_view(data):
#     log.save_data(data)
#     return 