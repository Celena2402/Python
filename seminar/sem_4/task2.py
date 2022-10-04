# 2. Найдите корни квадратного уравнения Ач^2+Bx+C=0 двумя способамиЖ 
# с помощью математических формул нахождения корней квадратного уравнения 
# с помощью дополнительных библиотек Python

import math

print("Ax^2 + Bx +C = 0")
a=float(input('Введите А:'))
b=float(input('Введите B:'))
c=float(input('Введите C:'))

discr=b**2-4*a*c
print("Дискриминант D = %.2f" % discr)

if discr>0:
    x1=(-b+math.sqrt(discr))/(2*a)
    x2=(-b-math.sqrt(discr))/(2*a)
    print("x1=%.2f \nx2=%.2f" % (x1,x2))
elif discr==0:
    x=-b/(2*a)
    print("x=%.2f" % x)
else:
    print("Корней нет")

# 2.
#import sympy

#x=sympy.Symbol("x")
#print(sympy.solveset(1*x**2-2*x-3, x))