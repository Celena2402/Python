# Задача2: Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:- [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

import random


def NewList(n):
    new_list = [random.randint(0, 20) for i in range(n)]
    return new_list


def ProductNumbers(new_list):
    list1 = []

    if len(list) % 2 == 0:
        leng = len(list) // 2
    else:
        leng = len(list) // 2 + 1

    for i in range(0, leng):
        pr = new_list[i] * new_list[len(new_list) - i - 1]
        list1.append(pr)
    return list1


n = int(input('Введите количество элементов в списке: '))
list = NewList(n)
print('Исходный список: ', list)
print('Произведение пар чисел списка:', ProductNumbers(list))
