import random
from game.rps import RPS


class Computer:
    def get_choice(self):
        user_choice = RPS(random.choice(list(RPS)))
        return user_choice
