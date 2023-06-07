#!/usr/bin/env python3
""" Alan Alegre | Final Project: Simple Game Box """

# Imports three different games
from textwrap import dedent
import high_low
import rock_paper_scissors
import trivia_api

def main():
    """ Runs the Game Box"""

    selection = -1

    print(dedent("""\
    Welcome to my final project. This is a simple program that allows you to
    select from three games. This is a fairly composite program tying together 
    a lot of the concepts learned of the past two weeks. Please enjoy!!!
    """))

    while selection != 0:

        selection = -1

        while selection not in [0, 1, 2, 3]:
            try:
                selection = int(input(dedent("""\
                    Please select from the following games:

                    1. High Low (Guess if the next card drawn will be higher or lower)
                    2. Rock Paper Scissors ... Lizard Spock (Variation of Rock Paper Scissors)
                    3. Trivia (General Knowledge)
                    0. Exit the program

                    Selection >>> """)))
            except ValueError:
                print("Invalid input, please try again.")

        if selection == 1:
            high_low.hi_low_game()
        elif selection == 2:
            rock_paper_scissors.rock_paper_scissors_game()
        elif selection == 3:
            trivia_api.trivia_game()

main()
