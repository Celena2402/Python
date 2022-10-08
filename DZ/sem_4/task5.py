# Задача 5. 
#       Даны два файла, в каждом из которых находится запись многочлена. 
#       Задача - сформировать файл, содержащий сумму многочленов.


from fileinput import close
import re
import itertools


fail1 = 'DZ/sem_4/task_4_1.txt'
fail2 = 'DZ/sem_4/task_4_2.txt'
fail3 ='DZ/sem_4/task5_fail3_sum.txt'

# Получение данных из файла
def ReadFile(fail):
    with open (str(fail),'r') as data:
        polynomial=data.read()
    return polynomial

# Получение списка кортежей каждого (<коэффициент>, <степень>)
def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol


print('Первый многочлен из file_1.txt: ')
polynomial1=ReadFile(fail1)
print(polynomial1)

print('Второй многочлен из file_2.txt: ')
polynomial2=ReadFile(fail2)
print(polynomial2)

# полученик кортежей (коэффициент и степень)
polinom_1 = convert_pol(polynomial1)
polinom_2 = convert_pol(polynomial2)
#print(polinom_1)
#print(polinom_2)

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)
x = [0] * (max(polinom_1[0][1], polinom_2[0][1] + 1))
for i in polinom_1 + polinom_2:
    x[i[1]] += i[0]
polinom_sum = [(x[i], i) for i in range(len(x)) if x[i] != 0]
polinom_sum.sort(key = lambda r: r[1], reverse = True)

#print(polinom_sum)  # вывод кортежа (суммы коэф и степени)

# Составление итогового многочлена
var = ['*x^'] * len(polinom_sum)
coefs = [x[0] for x in polinom_sum]
degrees = [x[1] for x in polinom_sum]
polinom_3 = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
for x in polinom_3:
    if x[0] == '0': del (x[0])
    if x[-1] == '0': del (x[-1], x[-1])
    if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
    if len(x) > 1 and x[-1] == '1':
        del x[-1]
        x[-1] = '*x'
    x.append(' + ')
polinom_3 = list(itertools.chain(*polinom_3))
polinom_3[-1] = ' = 0'
print('Cумма 1 и 2 многочлена:')
print("".join(map(str, polinom_3)))

with open('DZ/sem_4/task5_fail3_sum.txt', 'w', encoding='utf-8') as data:
    data.write("".join(map(str, polinom_3)))
