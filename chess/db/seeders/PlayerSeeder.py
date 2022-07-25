from tinydb import TinyDB


class PlayerSeeder:
    def __init__(self):
        pass

    def seed(self) -> None:
        # path from main.py file
        db = TinyDB('db/db.json')
        players = db.table('players')
        players.insert({ 'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'elo_points': 1016 })
        players.insert({ 'id': 2, 'first_name': 'Jane', 'last_name': 'Doe', 'elo_points': 894 })

    def clear(self) -> None:
        db = TinyDB('db/db.json')
        db.drop_table('players')