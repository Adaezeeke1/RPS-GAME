# Rock, Paper, Scissors

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
player_choice = input(
    "Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")

# Cast player_choice to an integer
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# Generate computer_choice
computer_choice = random.choice("123")

# Cast computer_choice to an integer
computer = int(computer_choice)

print("")
print("You chose: " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("⛷️ Python wins!")

print("")
print(" Well done Players!")
