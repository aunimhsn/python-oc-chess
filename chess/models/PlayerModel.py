from tinydb import TinyDB, Query


class PlayerModel:
    # https://stackoverflow.com/questions/24988162/define-functions-with-too-many-arguments-to-abide-by-pep8-standard
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_players():
        db = TinyDB('db/db.json')
        return db.table('players').all()

    @staticmethod
    def get_player_by_id(id:int):
        db = TinyDB('db/db.json')
        return db.table('players')[id - 1]
        



