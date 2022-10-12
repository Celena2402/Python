from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(device=1):
    xml='<xml>\n'
    xml+='   <Temperature units= "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml+='   <Pressure units="mmHg">{}</pressure>\n'\
        .format(pressure_view(device))
    xml+='   <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(wind_speed_view(device))
    xml+='</xml>'

    with open('lecture\lecture_4\join_job\data.xml', 'w') as page:
        page.write(xml)

    return xml

def new_create(data, device = 1):
    t,p,w=data
    t=t*1.8+32 # температура будет выводиться по Фарингейту
    xml='<xml>\n'
    xml+='   <Temperature units= "f">{}</temperature>\n'\
        .format(t)
    xml+='   <Pressure units="mmHg">{}</pressure>\n'\
        .format(p)
    xml+='   <wind_speed units = "m/s">{}</wind_speed>\n'\
        .format(w)
    xml+='</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data