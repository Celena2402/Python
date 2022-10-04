# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#      Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
#      в одной строке одно число.

#list = [45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3]


N = int(input('Введите N: '))
array = []
for i in range(-N, N + 1):
    array.append(i)
length_of_array = N * 2 + 1 
print('Список из N элементов, заполненных числами из промежутка [-N, N]:')
print(array)
print()

path = 'DZ/sem_2/file.txt'
input_files = open (path)
print('Список из файла file.txt: ')
for line in input_files.readlines():
    print(line.strip(), end=" ")
print()
leng=len(open("DZ/sem_2/file.txt").readlines())
#print('Количество строк в файле = ',len(open("DZ/sem_2/file.txt").readlines()))
print('Количество строк(элементов) в файле = ',leng)
print()

poz_1=int(input(f'Введите номер первой позиции (от 0 до {leng-1}): '))
poz_2=int(input(f'Введите номер второй позиции (от 0 до {leng-1}): '))
#with open(path) as f:
#    lines = f.readlines()
#    print(lines[poz_1])
#    print(lines[poz_2])
#    print(int(lines[poz_1])*int(lines[poz_2]))
#print()

if (poz_1 != poz_2):
    if (poz_1 < 20 and poz_2 < 20):
        with open(path) as f:
            lines = f.readlines()
            print('Элемент на позиции', poz_1, ' = ', lines[poz_1], end='')
            print('Элемент на позиции', poz_2, ' = ', lines[poz_2], end='')
            print('Произведение выбранных элементов равно: ', int(lines[poz_1])*int(lines[poz_2]))
    else:
        print('ОШИБКА! Вы ввели значение превышающее длину списка')
else:
    print('ОШИБКА! Вы ввели одинаковые номера позиции')

