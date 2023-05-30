#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    # a function defined within a class is a "method"
    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    # a function defined within a class is a "method"
    def get_dice(self): # returns the dice rolls
        return self.dice

def fight(x):
    """called at run time"""

    # initialize result if integrating into RPG game
    result = ""

    ## create our player objects
    player = Player()
    monster = Player()

    # player objects can use their method "roll"
    player.roll()
    monster.roll()

    # the f-string is simply a "fill in the {} with the value inside"
    print(f"Player rolled {player.get_dice()}")
    print(f"Monster rolled {monster.get_dice()}")

    # determine which player won
    if sum(player.get_dice()) == sum(monster.get_dice()):
        print("You have successfully fled!")
        result = "alive"
    elif sum(player.get_dice()) > sum(monster.get_dice()):
        result = "winner"
    else:
        print('A monster has killed you... YOU ARE DEAD')
        result = "dead"

    return result

if __name__ == "__main__":
    x = "Start Battle"
    print(x)
    print(fight(x))