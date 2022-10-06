# Задача 4. 
#       Задана натуральная степень k. Сформировать случайным образом 
#       список коэффициентов (значения от 0 до 100) многочлена и 
#       записать в файл многочлен степени k.
#           Пример:
#           - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
import itertools

k=int(input('Введите степень многочлена k= '))
odds = [random.randint(0, 100) for i in range(k+1)]
print(odds)


def getPolynomial(k, odds):
    template = ['*x^'] * (k - 1) + ['*x']
    #items=['+','-']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(odds, template, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ') 
        #x.append(items)
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


#k = randint(2, 7)
polynom = getPolynomial(k, odds)
print(f'Многочлен степени {k} : {polynom}')

with open('DZ/sem_4/task_4_1.txt', 'w') as data:
    data.write(polynom)


