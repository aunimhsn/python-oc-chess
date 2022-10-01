from tinydb import TinyDB, Query

from tinydb.table import Document


class PlayerModel:
    # https://stackoverflow.com/questions/24988162/define-functions-with-too-many-arguments-to-abide-by-pep8-standard
    def __init__(self, first_name:str, last_name:str, elo_points:int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.elo_points = elo_points

    @staticmethod
    def get_players() -> list[Document]:
        db = TinyDB('db/db.json')
        return db.table('players').all()

    @staticmethod
    def get_player_by_id(id:int) -> Document:
        db = TinyDB('db/db.json')
        return db.table('players').get(doc_id = id)
        



