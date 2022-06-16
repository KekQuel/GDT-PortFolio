# The very beginning of my programming projects.
# My first time learning Random lib which is EXTREMELY IMPORTANT for games made to be replayed!
import random

rps = ["Rock", "Paper", "Scissors"]  # List of states

i = 0

while i < 1:  # Check for win/lose

    x = random.randint(0, 2)  # Opponent randomly chooses either of these states

    player = input("Rock, Paper or Scissors? ")  # Pretty self-explanatory

    print(rps[x])

    if "Rock" != player and "Paper" != player and "Scissors" != player:
        print("Invalid")

#  Every possibility shown.
    if x == 0:  # Rock
        if player == "Rock":
            print("Tie, try again.")
        if player == "Scissors":
            print("Lmao skill issue")
            i = 1
        if player == "Paper":
            i = 1
            print("Noice you won")
            break

    elif x == 2:  # Scissors
        if player == "Paper":
            print("Lmao skill issue")
            i = 1
        if player == "Scissors":
            print("Tie, try again.")
        if player == "Rock":
            print("Noice you won.")
            i = 1
            break

    elif x == 1:  # Paper
        if player == "Rock":
            print("Lmao skill issue.")
            i = 1
        if player == "Paper":
            print("Tie, try again")
        if player == "Scissors":
            print("Noice you won")
            i = 1
            break
