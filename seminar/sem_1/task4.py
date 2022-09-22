# 4. Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

# 1 вариант
number=float(input('Введите number' ))
if number-int(number)==0:
    print("Нет")
else:
    num=int((number-int(number))*10)
    print(num)

# 2 вариант
number=float(input())
result=(number*10)%10
if result==0:
    print('Нет')
else:
    print(int(result))
