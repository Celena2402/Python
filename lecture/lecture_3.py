# ФУНКЦИИ С ОДНОЙ ПЕРЕМЕННОЙ

#  def f(x):
#     x**2

# g=f
# print(type(f))
# print(f(1))
# print(g(1))


# def f(x):
#     return x**2

# g=f
# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))


# def calc1(x):
#     return x+10

#print(calc1(10))

# def calc2(x):
#     return x*10

#print(calc2(10))

# def math(op,x):
#     print(op(x))

# math(calc2,10)
# math(calc1,10)




# ФУНКЦИИ С ДВУМЯ ПЕРЕМЕННами
#def sum(x,y):
#    return x+y

#f=sum
#f=lambda q,w:q+w
#sum=lambda x,y:x+y

# def mylt(x,y):
#     return x*y

# def calc(op,a,b):
#     print(op(a,b))
#     #return op(a,b)

# #calc(mylt,4,5)
# #calc(f,4,5)
# calc(lambda x,y:x+y,4,5)



#*********************
# <list comprehension>

# list=[]

# for i in range(1,101):
#     if(i%2==0):
#         list.append(i)

# print(list)

# # проще
# list=[i for i in range(1,21) if i%2==0]
# # подключаем картежи
# list=[(i,i) for i in range(1,21) if i%2==0]

# def f(x):
#     return x**3

# list=[f( i) for i in range(1,21) if i%2==0]
# # подключаем картежи
# list=[(i,f(i)) for i in range(1,21) if i%2==0]
# print(list)

# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# path='/'
# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)
# ----------------
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res=select(int,data)
# res=where(lambda x: not x%2,res)
# res=select(lambda x: (x,x**2), res)
# print(res)
# #data = select(int, data)
# #data = where(lambda e: not e % 2, data)
# #data = list(select(lambda e: (e, e**2), data))

# Функция map
# 1.
# li=[x for x in range(1,20)]

# li=list(map(lambda x:x+10, li))

# print(li)

# 2. ввод с клавиатуры
# data=list(map(int, input().split()))
# print(data)

# 3. вывод в столбцы
# data=list(map(int, input().split()))

# for e in data:
#     print(e)

# если записать данные в list то они там будут храниться,
# просто операция map не перезапишет второй раз

# data=map(int, '1 2 3 4 555 6'.split())

# for e in data:
#     print(e)

# исправим предыдущую задачу с функцией map

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res=map(int,data)
# res=where(lambda x: not x%2,res)
# res=list(map(lambda x: (x,x**2), res))
# print(res)
#data = select(int, data)
#data = where(lambda e: not e % 2, data)
#data = list(select(lambda e: (e, e**2), data))

#-------------------
# Функция FILTER
# фунцию where можно заменить filter

# data=[x for x in range(10)]

# res=list(filter(lambda x: not x%2==0, data))
# print(res)

# исправим предыдущую задачу с функцией map и filter

# data = '1 2 3 5 8 15 23 38'.split()

# res=map(int,data)
# res=filter(lambda x: not x%2,res)
# res1=list(map(lambda x: (x,x**2), res))
# print(res)
# print(res1)

#-------------------
# Функция ZIP

# users=['user1','user2','user3','user4','user5']
# ids=[4,5,9,14,7]
# salaty=[111,222,333]

# data=list(zip(users,ids,salaty))
# print(data)

# #-------------------
# # Функция ENUMERATE

# data=list(enumerate(users))
# print(data)