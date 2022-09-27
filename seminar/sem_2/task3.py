# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# 1.
str_1=input('str_1: ')
str_2=input('str_2: ')
print(str_1.count(str_2))

# 2.
inkrement=0
for i in range(len(str_1)):
    if str_2 in str_1[i: i+ len(str_2)]:
        inkrement+=1

print(inkrement)