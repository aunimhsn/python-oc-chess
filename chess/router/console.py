from controllers.PlayerController import PlayerController

class Console:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def routing(menu_input:int):
        if menu_input == 1:
            player_id = int(input('Entrer l\'id du joueur à consulter : '))
            PlayerController.show(player_id)

        if menu_input == 3:
            PlayerController.index()
