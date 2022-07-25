from views.MenuView import MenuView


class MenuController:

    def __init__(self):
        pass

    def menu(self):
        MenuView().show_menu()
        return int(input())