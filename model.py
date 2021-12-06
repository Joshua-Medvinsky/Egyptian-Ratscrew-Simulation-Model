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
import copy
import sys, os
 
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
    sim_one_game(players)
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
    players_left = copy.copy(players)
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
        print("Deck size: " + (str)(len(player.deck)))
    
    print("size: " +(str)(np.size(players_left)))
    
    # TODO: Deal with updating some player count when a player is eliminated
    # This is currently causing an issue when someone gets out
    while np.size(players_left) > 1:
        
        print("CURRENT SIZE--------------- : " +(str)(len(players_left)))
        print("CURRENT PLAYER INDEX--------------- : " +(str)(current_player_index))
      
        #take card from top
       
        placed_card = players_left[current_player_index].deck.pop(len(players_left[current_player_index].deck)-1)
        
        #     TODO: take card from top of current player and put on table deck
        table_deck.append(placed_card)

        #print("GAME DECK: " + table_deck)
        
        if is_valid_slap(table_deck, rules):
            #garbage placeholder
            #print("INSIDE SLAP METHOD")
            #index of the fastest player
            i = 0
            fast_index = 0 
            #fast_time = players_left[0].get_reaction_time()
            fast_time = 10000000
            for player in players_left:
                reaction_time = player.get_reaction_time()
                print("PLAYER: "+(str)(players_left[i].name)+ " reaction time " +(str)(reaction_time))
                if reaction_time<fast_time:
                    
                    
                    fast_index = i
                    fast_time = reaction_time
                i+=1
            print("Fast time: " + (str)(fast_index))
            #index of the next placer
            nextP = get_next_player_index(current_player_index, players_left)
            #time of the next place
            placeT = players_left[nextP].get_placing_time()
            #if placing time is faster than reaction time
            if placeT>players_left[fast_index].get_reaction_time():
                #What happens when a player gets a slap
                print()
                print()
                print(players_left[fast_index].name + " SLAPPED") 
                print(players_left[fast_index].name + "'s deck size before slap: " + (str)(len(players_left[fast_index].deck)))
                print("Table Deck: " + (str)(table_deck))
                print("Before, Player " + players_left[fast_index].name + " :" + (str)(players_left[fast_index].deck))
                #players_left[fast_index].deck.insert(0, table_deck.reverse())
                players_left[fast_index].slaps += 1
                for card in table_deck:
                    players_left[fast_index].deck.insert(0,card)
                players_left[fast_index].slap_cards_gained+=len(table_deck)
                print(players_left[fast_index].name + "'s deck size after slap: " + (str)(len(players_left[fast_index].deck)))
                print("After, Player " + players_left[fast_index].name + " :" + (str)(players_left[fast_index].deck))
                table_deck = []
                print("Current player: " + players_left[current_player_index].name)
                
                #if the current players deck is 0
                if np.size(players_left[current_player_index].deck) == 0:
                    if faceplacer > current_player_index:
                        faceplacer-=1
                        
                    players_left.pop(current_player_index)
                    #if you are the last player do not subtract
                    if current_player_index > fast_index:                            
                        current_player_index = fast_index
                    else:
                        current_player_index = fast_index - 1 
                    
                        
               # current_player_index = fast_index
                face_count = -1
                faceplacer = -1
                print("CURRENT SIZE--------------- : " +(str)(len(players_left)))
                print("CURRENT PLAYER INDEX--------------- : " +(str)(current_player_index))
                print("Current player after index change: " + players_left[current_player_index].name)
                print(players_left[current_player_index].name + "'s deck: ")
                print(players_left[current_player_index].deck)
                continue
            else:
                #Scenario in where the placing time is faster than the slap time
                for i in range(len(players_left)):
                    if(players_left[i].miss_slap_value==True):
                        players_left.pop
                        burn_card = players_left[current_player_index].deck.pop(len(players_left[current_player_index].deck)-1)
                        table_deck.insert(0, burn_card)
                        continue
        #face card logic
        
        if face_count > 0:
             face_count -= 1
        
        # Checks if current placed card is a face card
        print("Face count: " + (str)(face_count))
        print("placed card: " + placed_card[0])
        if is_face_card(placed_card):
            faceplacer = current_player_index
            face_count = ["Jack", "Queen", "King", "Ace"].index(placed_card[0]) + 1
            current_player_index = get_next_player_index(current_player_index, players_left)
            #print("face")
        
       
        if face_count == -1:
            #go to next player
            current_player_index= get_next_player_index(current_player_index, players_left)
       
        if face_count == 0:
            print("CURRENT PLAYER: " + (str)(current_player_index))
            
            print("FACE PLACER: " + (str)(faceplacer))
            
            print(players_left[faceplacer].deck)
            #players_left[faceplacer].deck.insert(0, table_deck.reverse())
            for card in table_deck:
                    players_left[faceplacer].deck.insert(0,card)
            players_left[faceplacer].face_cards_gained+=len(table_deck)
            table_deck = []
            current_player_index = faceplacer
            face_count = -1
            faceplacer = -1
            print(players_left[current_player_index].name + " won off of face cards")

        i = 0  
        elimination_index = 0
        for player in players_left:
            if np.size(player.deck) == 0:
                elimination_index = i
            i += 1
        
        if np.size(players_left[elimination_index].deck) == 0 and faceplacer != elimination_index:
            print("Elimination Index: " + (str)(elimination_index))
            print("Eliminated Player: " + (str)(elimination_index))
            print("Eliminated Player's deck + " + (str)(players_left[elimination_index].deck))
            if faceplacer > current_player_index:
                        faceplacer-=1
            players_left.pop(elimination_index)
            if current_player_index == len(players_left):
                current_player_index = 0
            
    
    print(players_left[0].name + " wins!")
    
    players_left[0].wins += 1
        
            
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
def hundomundo():
    
    for x in range(10):
        sim_one_game(dummy_players())
        

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
    
def dummy_players():
    
    playerOne = p.player("Player 1", "water",5,5,5,5)
    playerTwo = p.player("Player 2", "fire",5,5,5,5)
    playerThree = p.player("Player 3", "earth",5,5,5,5)
    
    playerList = [playerOne,playerTwo,playerThree]
    return playerList        
  
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
  
def sim_x_games(number_of_games):
    x_game_players =dummy_players()
    reset=x_game_players[:]
    #reset =copy.copy(x_game_players)
    #run games x times
    #blockPrint()
    for x in range(number_of_games):
        x_game_players = reset
        print(len(reset))
        print(len(x_game_players))
      
        sim_one_game(x_game_players)
        empty_deck(x_game_players)
     
    enablePrint()    
    #print out stats
    for player in x_game_players:
        print(player.name + ": Wins: " + (str)(player.wins)+" Slaps: "+ (str)(player.slaps) + \
              " Slap Cards gained: " +(str)(player.slap_cards_gained) + " Face cards gained: "+ \
              (str)(player.face_cards_gained))