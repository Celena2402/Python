# Задача 2
#       Создайте программу для игры с конфетами человек против человека.
#        Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
#        ход друг после друга. Первый ход определяется жеребьёвкой. За один 
#        ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
#         сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
#         чтобы забрать все конфеты у своего конкурента?
#          a) Добавьте игру против бота
#          b) Подумайте как наделить бота "интеллектом"

import random


candies=20
print(f'На столе лежит {candies} конфета.')
print('За один ход можно забрать не более чем 28 конфет.')
gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input('Введите имя 2 игрока: ')
#current_gamer = gamer_1

# Жеребьевка
gamer=random.choice([gamer_1,gamer_2])
print(f'По жеребьевке первым ходит игрок {gamer}')

# if gamer==gamer_1:
#     gamer_all=gamer_1
# else:
#     gamer_all=gamer_2


while candies > 0:
    print('Количество оставшихся конфет: {}'.format(candies))
    while True:
        number_to_delete = int(input('Ход игрока {} (1 - 28): '.format(gamer_12)))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
        else:
            print('Вы взяли количество конфет меньше 1 шт или больше 28 шт')

    #candies -= number_to_delete
    candies=candies-number_to_delete
    gamer_12 = gamer_2 if gamer_1 == gamer_1 else gamer_1

print('УРА!!! Победил(а) {}'.format(gamer_12))


