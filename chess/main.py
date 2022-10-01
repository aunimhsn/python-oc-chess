from router.Console import Console
from controllers.MenuController import MenuController
from db.seeders.DatabaseSeeder import DatabaseSeeder

def main():
    DatabaseSeeder().seed()
  
    while True:
        Console.routing(MenuController().menu())

    

    

main()