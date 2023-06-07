#!/usr/bin/env python3
""" Playing card object"""

import random

class PlayingCard:
    """ Creates an object representing a player card"""

    def __init__(self):
        """Constructor"""
        self.card = ''
        self.face = 0
        self.suit = 0
        self.face_value = ''
        self.suit_value = ''

    def draw_card(self):
        """ Draws a card from the deck"""
        self.face = random.randint(2, 14)
        self.suit = random.randint(1, 4)

    def is_equals(self, other_card):
        """ Returns true if current playing card is the same of the card drawn by the dealer """
        return self.face == other_card.face and self.suit == other_card.suit

    def get_face(self):
        """ Get face value of current card """
        return self.face

    def get_suit(self):
        """ Get suit value of current card """
        return self.suit

    def to_string(self):
        """ Returns the value and suit of the current card"""

        # Converts face value from integer to string
        self.face_value = {
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Jack",
            12:"Queen",
            13:"King",
            14:"Ace"
        }

        self.suit_value = {
            1:"of Clubs",
            2:"of Spades",
            3:"of Hearts",
            4:"of Diamonds"
        }

        self.card = f"{self.face_value[self.face]} {self.suit_value[self.suit]}"

        return self.card
