#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS 458: Fundamentals of Computer Simulation
Class Final Project
Author: Joshua Medvinsky and Daniel Penkov
"""

import numpy as np
import player
import random

# NOTES
# Figure out how to do continous knob turning testing

# Global variables
deck_count = 2
player_types = ["m", "r", "p","d", "m+", "m++"]
rules = ["pair", "sandwich", "bottom_top", "joker", "marriage",
         "divorce", "3_in_a_row"]
player_array = []
memorization_range = [2, 10]
reaction_range = [7,9]
placing_range = [2,10]
memorization_value = 5.6
reaction_value = 2
placing_value = 2
#table_deck = create_shuffled_table_deck()
# tracking slap sizes by game and level


def main():
    #create_players()    
    create_shuffled_table_deck()
    #while # no player has all cards yet:
    #logic for a single card place 
    # TODO: card is placed
    # TODO: if slap is valid, caclulcate if someone slaps
    # TODO: if non valid, calculate if someone might slap

#def create_players():
#    for player in len(player_types):
 #       player_array.append(Player(player_types[player]), memorization_value,
 #                               reaction_value, placing_value, miss_slap_value)
    
    
def is_valid_slap(table_deck, rules):
    if rules.count("pair") > 0:
        if len(table_deck) >= 2 and table_deck[-1][0] == table_deck[-2][0]:
            return True
    if rules.count('sandwich') > 0:
        if len(table_deck) >= 3 and table_deck[-1][0] == table_deck[-3][0]:
            return True
    if rules.count('bottom_top') > 0:
        if len(table_deck) >= 2 and table_deck[-1][0] == table_deck[0][0]:
            return True
    if rules.count('joker') > 0:
        if table_deck[-1][0] == "Joker":
            return True
    if rules.count('marriage') > 0:
        if len(table_deck) >= 2 and ((table_deck[-1][0] == "Queen" and table_deck[-2][0] == "King")
                                     or (table_deck[-1][0] == "King" and table_deck[-2][0] == "Queen")):
            return True
    if rules.count('divorce') > 0:
        if len(table_deck) >= 3 and ((table_deck[-1][0] == "Queen" and table_deck[-3][0] == "King")
                                     or (table_deck[-1][0] == "King" and table_deck[-3][0] == "Queen")):
            return True
    if rules.count('3_in_a_row') > 0:
        if len(table_deck) >= 3:  
            face_cards = {
                    "Jack": 11,
                    "Queen": 12,
                    "King": 13,
                    "Ace": 14
            }
            first = ""
            second = ""
            third = ""
            
            try:
                first = float(table_deck[-1][0])
            except ValueError:
                first = float(face_cards.get(table_deck[-1][0]))
                
            try:
                second = float(table_deck[-2][0])
            except ValueError:
                second = float(face_cards.get(table_deck[-2][0]))
                
            try:
                third = float(table_deck[-3][0])
            except ValueError:
                third = float(face_cards.get(table_deck[-3][0]))
    
            if are_decreasing(first, second, third) or are_increasing(first, second, third):
                return True        
    return False
    
def are_decreasing(first, second, third):
    return first + 1 == second and second + 1 == third
    
def are_increasing(first, second, third):
    return third + 1 == second and second + 1 == first

def create_shuffled_table_deck(): 
    table_deck = []
    #Jokers
    table_deck.append(("Joker","Black"))
    table_deck.append(("Joker","Red"))
    #card values list
    card_values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    #suits list
    Suits = ["Spades","Diamonds","Clubs","Hearts"]
    for s in Suits:
        for c in card_values:
            table_deck.append(tuple((c,s)))
            
    random.shuffle(table_deck)
    #uncomment to see deck
    #print(table_deck)
    return table_deck
    
def sim_one_game(players):
    return
    
def sim_x_games(players, number_of_games):
    return