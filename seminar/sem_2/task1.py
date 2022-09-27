# 1. Напишите программу, которая принимает на вход число N и выдает
# последовательность из N членов
# Пример: N=5: 1, -3, 9, -27,81

# 1-ый вариант
number=int(input('Введите число: '))
print(*((-3)**i for i in range(number)), sep=', ')
print()

# 2-ой вариант
N=int(input('N: '))
output=-1/3
for i in range(N):
    print(int(output:=output*-3), end=', ')
print()

# 3-ый вариант
N=int(input('N: '))
output=-1/3
print(*(output:=int(output*-3) for i in range(N)), sep=', ')