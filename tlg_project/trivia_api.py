#!/usr/bin/env python3
"""Alan Alegre | Final Project: Trivia Game"""

# Provides the appropriate
import html
import random
from textwrap import dedent
import requests

def trivia_modifier(url):
    """ Allows user to modify difficulty """

    # Creates a list with difficulties
    difficulty = ['easy', 'medium', 'hard']

    # Initializes confirmation variable
    confirmation = ''

    while confirmation != 'Y':

        # Initializes user choices
        user_difficulty = 'Blap'
        question_count = 0

        # Prompts the user to select the difficulty and ensures only the difficulties
        # in the difficulty list are accepted.
        while user_difficulty not in difficulty:
            user_difficulty = input(dedent(
                """
                Please select how challenging you want this trivia to be:

                Easy
                Medium
                Hard

                >>> """)).lower()

            if user_difficulty not in difficulty:
                print("\n***Invalid option, please select again***")

        # Ensures the user provides an integer greater than 5.
        while question_count < 5:
            try:
                question_count = int(input("\nHow many questions? >>> "))

                # Reminds user to enter five as the minimum amount of questions.
                if question_count < 5:
                    print("\nFive questions is the minimum required to start the game.")

                # Pokes fun at the user if they enter 50 or more questions.
                if question_count > 50:
                    print("\nJust how much spare time do you have???")
            except TypeError:
                print("\nPlease provide an integer.")

        # Confirm user choice, restarts while loop if user does not
        print(f"\nDifficulty: {user_difficulty.capitalize()}")
        print(f"Number of questions: {question_count}")
        confirmation = input("Please enter \'Y\' to confirm your selection >>> ").capitalize()

        if confirmation == 'Y':
            # Converts question_count to a string object
            question_count = str(question_count)

    # Provides the link to extract the API from the trivia site.
    url = f"https://opentdb.com/api.php?amount={question_count}&difficulty={user_difficulty}"

    return url

def main():
    "Executes the trivia program"

    print(dedent("""
        ===============================INSTRUCTIONS======================================
        Welcome to the trivia game!!! You will allowed to adjust the difficulty
        and the number of questions before starting the game. The questions are multiple 
        choice or true/false, and follow the follwing format:
        
        QUESTION:

        A. Answer 1 (or True)
        B. Answer 2 (or False)
        C. Answer 3
        D. Answer 4

        Hope you do well, otherwise the program will question your intelligence
        All in good fun, please enjoy!!!""")) # Update

    # Prompts the user to select a difficulty and amount of questions.
    url = ''
    url = trivia_modifier(url)

    # Initialize question counters and appropriate trackers
    counter = 0
    correct_selections = 0

    # Data will be a python dictionary rendered from your API link's JSON
    data = requests.get(url, timeout=10).json()

    # Print questions
    for question in data['results']:

        # Decodes any remaining HTML code in the dictionary.
        print(f"\n***** Question {counter + 1}: {html.unescape(question['question'])} *****\n")

        # Creates the list of questions
        answers = []
        answer_dict = {}

        # Decodes HTML code in answer
        correct_answer = html.unescape(question['correct_answer'])
        answers.append(correct_answer)

        # Decodes HTML code
        for wrong in question['incorrect_answers']:
            wrong = html.unescape(wrong)
            answers.append(wrong)

        # Randomizes order of answers in the list
        random.shuffle(answers)

        # Start with the numerical equivalent of 'A' in ASCII
        i = 65

        # Print answers
        for line in answers:
            print(f"{chr(i)}: {line}")
            answer_dict[chr(i)] = line
            i += 1

        # Prompts the user for input
        user_answer = input("\nPlease provide the letter of the correct answer: ").upper()

        # Updates question counter
        counter += 1

        # Checks for correct answer
        try:
            if answer_dict[user_answer] == correct_answer:
                print("\nCorrect!!!")
                correct_selections += 1
            else:
                print(f"\nIncorrect. The correct answer is {correct_answer}")
        except KeyError:
            print("Need to type A, B, C, or D. This will be marked incorrect")

        # Scores the trivia
        score = int((correct_selections / counter) * 100)

    # Prints the score, and informs the user if they passed or not.
    print("Passing score is 50.")
    print(f"\nFinal score: {score}")
    if score > 50:
        print(dedent("""
            Great job. The easy mode is challenging as it is. It is time to push yourself
            and select the harder modes. Major props if you selected the harder difficulties. 
            """))
    elif score > 0:
        print("\nPerhaps you need to study up a bit.")
    else:
        print("\nYou couldn't even get one right, Private Pyle?")

if __name__ == "__main__":
    main()
