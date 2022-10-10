# Задача 2
#       Создайте программу для игры с конфетами человек против человека.
#        Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
#        ход друг после друга. Первый ход определяется жеребьёвкой. За один 
#        ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
#         сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
#         чтобы забрать все конфеты у своего конкурента?
#          a) Добавьте игру против бота
#          b) Подумайте как наделить бота "интеллектом"


count_of_sticks = int(input('введите количество палочек для игры: '))
gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
current_gamer = gamer_1
while count_of_sticks > 0:
    print('количество оставшихся палочек: {}'.format(count_of_sticks))
    while True:
        number_to_delete = int(input('ход игрока {} (1 - 3): '.format(current_gamer)))
        if number_to_delete >= 1 and number_to_delete <= 3:
            break
    count_of_sticks -= number_to_delete
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

print('Победил {}'.format(current_gamer))