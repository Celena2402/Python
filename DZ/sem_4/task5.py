# Задача 5. 
#       Даны два файла, в каждом из которых находится запись многочлена. 
#       Задача - сформировать файл, содержащий сумму многочленов.


from fileinput import close
#import pandas

fail1 = 'DZ/sem_4/task5_fail_1.txt'
fail2 = 'DZ/sem_4/task5_fail_2.txt'

def ReadFile(fail):
    with open (str(fail),'r') as data:
        polynomial=data.read()
    return polynomial




print('Первый многочлен из file_1.txt: ')
polynomial1=ReadFile(fail1)
print(polynomial1)

print('Второй многочлен из file_2.txt: ')
polynomial2=ReadFile(fail2)
print(polynomial2)

# polynomial1_grp=polynomial1.groupby('+')
# polynomial1.grp.first()

name = polynomial1[0].split(' ')
name.extend(polynomial1[:2])
print(name)

