from game.rps import RPS
from utils.input_handler import get_valid_input


class Player:
    def get_choice(self):
        choice = get_valid_input(
            "\nEnter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n", range(1, 4), RPS)
        return choice
