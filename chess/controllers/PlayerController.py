from models.PlayerModel import PlayerModel
from views.PlayerView import PlayerView


class PlayerController:

    def __init__(self):
        pass

    @staticmethod
    def index() -> None:
        players =  PlayerModel.get_players()
        PlayerView().list_players(players)

    @staticmethod
    def show(id:int) -> None:
        player =  PlayerModel.get_player_by_id(id)
        PlayerView().show_player(player)


