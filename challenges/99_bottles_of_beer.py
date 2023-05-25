#/usr/bin/env python3
# 99 Bottles of Beer

def main():

    # Provide the amount of bottles of beer on the wall.
    bottles_of_beer = input("Please provide the number of beer bottles we will be drinking today >>> ")

    # Ensures user provides a number.
    while True:
        try:
            bottles_of_beer = int(input("Please provide the number of beer bottles we will be drinking today >>> "))
            break
        except:
            print("You did not provide a number")


main()
