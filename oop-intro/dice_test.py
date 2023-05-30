#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Mulligan
from cheatdice import Additional_Die
from cheatdice import Weighted_Dice
from cheatdice import Saboteur

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Saboteur() 
    cheater2 = Additional_Die()

    # both players take turns
    cheater1.roll()
    cheater2.roll()

    # both players use their cheat methods
    cheater1.cheat(cheater2)
    cheater2.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()
