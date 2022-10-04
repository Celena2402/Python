# 3. Задайте два числа. Напишите программу, которая найдет НОК
# (наименьшее общее кратное) этих двух чисел.

x=int(input())
y=int(input())

if x>y:
    Maxi=x
else:
    Maxi=y

while True:
    if not Maxi % x and not Maxi % y:
        print(Maxi)
        break
    Maxi+=1

# 2.
#from math import lcm
#a,b=tuple(map(int, input('Введите числа через пробел: ').split()))
#print(f'lcm={lcm(a,b)}')

# 3.
#from math import lcm
#a,b=tuple(map(int, input('Введите числа через пробел: ').split()))
#def gcd(x,y):
#    if y>x:
#        x,y=y,x

#    if y==0:
#        return x

#    return gcd(y,x % y)

#print(f'lcm={a*b/(gcd(a,b))}')