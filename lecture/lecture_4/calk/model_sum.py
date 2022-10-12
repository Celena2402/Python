from re import X

# метод отвечающий за иниализацую 2-х переменных х и у
x=0
y=0

def init(a,b):
    global x
    global y
    x=a
    y=b

#init(11,22)

#print(x)
#print(y)

# медок который будет складывать два числа
def do_it(): # вместо sum
    return x+y