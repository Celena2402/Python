# 5. Реализуйте алгоритм перемешивания списка.

import random

list= [45, 20, 4, 92, 10, 5, 79, 39, 63, 67, 2]
print('Исходный список: ', list)

# 1.
random.shuffle(list)
print('Новый список: ', list)

# 2. 
new_list = list
for i in range(len(new_list)):
    k = random.randint(0, len(new_list)-1)
    temp = new_list[i]
    new_list[i] = new_list[k]
    new_list[k] = temp
print('Новый список: ', new_list)
