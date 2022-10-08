# Задача 4. 
#       Задана натуральная степень k. Сформировать случайным образом 
#       список коэффициентов (значения от 0 до 100) многочлена и 
#       записать в файл многочлен степени k.
#           Пример:
#           - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
from random import randint
import itertools

# создаем коэффициенты многочлена
def InputOdds(k):
    odds = [random.randint(0, 100) for i in range(k+1)]
    while odds[0]==0:
        odds[0]=randint(1,100)
    return odds

#создаем сам многочлен
def getPolynomial(k, odds):
    template = ['*x^'] * (k - 1) + ['*x'] 
    # объединяем два списка
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(odds, template, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ') 
    
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')

# записываем многочлен в файл
def WriteFile(file, pol):
    with open(file, 'w', encoding='utf-8') as data:
        data.write(pol)

# вывод первого многочлена
k1 = int(input('Введите степень 1-ого многочлена k= '))
odds1 = InputOdds(k1)
print(odds1)
#odds1=[4,12,0]
polynom_1 = getPolynomial(k1, odds1)
print(f'Многочлен степени {k1} : {polynom_1}')
WriteFile('DZ/sem_4/task_4_1.txt',polynom_1)

# для 5 задачи создаем второй многочлен
k2 = int(input('Введите степень 2-ого многочлена k= '))
odds2 = InputOdds(k2)
print(odds2)
polynom_2 = getPolynomial(k2, odds2)
print(f'Многочлен степени {k2} : {polynom_2}')
WriteFile('DZ/sem_4/task_4_2.txt',polynom_2)

