#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS 458: Fundamentals of Computer Simulation
Class Final Project
Author: Joshua Medvinsky and Daniel Penkov
"""

import numpy as np
import player as p
import random

# NOTES
# Figure out how to do continous knob turning testing

# Global variables
deck_count = 2
player_types = ["m", "r", "p","d", "m+", "m++"]
#player_types = ["m", "r", "p"]
player_count = 3
rules = ["pair", "sandwich", "bottom_top", "joker", "marriage",
         "divorce", "3_in_a_row"]
players = []
memorization_range = [2, 5]
reaction_range = [7,9]
placing_range = [2,10]
memorization_value = 5.6
reaction_value = 2
placing_value = 2
miss_slap_value = 2
#table_deck = create_shuffled_table_deck()
# tracking slap sizes by game and level


def main():
    create_players()    
    #while # no player has all cards yet:
    #logic for a single card place 
    # TODO: if slap is valid, caclulcate if someone slaps
    # TODO: if non valid, calculate if someone might slap

def create_players():
    for player in len(player_types):
        players.append(player(player_types[player]), memorization_value,
                                reaction_value, placing_value, miss_slap_value)
    
    
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

def create_shuffled_game_deck(): 
    table_deck = []
    #Jokers
    table_deck.append(("Joker","Black"))
    table_deck.append(("Joker","Red"))
    #card values list
    card_values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    #suits list
    suits = ["Spades","Diamonds","Clubs","Hearts"]
    for suit in suits:
        for card in card_values:
            table_deck.append(tuple((card,suit)))
            
    random.shuffle(table_deck)
    #uncomment to see deck
    #print(table_deck)
    return table_deck
    
def sim_one_game(players):
    players_left = players
    game_deck = create_shuffled_game_deck()
    faceplacer = -1
    current_player_index = 0
    #face card counter
    face_count = -1
    #table deck
    table_deck = []
    for card in game_deck:
        players_left[current_player_index].deck.append(card)
        current_player_index = get_next_player_index(current_player_index, players_left)
    current_player_index = 0
    for player in players_left:
        print(player.deck)
        print("Deck size: " + (str)(np.size(player.deck)/2))
    
    
    while np.size(players_left) > 1:
       
        
        # TODO: a single card place occurs
        current_player_deck = players_left[current_player_index].deck
        #take card from top
        print("Popped Index: " + (str)((np.size(current_player_deck))/2-1))
        placed_card = current_player_deck.pop((int)(np.size(current_player_deck)/2)-1)
        #     TODO: take card from top of current player and put on table deck
        table_deck.append(placed_card)
        
        if is_valid_slap(game_deck, rules):
            #garbage placeholder
            #index of the fastest player
            fast_index = players_left.index(min(players_left[:].get_reaction_time))
            print("Fast time: " + (str)(fast_index))
            #index of the next placer
            nextP= get_next_player_index(current_player_index, players)
            #time of the next place
            placeT= players_left[nextP].get_placing_time
            #if placing time is faster than reaction time
            if placeT>players_left[fast_index].get_reaction_time:
                #What happens when a player gets a slap
                player_types[fast_index].deck.insert(0, table_deck.reverse())
                table_deck = []
                if np.size(current_player_deck[current_player_index]) == 0 \
                            and current_player_index != fast_index:
                    players_left.remove(current_player_index)
                current_player_index = fast_index
                face_count = -1
                faceplacer = -1
                print("Player" + str(current_player_index) +"won with a slap")             
                
                continue                
        #face card logic
        
        if face_count > 0:
             face_count -= 1
        
        # Checks if current placed card is a face card
        if is_face_card(placed_card):
            faceplacer = current_player_index
            face_count = ["Jack", "Queen", "King", "Ace"].index(placed_card[0]) + 1
            current_player_index = get_next_player_index(current_player_index, players)
        
       
        if face_count == -1:
            #go to next player
            current_player_index= get_next_player_index(current_player_index, players)
       
        if face_count == 0:
            #TODO: give faceplacer
            player_types[faceplacer].deck.insert(0, table_deck.reverse())
            table_deck = []
            current_player_index = faceplacer
            face_count = -1
            faceplacer = -1
            print("Player" + str(current_player_index) +"won off of face cards")
        i = 0  
        for player in players_left:
            if np.size(player.deck) == 0:
                elimination_index = i
            i += 1
        #elimination_index = players_left.index(np.size(players_left.player.deck) == 0) 
        
        if players_left.index(min(np.size(players_left[:].deck))) == 0 \
                                and faceplacer != elimination_index:
            players_left.remove(elimination_index)
        
            
    '''#TODO: calculate every players chance of getting the slap
                #TODO:calculate: preslaps, memorization induced slapping
                    #TODO: if player gets slap or not, calculate every 
                    #      player's chance of memorizing some cards: jokers, pairs, bottom card
            #TODO: calculate every players chance of placing down a card'''
            
#def more_than_one_player_left(players):
#    count = 0
#    for player in players:
#        if np.size(player.deck) > 0:
#           count += 1
#    return count >= 2

def get_next_player_index(current_index, players):
    if current_index == np.size(players) - 1:
        return 0
    else:
        return current_index + 1
    
def get_last_player_index(current_index, players):
    if current_index == 0:
        return np.size(players) - 1
    else:
        return current_index - 1
    
def is_face_card(placed_card):
    face_cards = ["Jack", "Queen", "King", "Ace"]
    return face_cards.count(placed_card[0]) == 1

def empty_deck(player_list):
    for player in player_list:
        player.deck = []
    
    
    
#def sim_x_games(players, number_of_games):
    