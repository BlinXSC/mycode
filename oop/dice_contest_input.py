#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # name of cheats:
    print("Cheats available for testing:")
    print("1 - Cheat_Swapper")
    print("2 - Cheat_Loaded_Dice")
    print("3 - Mulligan")
    print("4 - Additional_Die")
    print("5 - Weighted_Dice")
    print("6 - Saboteur\n")

    # cheat1
    cheat1 = Additional_Die()
    cheat2 = Weighted_Dice()

    # track scores for both players
    cheat1_score = 0
    cheat2_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        cheat1.roll()
        cheat2.roll()

        cheat1.cheat()
        cheat2.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(cheat1.get_dice()) == sum(cheat2.get_dice()):
            #print("Draw!")
            pass
        elif sum(cheat1.get_dice()) > sum(cheat2.get_dice()):
            #print("Dice swapper wins!")
            cheat1_score+= 1
        else:
            #print("Loaded dice wins!")
            cheat2_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Cheat1 won: {cheat1_score}")
    print(f"Cheat2 dice won: {cheat2_score}")

    # determine the winner
    if cheat1_score == cheat2_score:
        print("Game was drawn")
    elif cheat1_score > cheat2_score:
        print("Cheat1 won most games")
    else:
        print("Cheat2 dice won most games")

if __name__ == "__main__":
    main()