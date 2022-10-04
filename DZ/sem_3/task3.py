# Задача 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
#     Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.20

import random


def RealNumbers(n):
    new_list = []
    # for i in range(n):
    #    new_list.append(round(random.uniform(0, 10),2))
    new_list = [round(random.uniform(0, 10), 2) for i in range(n)]
    return new_list


def FractionalPart(new_list):
    for i in range(0, n):
        new_list[i] = round(new_list[i] % 1, 2)
    return new_list


def MaxMin(new_list):  # метод перебора
    max_list = new_list[0]
    min_list = new_list[0]
    for i in new_list:
        if i > max_list:
            max_list = i
        elif i < min_list:
            min_list = i
    MinMax = [max_list, min_list]
    return MinMax


n = int(input('Введите количество элементов в списке n= '))

list = RealNumbers(n)  # исходный список
print(list)

part_list = FractionalPart(list)  # дробные части списка
print(part_list)

# нахождение max и min с помощью встроенной функции
max_list=max(part_list)
min_list=min(part_list)
print(f'max= {max_list}, min= {min_list}, max-min= {round((max_list-min_list),2)}')

# нахождение max и min методом перебора
max_min = MaxMin(part_list)
#print(max_min)
diff = round(max_min[0]-max_min[1], 2)
print(f'max= {max_min[0]}, min= {max_min[1]}, max-min= {diff}')
