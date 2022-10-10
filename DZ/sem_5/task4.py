# Задача 4.
#       Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#       Входные и выходные данные хранятся в отдельных текстовых файлах.

from email import message
from re import I


fail = 'DZ/sem_5/task4_message.txt'
fail_encoded = 'DZ/sem_5/task4_encoded.txt'
fail_decoded = 'DZ/sem_5/task4_decoded.txt'

with open(fail, 'r', encoding='utf-8') as original_message:
    message_line = original_message.readlines()
    for line in message_line:
        message = line.strip()
        print(f'Исходный файл:  {message}')


# Сжатие

        with open(fail_encoded, 'w', encoding='utf-8') as message_encoded:
            encoded_str = ''
            i = 0
            while i < len(message):
                k = 1
                while i+1 < len(message) and message[i] == message[i+1]:
                    if (message[i] == message[i+1]):
                        k = k+1
                        i = i+1
                    else:
                        break
                encoded_str = encoded_str+str(k)+message[i]
                i = i+1
            print(f'Сжатый файл:  {encoded_str}')
            for i in range(len(encoded_str)):
                message_encoded.write(f'{encoded_str[i]}')
            message_encoded.write('\n')
        message_encoded.close()
original_message.close()

# Восстановление

with open(fail_encoded, 'r', encoding='utf-8') as message_enc:
    message_line = message_enc.readlines()
    for line in message_line:
        message_dec = line.strip()
        #print(f'Исходный файл:  {message_dec}')
        with open(fail_decoded, 'w', encoding='utf-8') as message_decoded:
            decoded_str = ''
            k = ''
            for i in message_dec:
                if i.isdigit():
                    k = k+i
                else:
                    decoded_str = decoded_str+i*int(k)
                    k = ''
            print(f'Востановленный файл:  {decoded_str}')

            for i in range(len(decoded_str)):
                message_decoded.write(f'{decoded_str[i]}')
            message_decoded.write('\n')
    message_decoded.close()
message_enc.close()
