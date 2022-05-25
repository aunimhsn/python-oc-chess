from tinydb import TinyDB


class TournamentSeeder:
    def __init__(self):
        pass

    def seed(self) -> None:
        # path from main.py file
        db = TinyDB('db/db.json')
        tournaments = db.table('tournaments')
        tournaments.insert({ 
            'name': 'Blitz Chess Arena', 
            'description': 'Come n\' prove them wrong about your chess skills!',
            'localisation': 'Online',
            'time_control': 360,
            'players': [
                {
                    'id': 1,
                    'firstname': 'John',
                    'lastname': 'Doe',
                    'elo_points': 1080
                },
                {
                    'id': 1,
                    'firstname': 'Jane',
                    'lastname': 'Doe',
                    'elo_points': 1014
                }
            ],
            'rounds': [
                {
                    'winner': {
                        'id': 1,
                        'firstname': 'John',
                        'lastname': 'Doe',
                        'elo_points': 1080
                    },
                    'looser': {
                        'id': 2,
                        'firstname': 'Jane',
                        'lastname': 'Doe',
                        'elo_points': 1014
                    }
                }
            ]
        })
    
    def clear(self) -> None:
        db = TinyDB('db/db.json')
        db.drop_table('tournaments')

