from random import randint


def get_temperature(senson):
    return randint(-20,0) if senson else randint(0,20)

def get_pressure(senson):
    if senson:
        return randint(720,750)
    else:
        return randint(750,770)

def get_wind_speed(senson):
    if senson==1:
        return randint(0,30)
    else:
        return randint(30,50)

def data_collection(senson=1):
    return (get_temperature(senson), get_pressure(senson), get_wind_speed(senson))


