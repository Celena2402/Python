# Задача 2
#       Создайте программу для игры с конфетами человек против человека.
#        Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
#        ход друг после друга. Первый ход определяется жеребьёвкой. За один
#        ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
#         сделавшему последний ход. Тот кто взял последним - тот проиграл.Сколько конфет нужно взять первому игроку,
#         чтобы забрать все конфеты у своего конкурента?
#          a) Добавьте игру против бота
#          b) Подумайте как наделить бота "интеллектом"

import random


candies = int(
    input('Введите общее количество конфет, которые лежат на столе: '))
print(f'На столе лежит {candies} конфет(а).')

candies_step = int(
    input('Введите max количество конфет, которые можно взять за один ход: '))
print(f'За один ход можно взять не более чем {candies_step} конфет(ы).')

gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input(
    'Введите имя 2 игрока: ')

# Жеребьевка
gamer = random.choice([gamer_1, gamer_2])
print(f'По жеребьевке первым ходит игрок {gamer}')

if gamer == gamer_1:
    current_gamer = gamer_1
    while candies > 0:
        print('Количество оставшихся конфет: {}'.format(candies))
        while True:
            number_to_delete = int(
                input('Ход игрока {}: '.format(current_gamer)))
            if number_to_delete >= 1 and number_to_delete <= candies_step:
                break
            else:
                print(
                    f'Вы взяли количество конфет меньше 1 шт или больше {candies_step} шт')
        candies = candies-number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

    print('УРА!!! Победил(а) {}'.format(current_gamer))

else:
    current_gamer = gamer_2
    while candies > 0:
        print('Количество оставшихся конфет: {}'.format(candies))
        while True:
            number_to_delete = int(
                input('Ход игрока {} : '.format(current_gamer)))
            if number_to_delete >= 1 and number_to_delete <= candies_step:
                break
            else:
                print(
                    f'ОШИБКА!!! Вы взяли количество конфет меньше 1 шт или больше {candies_step} шт')
        candies = candies-number_to_delete
        current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2

    print('УРА!!! Победил(а) {}'.format(current_gamer))
