#!/usr/bin/env python3

# Import HTML module 
import html

# Dictionary from Open Trivia Database
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

# Slices Questions
question = trivia["question"]
correct_answer = trivia["correct_answer"]
incorrent1 = trivia["incorrect_answers"][0]
incorrent2 = trivia["incorrect_answers"][1]
incorrent3 = trivia["incorrect_answers"][2]

# Checks for correct answer
print(question)
print(f"A. {html.unescape(correct_answer)}")
print(f"B. {html.unescape(incorrent1)}")
print(f"C. {html.unescape(incorrent2)}")
print(f"D. {html.unescape(incorrent3)}")

# Prompts user for correct answer
answer = input("\nAnswer >>> ")
answer = answer.upper()

# Conditional statement checking for correct answer
if answer == "A":
    print("\nCorrect!!!")
else:
    print("\nWrong...")