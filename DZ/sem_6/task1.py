# Задача 1
#       Напишите программу вычисления арифметического выражения заданного строкой.
#       Используйте операции +,-,/,*. приоритет операций стандартный.
#       Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
#       Добавьте возможность использования скобок, меняющих приоритет операций.
#       Пример: 1+2*3 => 7; (1+2)*3 => 9;


import math

example = input("Введите выражение через пробел: ")
# example = '3 + ( 9 - 6 ) * ( 8 - 4 ) + 8 / 2'     # результат 19

# 1.
#num = eval(input('Введите выражение: '))
num = eval(str(example))
print(f'Результат выражения равен = {num}')

# 2.
func = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


# раскрытие скобок, разбитие выражения
def parenthesis_expansion(line_example):
    new_lst = []
    i = 0
    while i < len(line_example):
        if line_example[i] == '(':
            n = line_example.index(')', i)
            new_lst.append(line_example[i + 1:n])
            i = n
        else:
            new_lst.append(line_example[i])
        i += 1
    return new_lst


def solution_brackets(new_lst):  # решение в скобках
    for i in range(len(new_lst)):
        if isinstance(new_lst[i], list):         # проверка принадлежности
            a, b, c = parenthesis_expansion(new_lst[i])
            new_lst[i] = func[b](a, c)           # вычисляется в скобках
    return new_lst


def calculation(new_lst):                         # вычисление
    # enumerate()– узнаем сразу индекс элемента и его значение
    first_lst = [i for i, j in enumerate(new_lst) if j in '*/']
    while first_lst:
        t = first_lst[0]
        a, b, c = new_lst[t - 1: t + 2]
        new_lst.insert(t - 1, func[b](a, c))
        # удаление переменной из списка
        del new_lst[t: t + 3]
        first_lst = [i for i, j in enumerate(new_lst) if j in '*/']

    while len(new_lst) > 1:
        a, b, c = new_lst[:3]
        del new_lst[:3]
        new_lst.insert(0, func[b](a, c))
    return new_lst


# example =input("Введите выражение через пробел: ")
# example = '3 + ( 9 - 6 ) * ( 8 - 4 ) + 8 / 2'     # результат 19
# print(example)
# print(parenthesis_expansion(example.split()))
# print(solution_brackets(parenthesis_expansion(example.split())))
res = calculation(solution_brackets(parenthesis_expansion(example.split())))
print(f'Результат выражения равен= {str(res)[2:-2].replace(",", "")}')
