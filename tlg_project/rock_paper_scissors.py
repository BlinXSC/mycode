#!/usr/bin/env python3
"""
Rock Paper Scissors game :)
"""
from textwrap import dedent
import random

def rock_paper_scissors_game():
    """Function that runs the game"""

    # Briefs the player on the rock paper scissors game.
    print(dedent("""
    ===============================INSTRUCTIONS======================================
    Welcome to a game of Rock, Paper, Scissors... Lizard, Spock. This is a modified
    version of Rock Paper Scissors as played on the TV Show "The Big Bang Theory".
    The computer and player will enter their choice. Here are the rules that decide 
    the winner:

        - Rock crushes lizard and scissors
        - Paper covers rock, and disproves Spock
        - Scissors cuts paper, and decapitates lizard
        - Spock smashes scissors, and vaporizes rock
        - Lizard eats paper, and poisons Spock
    
    The game ends when the player or computer score three points.
        """))

    # Initializes the score
    player_score = 0
    computer_score = 0

    # Loop runs until player or computer scores three points.
    while (player_score < 3 and computer_score < 3):

        # Computer has three options to pick from
        options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

        # Computer's choice
        computer_choice = random.choice(options)
        # print(computer_choice) #For debug purposes, keep this line inactive

        # User picks
        user_choice = input('Enter your choice (rock, paper, scissors, lizard, Spock) >>> ').lower()

        # Ensures user choices the appropriate option
        while user_choice not in options:
            print('You did not choose rock, paper, or scissors...\n')
            user_choice = input('Re-enter choice (rock, paper, scissors, lizard, Spock) >>> ').lower()

        print(f"Player selects {user_choice}, computer selects {computer_choice}")

        # See introduction for rules.
        victories = {
            "rock":["scissors", "lizard"],
            "paper":["rock", "spock"],
            "scissors":["paper", "lizard"],
            "lizard":["paper, spock"],
            "spock":["rock", "scissors"]
        }

        # Compare choices
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif computer_choice in victories[user_choice]:
            print("You win this round.\n")
            player_score += 1
        else:
            print("Sorry... computer wins...\n")
            computer_score += 1

        # Print score between player and computer
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}\n")

    # Provides player the results of this match.
    if player_score > computer_score:
        print("You win!!!")
    else:
        print("Better luck next time...")

    # Insults the player if they did not win one round in the entire match.
    if player_score == 0:
        print("Perhaps you should call it a day... your luck isn't so good at the moment.")

    print("\nReturning to Game Box...")

def main():
    """Main program"""
    rock_paper_scissors()

# Calls main function
if __name__ == "__main__":
    main()
