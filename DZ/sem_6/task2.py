# Задача 2
#       Дана последовательность чисел. Получить список уникальных элементов заданной 
#       последовательности, список повторяемых и убрать дубликаты из заданной 
#       последовательности.
#       Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10]
print(lst)

data=[x for x in lst]
new_lst=list(filter(lambda x: lst.count(x)<2, data))
print(new_lst)

data_1=[x for x in set(lst)]
new_lst1=list(filter(lambda x: lst.count(x)>1, data_1))
print(new_lst1)

new_lst2=[]
new_lst2=list(filter(lambda x: x not in new_lst2, data_1))
print(new_lst2)

# ************
# 2.

# for i in lst:
#     if lst.count(i)<2:
#         new_lst.append(i)
# print(new_lst)

#  
# new_lst1 = [x for x in set(lst) if lst.count(x) > 1]
# # 2.
# # new_lst1={}
# # for i in lst:
# #     if lst.count(i)>1:
# #         new_lst1.append(i)
# print(new_lst1)

# new_lst2=[]
# for i in lst:
#     if i not in new_lst2:
#         new_lst2.append(i)
# print(new_lst2)