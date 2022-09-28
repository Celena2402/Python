# *** Файлы ***

# запись данных в файл
#with open('file.txt', 'w') as data:
#    data.write('line 1\n')
#    data.write('line 2\n')

#colors = ['red', 'green', 'blue']
#data = open('file.txt', 'a') #a - записывается текст при каждом запске
#data = open('file.txt', 'w') # W - происходит презапись текста, старые удаляются и саписываются новые
#data.writelines(colors) # разделителей не будет
#data.write('\nLINE 12\n')
#data.write('LINE 13\n')
#data.close()

#exit() 

# чтение файла
#path = 'file.txt'
#data = open(path, 'r')
#for line in data:
#    print(line)
#data.close()

# *** ФУНКЦИИ ***

#def f(x):
#    return x**2

#import hello

#print(hello.f(1))

#def f(x):
#    if x == 1:
#        return 'Целое'
#    elif x == 2.3:
#        return 23
#    else:
#        return

#def concatenatio(*params):
#    res: str = ""
#    for item in params:
#        res += item
#    return res
#print(concatenatio('a', 's', 'd', 'w')) # asdw
#print(concatenatio('a', '1', 'd', '2')) # a1d2
#print(concatenatio(1, 2, 3, 4)) # TypeError: ..

# *** РЕКУРСИЯ ***
#def fib(n):
#    if n in [1, 2]:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)

#list = []
#for e in range(1, 10):
#  list.append(fib(e))
#print(list) # 1 1 2 3 5 8 13 21 34

# *** КОРТЕЖ *** – это неизменяемый “список”

#a=(3,4,5) # кортеж. кол-во элементов не может быть меньше 2-ч
#print(a)
#print(a[0])
#print(a[-1])

#t = tuple(['red', 'green', 'blue'])
#print(t[0]) # red
#print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
#print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
#for e in t:
#    print(e) # red green blue
#t[0] = 'black' # TypeError: 'tuple' object does not support
#item assignment


#t = tuple(['red', 'green', 'blue'])
#red, green, blue = t
#print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# *** СЛОВАРИ ***

# 1.
#dictionary = {}
#dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
#print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
#print(dictionary['left']) # ←
# типы ключей могут отличаться

# 2.
#print(dictionary['up']) # ↑
# типы ключей могут отличаться
#dictionary['left'] = '⇐'
#print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
#del dictionary['left'] # удаление элемента
#for item in dictionary: # for (k,v) in dictionary.items():
#    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# *** МНОЖЕСТВА ***

# 1.
#a = {1, 2, 3, 5, 8}
#b = {'2', '5', 8, 13, 21}
#print(type(a)) # set
#print(type(b)) # set

# 2.
#a = {1, 2, 3, 5, 8}
#b = set([2, 5, 8, 13, 21])
#c = set((2, 5, 8, 13, 21))
#print(type(a)) # set
#print(type(b)) # set
#print(type(c)) # set
#a = {1, 1, 1, 1, 1}
#print(a) # {1}

# 3.
#colors = {'red', 'green', 'blue'}
#print(colors) # {'red', 'green', 'blue'}
#colors.add('red')
#print(colors) # {'red', 'green', 'blue'}
#colors.add('gray')
#print(colors) # {'red', 'green', 'blue','gray'}
#colors.remove('red')
#print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
#colors.discard('red') # ok
#print(colors) # {'green', 'blue','gray'}
#colors.clear() # { }
#print(colors) # set()

# 4. 
#a = {1, 2, 3, 5, 8}
#b = {2, 5, 8, 13, 21}
#c = a.copy() # c = {1, 2, 3, 5, 8}
#u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
#i = a.intersection(b) # i = {8, 2, 5}
#dl = a.difference(b) # dl = {1, 3}
#dr = b.difference(a) # dr = {13, 21}
#q = a \
#    .union(b) \
#    .difference(a.intersection(b))
# {1, 21, 3, 13}

# 5. неизменяемое множество
#a = {1, 2, 3, 5, 8}
#b = frozenset(a)
#print(b) # frozenset({1, 2, 3, 5, 8})

# *** СПИСКИ ***

#list1=[1,2,3,4,5]
#list2=list1

#list1[0]=123
#list2[1]=333 
#print()
#for e in list1:
#    print(e)
#print()
#for e in list2:
#    print(e)

list1=[1,2,3,4,5]

#print(list1.pop()) # удвляет последний элемент в списке
#print(list1)
#print(list1.pop())
#print(list1)
#print(list1.pop())
#print(list1) 

print(list1.pop(3)) # удаление конкретного элемента
print(list1)

print(list1.insert(2, 11)) # добавляет на в2-ую позицию элемент 11
print(list1)

print(list1.append(11)) # добавляется 11 в конец списка
print(list1)