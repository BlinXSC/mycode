#/usr/bin/env python3
# 99 Bottles of Beer

def main():

    # Initializes bottles of beer
    bottles_of_beer = 101

    # Ensures user provides a integer to represent number of bottles of beer to drink, no more than 100
    while bottles_of_beer > 100:
        try:
            bottles_of_beer = int(input("Please provide the number of beer bottles we will be drinking today >>> "))
            if bottles_of_beer > 100:
                print("Too much beer... enter no more than 100.")
        except:
            print("You did not provide a number")

    # Creates a range for a for loop
    drink = range(bottles_of_beer, 0, -1)

    # For loop constructs the song
    for x in drink:
        print(f"\n{x} bottles of beer on the wall")
        print(f"{x} bottles of beer")
        print("Take one down, pass it around")
        print(f"{x - 1} bottles of beer on the wall")

main()
