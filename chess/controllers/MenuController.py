from views.MenuView import MenuView
import sys
from db.seeders.DatabaseSeeder import DatabaseSeeder


class MenuController:

    def __init__(self):
        pass

    def menu(self):
        MenuView().show_menu()
        return int(input())

    def exit(self):
        DatabaseSeeder().clear()
        sys.exit()