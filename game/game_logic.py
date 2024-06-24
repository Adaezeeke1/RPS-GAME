import sys
from game.rps import RPS
from game.player import Player
from game.computer import Computer
from utils.input_handler import get_valid_input


class RockPaperScissorsGame:
    def __init__(self):
        self.score = {"player": 0, "computer": 0, "ties": 0}
        self.player = Player()
        self.computer = Computer()

    def determine_winner(self, player, computer):
        if player == computer:
            self.score["ties"] += 1
            return "😲 It's a tie!"
        elif (player == RPS.ROCK and computer == RPS.SCISSORS) or \
             (player == RPS.PAPER and computer == RPS.ROCK) or \
             (player == RPS.SCISSORS and computer == RPS.PAPER):
            self.score["player"] += 1
            return "🎉 You win!"
        else:
            self.score["computer"] += 1
            return "⛷️ Python wins!"

    def display_choices(self, player, computer):
        print(f"\nYou chose: {player.name}.")
        print(f"Python chose: {computer.name}.\n")

    def display_score(self):
        print("\nScoreboard:")
        print(f"You: {self.score['player']}")
        print(f"Python: {self.score['computer']}")
        print(f"Ties: {self.score['ties']}\n")

    def play_again(self):
        return get_valid_input("\nPlay again? \n\nY for Yes, \nN to Exit\n\n", ['y', 'n']).lower() == 'y'

    def play(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            player_choice = self.player.get_choice()
            computer_choice = self.computer.get_choice()
            self.display_choices(player_choice, computer_choice)
            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            self.display_score()
            if not self.play_again():
                print("\nThanks for playing!")
                sys.exit("Bye!")
