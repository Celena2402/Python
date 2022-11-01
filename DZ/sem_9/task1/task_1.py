# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP


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
width = heigth = size_block*3 + margin*4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

color_background = (150, 126, 126)
color_x = (207, 97, 128)
color_o = (180, 153, 189)
color_font = (232, 211, 211)

mas = [[0]*3 for i in range(3)]
query = 0    # переменная цвета
game_over = False


# цикл обработки событий
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
# ставим Х или 0
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # узнаем номер колонки по которой кликнули
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)

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
            screen.fill(color_background)

    if not game_over:

        # цвет фона, на которм рисуем х или 0

        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = color_x
                elif mas[row][col] == 'o':
                    color = color_o
                else:
                    color = color_font
            # координаты
                x = col*size_block+(col+1)*margin
                y = row*size_block+(row+1)*margin

                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            # рисуем на поле х
                if color == color_x:
                    pygame.draw.line(screen, color_font, (x+30, y+30),
                                     (x+size_block-30, y+size_block-30), 6)
                    pygame.draw.line(
                        screen, color_font, (x+size_block-30, y+30), (x+30, y+size_block-30), 6)
                elif color == color_o:  # рисуем 0
                    pygame.draw.circle(
                        screen, color_font, (x+size_block//2, y+size_block//2), size_block//2-25, 5)

        if (query-1) % 2 == 0:
            game_over = check_win(mas, 'x')
        else:
            game_over = check_win(mas, 'o')

        if game_over:
            # вывод текста
            screen.fill(color_background)
            f1 = pygame.font.SysFont('couriernew', 20)
            text_f1 = f1.render('Чтобы продолжить нажмите', True, color_font)
            text_f2 = f1.render('пробел', True, color_font)

            font1 = pygame.font.SysFont('couriernew', 60)
            text2 = font1.render('ПОБЕДИЛ', True, color_font)

            font = pygame.font.SysFont('couriernew', 80)
            text1 = font.render(game_over, True, color_font)
            text_rect = text1.get_rect()
            text_x = screen.get_width()/2-text_rect.width/2
            text_y = screen.get_height()/2-text_rect.height/2

            screen.blit(text2, [30, 70])
            screen.blit(text1, [text_x, text_y])
            screen.blit(text_f1, [15, 250])
            screen.blit(text_f2, [120, 285])

        pygame.display.update()
