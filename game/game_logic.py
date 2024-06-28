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
        elif (player == RPS.ROCK and computer == RPS.SCISSORS) or \
             (player == RPS.PAPER and computer == RPS.ROCK) or \
             (player == RPS.SCISSORS and computer == RPS.PAPER):
            self.score["player"] += 1
        else:
            self.score["computer"] += 1

    def display_choices(self, player, computer):
        print(f"\nYou chose: {player.name}.")
        print(f"Python chose: {computer.name}.\n")

    def display_score(self):
        print("Scoreboard:")
        print(f"You: {self.score['player']}")
        print(f"Python: {self.score['computer']}")

    def play_again(self):
        return get_valid_input("\nPlay again? \n\nY for Yes, \nN to Exit\n\n", ['y', 'n']) == 'y'

    def play_round(self):
        player_choice = self.player.get_choice()
        computer_choice = self.computer.get_choice()
        self.display_choices(player_choice, computer_choice)
        self.determine_winner(player_choice, computer_choice)

    def final_winner_message(self):
        if self.score["player"] > self.score["computer"]:
            return "\n🏆 Congrats! You smashed it!"
        elif self.score["player"] < self.score["computer"]:
            return "\n🤖 oof... Better luck next time!"
        else:
            return "\n🤝 A tie! Good game!"

    def play(self):
        print("Welcome to Rock, Paper, Scissors!")
        while True:
            self.score = {"player": 0, "computer": 0, "ties": 0}
            for round in range(3):
                print(f"\nRound {round + 1} of 3:")
                self.play_round()
                self.display_score()
            print(self.final_winner_message())
            if not self.play_again():
                print("\nThanks for playing!")
                sys.exit("Bye!")
