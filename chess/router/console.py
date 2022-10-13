from controllers.PlayerController import PlayerController
from controllers.TournamentController import TournamentController
from controllers.MenuController import MenuController

class Console:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def routing(menu_input:int):
        if menu_input == 1:
            player_id = int(input('Enter a player\'s ID: '))
            PlayerController.show(player_id)

        if menu_input == 3:
            PlayerController.index()

        if menu_input == 5:
            TournamentController.create()

        if menu_input == 6:
            MenuController.exit()
