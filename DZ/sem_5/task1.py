# Задача 1.
#       Напишите программу, удаляющую из текста все слова, содержащие "абв".



line = 'автобус абв дубина выбойка книга тетрадь забота взбивка слово вербена арка'

print(line)

print(" ".join([x for x in line.split() if not x.startswith(("а","б","в"))]))






