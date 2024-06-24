from game.rps import RPS
from utils.input_handler import get_valid_input


class Player:
    def get_choice(self):
        valid_choices = list(map(RPS, range(1, 4)))
        user_choice = get_valid_input(
            "\nEnter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n",
            valid_choices, RPS)
        return user_choice
