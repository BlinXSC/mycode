#!/usr/bin/env python3
"""
Rock Paper Scissors game :)
"""

import random

def rock_paper_scissors():
    """Function that runs the game"""

    # Briefs the player on the rock paper scissors game.
    print("Welcome to a game of rock paper scissors. The computer will make a choice,")
    print("then the player will enter their choice. Rock beats scissors, scissors beats paper,")
    print("and paper beats rock. The game ends when the player or computer score three points. \n")

    # Initializes the score
    player_score = 0
    computer_score = 0

    # Loop runs until player or computer scores three points.
    while (player_score < 3 and computer_score < 3):

        # Computer has three options to pick from
        options = ['rock', 'paper', 'scissors']

        # Computer's choice
        computer_choice = random.choice(options)
        # print(computer_choice) #For debug purposes, keep this line inactive

        # User picks
        user_choice = input('Enter your choice (rock, paper, scissors) >>> ').lower()

        # Ensures user choices the appropriate option
        while user_choice not in options:
            print('You did not choose rock, paper, or scissors...')
            user_choice = input('Enter your choice (rock, paper, scissors) >>> ').lower()

        print(f"Player selects {user_choice}, computer selects {computer_choice}")

        victories = {
            "rock":"scissors",  # Rock beats scissors
            "paper":"rock",  # Paper beats rock
            "scissors":"paper"  # Scissors beats paper
        }

        # Compare choices
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif computer_choice == victories[user_choice]:
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

    # Insults the player if they did not win one round in the entire match.abs
    print("Perhaps you should call it a day... your luck isn't so good at the moment.")

def main():
    """Main program"""
    rock_paper_scissors()

# Calls main function
if __name__ == "__main__":
    main()
