#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

# Import random module
import random

def main():
    
    # Picks a number from 1 - 100
    num = random.randint(1, 100)

    # Initialize variables
    rounds = 0
    guess = 0

    # While loop continues the game as long as the round remains below five.
    while (rounds < 5 and guess != num):
        
        print(f"Round {rounds + 1}")
        guess = input("Guess a number between 1 and 100\n> ")
        
        # Ensures the user provides an integer
        while guess.isdigit() == False:
            print("Please provide an integer between 1 and 100.")
            guess = input("Guess a number between 1 and 100\n> ")

        # Converts string to integer
        guess = int(guess)

        # Checks if the number is high, low, or correct
        if guess > num:
            print("Too high!")
            rounds = rounds + 1 
        elif guess < num:
            print("Too low!")
            rounds = rounds + 1
        else:
            print("Correct!")

main()