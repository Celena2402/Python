# 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
#      Пример: 6782 -> 23; 0,56 -> 11

num = float(input('Введите число N: '))
#number = num * 10 ** 2
leng_num = len(str(num))
number = num * 10 ** (leng_num - 2)

sum = 0
while (number > 0):
    sum = sum + number % 10
    number = number // 10

print('Сумма чисел у числа', num, 'равна', sum)