
import menu
import loggin
import UI


def start():
    while True:
        button=menu.menu()
        if button == 1:
            UI.add_view()
        elif button == 2:
            loggin.delete_data()
        elif button == 3:
            loggin.edit_data()
        elif button == 4:
            UI.save_view()
            loggin.save_data()
        elif button == 5:
            loggin.output_data()
        elif button == 0:
            print('Выход')
        else:
            print('введите цифру из меню')
            start()