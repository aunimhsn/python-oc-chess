from typing import Dict, List
from models.PlayerModel import PlayerModel
from views.PlayerView import PlayerView


class PlayerController:

    def __init__(self):
        pass

    @staticmethod
    def index() -> None:
        # 1 étape récupérer la liste de tous les joueurs
        # players list[Document]
        players =  PlayerModel.get_players()
        PlayerView().list_players(players)

    @staticmethod
    def show(id:int) -> None:
        player =  PlayerModel.get_player_by_id(id)
        PlayerView().show_player(player)

    @staticmethod
    def create(data) -> None:
        PlayerModel.set_players(data)


