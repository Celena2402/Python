# 1. Задайте список. Напишите программ, которая определит
# присутствует ли в заданном списке строк некое число
#

# 1
#lst = ["1" , "2", "2zxc", "dgdf", "23zxcjfj"]
#N=input("Введите число: ")

# for item in lst:
#    if N in item:
#        print(f'Число {N} найдено в списке, в строке {item}')
#        break


# 2.
ls = ["r423", "344", "2rer", "wdfwdf"]
print(ls)

num = input("Введите число: ")
for i in ls:
    if str(num) in i:
        print("yes")
        break
else:
    print("no num")
