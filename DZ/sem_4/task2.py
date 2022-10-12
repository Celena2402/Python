# Задача2: 
#      Задайте натуральное число N. Напишите программу, которая 
#       составит список простых множителей числа N.

import math

num = int(input('Введите натрульное число N= '))

prime_factors = []
n = num
while n % 2 == 0:
    prime_factors.append(2)
    n = n//2

for i in range(3, int(math.sqrt(n))+1, 2):
    while (n % i == 0):
        prime_factors.append(i)
        n = n//i

if n!=1:
    prime_factors.append(n)

#print(prime_factors)
print(f'Число {num} можно разложить на множители {prime_factors}')
#print('{} = {}' .format(num, prime_factors))
