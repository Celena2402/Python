# Задача 4.
#       Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
#       Входные и выходные данные хранятся в отдельных текстовых файлах.

from re import I


# def encode(message, len):
#     encoded_str=""
#     i=0
#     while i<len(message):
#         k=1
#         #ch=message[i]
#         #j=i
#         while i+1<len(message) and message[i]==message[i+1]:
#             #if (message[j]==message[j+1]):
#             k=k+1
#             i=i+1
            
#         encoded_str=encoded_str+str(k)+message[i]
#         i=i+1
#     return encoded_str



fail = 'DZ/sem_5/task4_message.txt'
print('Сообщение из файла: ')
message = open(fail, 'r')
for line in message:
   print(line)
message.close()

leng=len(open("DZ/sem_5/task4_message.txt").readlines())
print(leng)

# encoded_str=""
# i=0
# while i<leng:
#     k=1
#         #ch=message[i]
#         #j=i
#     while i+1<len(message) and message[i]==message[i+1]:
#             #if (message[j]==message[j+1]):
#         k=k+1
#         i=i+1
            
#     encoded_str=encoded_str+str(k)+message[i]
#     i=i+1
#     #return encoded_str
# # encoded_message=encode(message_str,leng)
# print(encoded_str)