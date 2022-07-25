from tinydb.table import Document


class PlayerView:
    def __init__(self):
        pass

    def list_players(self, players:list[Document]) -> None:
        for player in players:
            print(f"ID : { player['id'] }")
            print(f"Prénom : { player['first_name'] }")
            print(f"Nom : { player['last_name'] }")
            print(f"Points d'Elo : { player['elo_points'] }")

    def show_player(self, player:Document) -> None:
        print(f"ID : { player['id'] }")
        print(f"Prénom : { player['first_name'] }")
        print(f"Nom : { player['last_name'] }")
        print(f"Points d'Elo : { player['elo_points'] }")
