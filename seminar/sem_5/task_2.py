# Задача 2.
#       Дан список чисел. Создайте список, в который попадают числа,
#       описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#        Пример:
#         [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# 1.
lst = [87, 78, 2, 3, 4, 6, 1, 7]

for i in range(len(lst)):
    result = [lst[i]]
    for j in range(i, len(lst)):
        if lst[j] > result[len(result)-1]:
            result.append(lst[j])
    if len(result) != 1:
        break
print(result)

# 2. с помощью моржового оператора
lst1 = [1, 5, 2, 3, 4, 6, 1, 7]

first = lst1[0]
result = [first := num for num in lst1 if num >= first]

print(result)

# 3 . Находит все комбинации
lst2 = [1, 5, 2, 3, 4, 6, 1, 7]
array = []
for i, el1 in enumerate(lst2):
    for j, el2 in enumerate(lst2[i:]):
        first = el1
        seq = [first]+[first := num for num in lst2[j:] if num > first]
        if seq not in array and len(seq) > 1:
            array.append(seq)
print(*array, sep='\n')
