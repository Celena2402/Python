# Задача 1.
#       Вычислить число c заданной точностью d
#       Пример: - при d = 0.001, π = 3.141,    10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal
n = Decimal(input('Введите вещественное число N= '))
d = Decimal(input('Введите точно сть d= '))
#d=len(input("Введите число d с заданной точностью:\n").split(".")[1])

number = n.quantize(Decimal(d))

print(f'Если число {n} округлить с точностью {d}, то получится число {number}')
