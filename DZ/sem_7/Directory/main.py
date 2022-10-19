# Задача: 
# Написать программу по импорту и экспорту телефонного справочника состоящий 
# из N тысяч строк,       содержащих информацию о неких пользователях.
#     
# Предлагаемые поля: id, имя, фамилия, день рождения, место работы, номер телефона 
# (может быть несколько). В качестве символа разделителя использовать пустую строку (пустой символ).
# Программа должна быть модульной (как показывалось на уроке). Она должна уметь 
# генерировать справочник и сохранять его в файл при необходимости (экспорт) или 
# загружать (импорт). Также необходимо организовать просмотр информации из справочника 
# (генерируемого или загружаемого).
#       В качестве формата файла можно использовать форматы csv, json, xml


import UI_reference as ui
import logging_reference as lr
import html_reference as hr
import xml_referebce as xr

ui.name_view(lr.name_logger)
ui.surname_view(lr.surname_logger)
ui.birthday_view(lr.birthday_logger)
ui.place_work_view(lr.place_work_logger)
ui.phone_view(lr.phone_logger)

# вывод справочника в консоль
print()
print('Содержимое справочника: ')
print(lr.write_reference())

#print(hr.create())  # html
#print(xr.create())  # xml
