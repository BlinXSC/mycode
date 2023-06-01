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
            except:
                print("\nPlease provide an integer.")

        # Confirm user choice, restarts while loop if user does not 
        print(f"\nDifficulty: {user_difficulty.capitalize()}")
        print(f"Number of questions: {question_count}")
        confirmation = input("Please enter \'Y\' to confirm your selection >>> ").capitalize()

        if confirmation == 'Y':
            # Converts question_count to a string object
            question_count = str(question_count)

        # Provides the link to extract the API from the trivia site.
        URL = f"https://opentdb.com/api.php?amount={question_count}&difficulty={user_difficulty}"

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

        Hope you do well, otherwise the program will question your overall 
        intelligence. All in good fun, please enjoy!!!""")) # Update

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
        print(f"\n*****Question {counter + 1}: {html.unescape(question['question'])}*****\n")

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
            print("Need to type A, B, C, or D. This will be marked incorrect")

        # Scores the trivia
        score = int((correct_selections / counter) * 100)

if __name__ == "__main__":
    main()
