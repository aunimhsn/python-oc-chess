from .PlayerSeeder import PlayerSeeder
from .TournamentSeeder import TournamentSeeder


class DatabaseSeeder:
    def __init__(self):
        pass

    def seed(self):
        PlayerSeeder().seed()
        TournamentSeeder().seed()

    def clear(self):
        PlayerSeeder().clear()
        TournamentSeeder().clear()
