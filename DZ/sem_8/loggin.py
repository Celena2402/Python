import UI
from datetime import datetime as dt
from time import time

#def add_data(data):
#    UI.data.append(name, surname, birthday, class_number, phone)
#data.append([UI.add_view(name)],[UI.add_view(surname)])





# def delete_data():



# def edit_data():



def save_data(data):
    global name
    global surname
    global birthday
    global class_number
    global phone

    name, surname,birthday, class_number, phone=data
    time=dt.now().strftime('%d/%m/%Y %H:%M')
    with open('DZ\sem_8\log.cvn','a', encoding='utf-8') as file:
        #for idx, line in enumerate(file, start=1):
            #file.write('{} {}  {} '.format(idx, time, data))
        #    file.write(f'{idx} {time} {name}  {surname} {birthday} {class_number} {phone}')
        #file.write(f'{time} {UI.name}  {UI.surname} {UI.birthday} {class_number} {phone}')
        file.writelines(f'{time} {name}  ')
            


# def output_data():


# def exit():
