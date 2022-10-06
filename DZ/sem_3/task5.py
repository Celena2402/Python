# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для
#    отрицательных индексов.
#     Пример: - для k = 8 список будет выглядеть так:
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def NeoFibonacci(n):
    a, b = 1, -1
    for i in range(n):
        yield a
        a, b = b, a-b

n = int(input('Введите количество элементов в списке: '))
data0 = [0]
data = list(fibonacci(n))
neo_data = list(NeoFibonacci(n))
# print(data)
# print(neo_data)
print(f'Спиок чисел Негафибоначчи при n={n}:\n{neo_data[::-1] + data0 + data}')
