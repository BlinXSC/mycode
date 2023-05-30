#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model"""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

# allows user to take a mulligan
class Mulligan(Player): #inheritance of Player
    def cheat(self):
        if sum(self.get_dice()) <= 9:
            self.dice = []
            for i in range(3):
                self.dice.append(randint(1, 6))

# enables the user to roll one more dice
class Additional_Die(Player):
    def cheat(self):
        self.dice.append(randint(1, 6))

# weight the first dice so it cannot roll less than a three
class Weighted_Dice(Player):
    def cheat(self):
        if self.dice[0] < 3:
            self.dice[0] = randint(3,6)

# sabotages other player's dice to roll less than a three
class Saboteur(Player):
    def cheat(self, other_player):
        other_player.dice = [randint(1,3) for i in range(3)]

# ensures all 6s are rolled
class Drop_the_Hammah(Player):
    def cheat(self):
        self.dice = [6,6,6]