# 5.     Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#     Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты первой точки А')
xa=int(input('x= '))
ya=int(input('y= '))

print('Введите координаты второй точки B')
xb=int(input('x= '))
yb=int(input('y= '))

import math
result=round(math.sqrt((xb-xa)**2+(yb-ya)**2),2)
print(f"Расстояние между точками А({xa},{xb}) и B({xb},{yb}) равно {result}")
