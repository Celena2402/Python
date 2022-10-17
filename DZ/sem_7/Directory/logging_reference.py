from datetime import datetime as dt
from time import time

# модуль отвечает за логирование температуры
# def temperature_logger(data):
#     time=dt.now().strftime('%H:%M')
#     with open('lecture\lecture_4\join_job\log.cvn','a') as file:
#         file.write('{}; temperature;{}\n'.
#         format(time, data))
def name_logger(data):
    time=dt.now().strftime('%H:%M')
    with open('DZ\sem_7\Directory\log.cvn','a') as file:
        file.write('{}; name;{}\n'.
        format(time, data))

# def pressure_logger(data):
#     time=dt.now().strftime('%H:%M')
#     with open('lecture\lecture_4\join_job\log.cvn','a') as file:
#         file.write('{}; pressure;{}\n'.
#         format(time, data))


# def wind_speed_logger(data):
#     time=dt.now().strftime('%H:%M')
#     with open('lecture\lecture_4\join_job\log.cvn','a') as file:
#         file.write('{}; wind_speed;{}\n'
#         .format(time, data))


