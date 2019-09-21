# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

class Card:
    def_init_(self, suit, value):
        self.suit = suit
        self.value = value
        
    def_repr_(self):
        return " of ".join((self.value, self.suit))

class Deck:
    def_init_(self):
        self.cards = [Cards(s, v) for s in ["Spades", "Cloves", "Hearts", "Diamonds"] for 
                      v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                            "Q", "K"]]
        
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
            
    def deal(self):
        if len(self.cards) >1:
            return self.cards.pop(0)