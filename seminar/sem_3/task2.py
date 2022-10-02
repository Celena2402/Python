# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.


lst = ["dfgf", "gfj", "2zxc", "dgdf", "dfgf"]
N = input("Введите строку: ")

counter = 0
target_counter = 2

for i, el in enumerate(lst):
#for i in range(len(lst)):
#    if N == lst[i]:
    if N == el:    
        counter += 1
        if counter == target_counter:
            print(
                f'Строка {N} найдена в списке. Ее {counter} нахождение в списке под индексом {i}')
            break
else:
    print("Строка не надена или найдена недостаточное количество раз")
        
