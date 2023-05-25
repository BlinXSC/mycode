#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

calc1 = "a"
calc2 = "a"
operation = " "

while (calc1 != "q" or calc2 != "q"):

    # Requests for the first number from the first user, or quits if they provide a q.
    calc1 = input("\nPlease provide a number. Or enter q to quit: ")
    if (calc1.lower() == "q"):
        break       

    calc1 = float(calc1)

    # Requests for second number from the user, or quits if they provide a q.
    calc2 = input("\nPlease provide a number. Or enter q to quit: ")
    if (calc2.lower() == "q"):
        break       

    calc2 = float(calc2)

    # Adds or subtracts per user selection. Informs user if they pick otherwise or did not provide numbers.
    operation = input("\nEnter an operation to perform on the two operators (+ or -): ")
    if operation == "+":
        print(f"\n{str(calc1 + calc2)}")
    elif operation == "-":
        print(f"\n{str(calc1 - calc2)}")
    else:
        print("\nNot a valid entry. Restarting...")