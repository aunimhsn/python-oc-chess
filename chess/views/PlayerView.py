from models.PlayerModel import PlayerModel


class PlayerView:
    def __init__(self):
        pass

    def show_players(self, players) -> None:
        for player in players:
            print(f"Prénom : {player['first_name']}")
            print(f"nom : {player['last_name']}")
            print(f"nom : {player['elo_points']}")
