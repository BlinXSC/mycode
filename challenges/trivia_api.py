#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

# Provides the appropriate 
import html
import random
import requests

URL= "https://opentdb.com/api.php?amount=3&difficulty=easy"

def main():
    "Executes the trivia program"

    print("Welcome to the trivia game!!!") # Update

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
        if answer_dict[user_answer] == correct_answer:
            print("Correct!!!\n")
            correct_selections += 1
        else:
            print("Incorrect\n")

        # Scores the trivia
        score = int((correct_selections / counter) * 100)

if __name__ == "__main__":
    main()
