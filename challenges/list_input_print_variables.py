#!/usr/bin/env python3
# Alan | Exercise: Lists, Input, Print, Variables

# Import Random Module
import random

def main():
    
    # Define the lists.
    wordbank= ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 
                  'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 
                  'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    
    # Prints both lists
    # print(wordbank)
    # print(tlgstudents)

    # Add the integer 4 to the wordbank list
    wordbank.append(4)

    # Prints updated wordbank list 
    # print(wordbank)

    # Bonus 2: stores length of tlgstudent list in variable number_of_tlgstudents
    number_of_tlgstudents = len(tlgstudents)

    # Requests the user to pick a number between 0 and 20, inclusive
    # num = int(input("Please select a number within 0 and 20 >>> "))

    # Bonus 1: Random number picked within 0 and 20.
    # num = random.randrange(0,20)

    # Bonus 2: Request the user to pick a number between 1 and the current number of TLG students
    num = int(input(f"Please select a number within 1 and {number_of_tlgstudents} >>> ")) - 1

    # Slices a name of out of the TLG Student list accoding to the user's selection.
    student_name = tlgstudents[num]

    # Final output.
    print(student_name + " always uses " + str(wordbank[2]) + " " + str(wordbank[1]) + " to indent.")

# Calls main method
main()
