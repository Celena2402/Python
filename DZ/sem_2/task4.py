# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#      Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
#      в одной строке одно число.

#list = [45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3]
#list = open('file.txt', 'r')
#with open('file.txt') as list:
#    for line in list:
#        print(line)
list=open("file.txt", "r")
while True:
    line=list.readline()
    if not line:
        break
    print(line.strip())

list.close

#print('Количество позиций в списке', len(list))

poz_1=int(input(f'Введите номер первой позиции (от 0 до {len(list)-1}): '))
poz_2=int(input(f'Введите номер второй позиции (от 0 до {len(list)-1}): '))

#if (poz_1 != poz_2):
#    if (poz_1 < len(list) and poz_2 < len(list)):
#        print('Позиция на месте', poz_1, ' = ', list[poz_1])
#        print('Позиция на месте', poz_2, ' = ', list[poz_2])
#        print('Произведение выбранных позиций равно: ', list[poz_1]*list[poz_2])
#    else:
#        print('ОШИБКА! Вы ввели значение превышающее длину списка')
#else:
#    print('ОШИБКА! Вы ввели одинаковые номера позиции')

