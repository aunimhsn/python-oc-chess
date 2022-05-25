from controllers.MenuController import MenuController
from controllers.PlayerController import PlayerController
from db.seeders.DatabaseSeeder import DatabaseSeeder

def main():
    DatabaseSeeder().seed()
    MenuController().menu()

    # Testing controller...
    PlayerController().players()


    DatabaseSeeder().clear()

main()