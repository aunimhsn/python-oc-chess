from router.Console import Console
from controllers.MenuController import MenuController
from db.seeders.DatabaseSeeder import DatabaseSeeder

def main():
    DatabaseSeeder().seed()    
    Console.routing(MenuController().menu())

    DatabaseSeeder().clear()

main()