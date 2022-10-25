# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import queue
import pygame
import sys

# проверка на победу


def check_win(mas, sign):
    zerows = 0
    for row in mas:
        zerows += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
        # if mas[col][0]==sign and mas[col][1]==sign and mas[col][2]==sign:
        #     return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zerows == 0:
        return 'Ничья'
    return False


# строим окно
pygame.init()
size_block = 100   # размер блока
margin = 5          # размер отступа
width = heigth = size_block*3+margin*4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

# цвета
# black=(0,0,0)
# red=(255,0,0)
# green=(0,255,0)
# white=(255,255,255)
black = (150, 126, 126)
red = (207, 97, 128)
green = (180, 153, 189)
white = (232, 211, 211)
# массив заполнен 0 и означает что ветка сейчас пустая
mas = [[0]*3 for i in range(3)]
query = 0    # переменная чтоы цвета чередовались  1 2 3 4 5 6
game_over = False  # чтобы программа в конце не зависала и выходила


# цикл обработки событий
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
# ставим Х или 0
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # узнвем номер колонки по которой кликнули
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            # проверяемм на четное и не четное, кто ходит
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'  # в массив заносим значение х
                else:
                    mas[row][col] = 'o'
                query += 1
        # чтобы игра запускалась заново при нажании пробела
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query = 0
            screen.fill(black)

    if not game_over:
        
        # ложный цикл по стокам и столбцам

        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red      # крестики рисуются на красном фоне
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white    # остальные поля пока белые
            # координаты верхнего левого угла квадрата
                x = col*size_block+(col+1)*margin
                y = row*size_block+(row+1)*margin
                # координаты правого нижнего угла
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            # рисуем на поле х
                if color == red:   # рисуем крестик по координатам
                    pygame.draw.line(screen, white, (x+30, y+30),
                                     (x+size_block-30, y+size_block-30), 6)
                    pygame.draw.line(
                        screen, white, (x+size_block-30, y+30), (x+30, y+size_block-30), 6)
                elif color == green:  # рисуем 0
                    pygame.draw.circle(
                        screen, white, (x+size_block//2, y+size_block//2), size_block//2-25, 5)

        if (query-1) % 2 == 0:  # четные это х
            game_over = check_win(mas, 'x')
        else:
            game_over = check_win(mas, '0')

        if game_over:
            # закрашиваем наш экран полностью черным цветом
            screen.fill(black)
            font = pygame.font.SysFont('couriernew', 80)     # создаем шрифт
            # текст окрашивает параметр game_over в белый цвет
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()                      # узнаем координаты текста
            # 2 точки находим центр нашего экрана
            text_x = screen.get_width()/2-text_rect.width/2
            text_y = screen.get_height()/2-text_rect.height/2     # чтобы текст был в середине
            # прикрепляет наш текст по найденым координатам
            screen.blit(text1, [text_x, text_y])

        pygame.display.update()
