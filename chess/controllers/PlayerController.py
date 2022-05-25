from models.PlayerModel import PlayerModel
from views.PlayerView import PlayerView


class PlayerController:

    def __init__(self):
        pass

    def players(self) -> None:
        players =  PlayerModel.get_players()
        PlayerView().show_players(players)



