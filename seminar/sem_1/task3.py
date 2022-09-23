#3. Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N
#     *Примеры:*
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

#number=int(input("Введите А: "))

#for i in range(-a,a):
#    print (i)

#for value in range(-number, number+1):
#    print(value, end=', ')

# второй вариант
number=int(input())

print(*range(-number,number+1),sep=',')