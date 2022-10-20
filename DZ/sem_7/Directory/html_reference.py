from UI_reference import name_view
from UI_reference import surname_view
from UI_reference import birthday_view
from UI_reference import place_work_view
from UI_reference import phone_view

def create(device=1):
    style='style="font-size:30px;"'
    html='<html>\n <head></head>\n  <body>\n'
    html+='   <p {}>Name (Имя): {} </p>\n'\
        .format(style, name_view(device))
    html+='   <p {}>Surname (Фамилия): {} </p>\n'\
        .format(style, surname_view(device))
    html+='   <p {}>Birthday (Дата рождения): {} </p>\n'\
        .format(style, birthday_view(device))
    html+='   <p {}>Place_work (Место работы): {} </p>\n'\
        .format(style, place_work_view(device))
    html+='   <p {}>Phone (Номер телефона): {} </p>\n'\
        .format(style, phone_view(device))

    with open('DZ\sem_7\Directory\index.html', 'w', encoding='utf-8') as page:
        page.write(html)

    return html