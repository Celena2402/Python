from UI_reference import name_view
from UI_reference import surname_view
from UI_reference import birthday_view
from UI_reference import place_work_view
from UI_reference import phone_view

def create(device=1):
    xml='<xml>\n'
    xml+='   <Name (Имя)>{}</name>\n'\
        .format(name_view(device))
    xml+='   <Surname (Фамилия):>{}</surname>\n'\
        .format(surname_view(device))
    xml+='   <Birthday (Дата рождения)>{}</birthday>\n'\
        .format(birthday_view(device))
    xml+='   <Place_work (Место работы):>{}</place_work>\n'\
        .format(place_work_view(device))
    xml+='   <Phone (Номер телефона):>{}</phone>\n'\
        .format(phone_view(device))
    xml+='</xml>'

    with open('DZ\sem_7\Directory\data.xml', 'w', encoding='utf-8') as page:
        page.write(xml)

    return xml