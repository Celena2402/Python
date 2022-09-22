#2. Напишите программу, которая на вход принимает 5 чисел и 
# находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
d=int(input('d= '))
e=int(input('e= '))

max=a
if b>a:
    max=b
if c>max:
    max=c
if d>max:
    max=d
if e>max:
    max=e

print(max)


#второй вариант
a = 5
data=[]

for count in range(0,a):
    data.append(int(input("Input number:")))

maxl = data[0] #init max

for value in data:
    print (value)
    if value > maxl:
        maxl = value
        
#max=max(data)
print (value)
print ("max: ", maxl)
