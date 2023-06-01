#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import html
import random
import requests

URL= "https://opentdb.com/api.php?amount=5&difficulty=easy"

def trivia():
    "Executes the trivia program"

    print("Welcome to the trivia game!!!") # Update

    # Initialize question counter
    counter = 1

    # Data will be a python dictionary rendered from your API link's JSON
    data = requests.get(URL, timeout=10).json()

    # Print questions
    for question in data['results']:

        # Decodes any remaining HTML code in the dictionary.
        print(f"\nQuestion {counter}: {html.unescape(question['question'])}\n")

        # Creates the list of questions
        answers = []

        # Decodes HTML code in answer
        correct_answer = html.unescape(question['correct_answer'])
        answers.append(correct_answer)

        # Decodes HTML code
        for wrong in question['incorrect_answers']:
            wrong = html.unescape(wrong)
            answers.append(wrong)

        # Randomizes order of answers in the list
        random.shuffle(answers)

        # Print answers
        for x in answers:
            print(x)

        # Updates question counter
        counter += 1

if __name__ == "__main__":
    trivia()
