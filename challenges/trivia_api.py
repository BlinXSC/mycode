#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

# Provides the appropriate
import html
import random
import requests
from textwrap import dedent

# Default URL
URL= "https://opentdb.com/api.php?amount=5&difficulty=easy"

def trivia_modifier():
    """ Allows user to modify difficulty """
    # Initializes user choices
    user_difficulty = ''
    question_count = 0

    # Creates a list with difficulties
    difficulty = ['easy', 'medium', 'hard']
    
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

def main():
    "Executes the trivia program"

    print("Welcome to the trivia game!!!") # Update

    # Prompts the user to select a difficulty and amount of questions.
    trivia_modifier()

    # Initialize question counters and appropriate trackers
    counter = 0
    correct_selections = 0

    # Data will be a python dictionary rendered from your API link's JSON
    data = requests.get(URL, timeout=10).json()

    # Print questions
    for question in data['results']:

        # Decodes any remaining HTML code in the dictionary.
        print(f"\nQuestion {counter + 1}: {html.unescape(question['question'])}\n")

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
        for x in answers:
            print(f"{chr(i)}. {x}")
            answer_dict[chr(i)] = x
            i += 1

        # Prompts the user for input
        user_answer = input("\nPlease provide the letter of the correct answer: ").upper()

        # Updates question counter
        counter += 1

        # Checks for correct answer
        try:
            if answer_dict[user_answer] == correct_answer:
                print("Correct!!!\n")
                correct_selections += 1
            else:
                print("Incorrect\n")
        except:
            print("Need to select A, B, C, or D. This is be marked incorrect")

        # Scores the trivia
        score = int((correct_selections / counter) * 100)

if __name__ == "__main__":
    main()
