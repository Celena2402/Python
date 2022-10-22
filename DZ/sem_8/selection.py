import menu
import UI


def start():
    while True:
        button=menu.menu()
        if button == 1:
            UI.add_view()
        elif button == 2:
            UI.save_view()
        elif button == 3:
            UI.output_view()              
        elif button == 0:
            print('Выход')
            exit()
        else:
            print('введите цифру из меню')
            start()