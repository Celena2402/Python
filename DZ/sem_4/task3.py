# Задача 3. 
#       Задайте последовательность чисел. Напишите программу, 
#       которая выведет список неповторяющихся элементов 
#       исходной последовательности.

data=list(map(int, input('Введите последовательность чисел через пробел ').split()))

new_data=[]

for i in data:
    if i not in new_data:
        new_data.append(i)

print(new_data)



