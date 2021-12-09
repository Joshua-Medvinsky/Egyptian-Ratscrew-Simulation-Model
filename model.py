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

# Global variables
turns = 0
deck_count = 1
player_types = ["m", "r", "p","d", "m+", "m++"]
player_count = 3
rules = ["pair", "sandwich", "top_bottom", "joker", "marriage",
         "divorce", "3_in_a_row"]
players = []
memorization_range = [2, 5]
reaction_range = [7,9]
placing_range = [2,10]
memorization_value = 5.6
reaction_value = 2
placing_value = 2
miss_slap_value = 2
# tracking slap sizes by game and level
# graph of turns vs amount of decks over 10000 games

def main():
    create_players()
    sim_one_game(players)


def create_players():
    for player in len(player_types):
        players.append(player(player_types[player]), memorization_value,
                                reaction_value, placing_value, miss_slap_value)
    
    
def is_valid_slap(table_deck, rules):
    if rules.count("pair") > 0:
        if len(table_deck) >= 2 and table_deck[-1][0] == table_deck[-2][0]:
            # Slap is a pair
            return True
    if rules.count("sandwich") > 0:
        if len(table_deck) >= 3 and table_deck[-1][0] == table_deck[-3][0]:
            # Slap is a sandwich
            return True
    if rules.count("top_bottom") > 0:
        if len(table_deck) >= 2 and table_deck[-1][0] == table_deck[0][0]:
            # Slap is top/bottom
            return True
    if rules.count("joker") > 0:
        if table_deck[-1][0] == "Joker":
            # Slap is a joker
            return True
    if rules.count("marriage") > 0:
        if len(table_deck) >= 2 and ((table_deck[-1][0] == "Queen" and table_deck[-2][0] == "King")
                                     or (table_deck[-1][0] == "King" and table_deck[-2][0] == "Queen")):
            # Slap is marriage
            return True
    if rules.count("divorce") > 0:
        if len(table_deck) >= 3 and ((table_deck[-1][0] == "Queen" and table_deck[-3][0] == "King")
                                     or (table_deck[-1][0] == "King" and table_deck[-3][0] == "Queen")):
            # Slap is divorce
            return True
    if rules.count("3_in_a_row") > 0:
        if len(table_deck) >= 3:  
            face_cards = {
                    #makes joker untouchable 
                    "Joker": -5,
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
                # Slap is 3 in a row
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
    
def sim_one_game(players,num_games):
    global turns
    players_left = copy.copy(players)
    game_deck = create_shuffled_game_deck()
    faceplacer = -1
    current_player_index = 0
    #face card counter
    face_count = -1
    #table deck
    table_deck = []
    #shuffling cards
    for deck_no in range(deck_count):
        for card in game_deck:
            players_left[current_player_index].deck.append(card)
            current_player_index = get_next_player_index(current_player_index, players_left)
    
    current_player_index = 0
    

    #runs while there are more than 1 players left in the game
    while np.size(players_left) > 1:
        if num_games == 1:
            for player in players_left:
                print(player.name + ": " + (str)(player.deck))
                print()
                print("Table deck: " + (str)(table_deck))
        
        #print("CURRENT SIZE--------------- : " +(str)(len(players_left)))
        #print("CURRENT PLAYER INDEX--------------- : " +(str)(current_player_index))
      
       # if len(players_left[current_player_index].deck) == 0 and faceplacer!=current_player index:
            
            
            
               
            
        #take card from top of current player

        if len(players_left[current_player_index].deck) == 0:
            current_player_index = get_next_player_index(current_player_index, players_left)

        placed_card = players_left[current_player_index].deck.pop(len(players_left[current_player_index].deck)-1)
        #add card to table deck
        table_deck.append(placed_card)
        #add turn to the game
        turns+=1
        if num_games == 1:
            print()
            print(players_left[current_player_index].name + \
                  " places a card: " + (str)(placed_card))
        place_time_quicker = False
        
        i = 0
        #index of the fastest player
        fast_index = 0 
        #fast_time = players_left[0].get_reaction_time()
        fast_time = 10000000
        for player in players_left:
            reaction_time = player.get_reaction_time()
            #print(player.name + "'s reaction time: " + (str)(reaction_time))
            if reaction_time < fast_time:
                fast_index = i
                fast_time = reaction_time
            i+=1
        #index of the next placer
        next_player = get_next_player_index(current_player_index, players_left)
        #time of the next place
        place_time = players_left[next_player].get_placing_time()
        #if reaction time is faster than place time
        if(place_time < fast_time):  place_time_quicker = True
        #checks if the current slap is valid 
        
        if is_valid_slap(table_deck, rules):
            
            #print("INSIDE SLAP METHOD")           
            # ---------- Utilizing memorized cards logic ----------
            memorization_slap_players = []
            for player in players_left:
                if num_games == 1:
                    print(player.name + "'s memorized deck: " + (str)(player.memorized_deck))
                # Joker is remembered
                if len(table_deck) >= 1 and len(player.memorized_deck) >= 1 and \
                    table_deck[-1][0] == "Joker" and \
                    player.memorized_deck.count(table_deck[-1]) == 1:
                    if num_games == 1:
                        print(player.name + " memorized the joker!")
                    player_slapped = np.random.randint(0,100) <= 95 #38/40
                    player_slapped = True
                    if player_slapped:
                        memorization_slap_players.append(player)
                # Pair is remembered
                elif len(table_deck) >= 2 and len(player.memorized_deck) >= 2 and \
                    table_deck[-1][0] == table_deck[-2][0] and \
                    player.memorized_deck.count(table_deck[-1]) == 1:
                    pair_card = table_deck[-1]
                    card_value = pair_card[0]
                    card_index = player.memorized_deck.index(pair_card)
                    if card_index < len(player.memorized_deck) - 1 and \
                        card_value == player.memorized_deck[card_index + 1][0]:
                        if num_games == 1:
                            print(player.name + " memorized the pair of " + (str)(card_value) + "'s!") 
                        player_slapped = np.random.randint(0,100) <= 75 #30/40
                        player_slapped = True
                        if player_slapped:
                            memorization_slap_players.append(player)
                # Top/Bottom is remembered
                elif len(table_deck) >= 2 and len(player.memorized_deck) >= 1 and \
                    table_deck[-1][0] == table_deck[0][0]:
                    target_card = (table_deck[0][0], "top/bottom")
                    card_value = target_card[0]
                    if player.memorized_deck.count(target_card) == 1:
                        if num_games == 1:
                            print(player.name + " memorized the top/bottom " + (str)(card_value) + "'s!")
                        player_slapped = np.random.randint(0,100) <= 53 #21/40 
                        player_slapped = True
                        if player_slapped:
                            memorization_slap_players.append(player)
                            player.memorized_top_bottom = True
                            
                            
            #print("Memorization slap players: " + (str)(memorization_slap_players))
            if num_games == 1:
                for player in memorization_slap_players:
                    print(player.name + "'s memorization deck: " + (str)(player.memorized_deck))
            memory_slapper = p.player
            if len(memorization_slap_players) == 1:
                memory_slapper = memorization_slap_players[0]
            elif len(memorization_slap_players) > 1:
                memory_slapper = random.choice(memorization_slap_players)
                
            # Remove memorized cards from player memorization deck
            for player in memorization_slap_players:
                if player.memorized_top_bottom:
                    card = (table_deck[-1][0], "top/bottom")
                    if player.memorized_deck.count(card) == 1:
                        player.memorized_deck.remove(card)
                else:
                    card_index = player.memorized_deck.index(table_deck[-1])
                    player.memorized_deck.remove(table_deck[-1])
                player.memorized_top_bottom = False
                    
            # -------------------- Memorization logic --------------------
            cards_to_memorize = []
            # Slap is pair or joker
            if len(table_deck) >= 2 and (table_deck[-1][0] == table_deck[-2][0] or \
                table_deck[-1][0] == "Joker"):
                cards_to_memorize.append(table_deck[-1])
                #cards_to_memorize.append(table_deck[-2])
            # Slap is top/bottom
            elif len(table_deck) >= 2 and table_deck[-1][0] == table_deck[0][0]:
                card = table_deck[0]
                new_card = (card[0], "top/bottom")
                cards_to_memorize.append(new_card)
            # If there are slap cards to memorize
            if len(cards_to_memorize) == 1:
                #print("There are cards to memorize")
                #Every player has the chance to memorize the slap cards
                for player in players_left:
                    if num_games == 1:
                        print("Memorization deck: " + (str)(player.memorized_deck))
                    #Checks if player has enough memorization capacity
                    if (player.memorization_limit - \
                        len(player.memorized_deck)) >= len(cards_to_memorize):
                        memorization_chance = np.random.randint(player.memorization_chance_low, player.memorization_chance_high)
                        if np.random.randint(0,100) <= memorization_chance:
                            if num_games == 1:
                                print("Slap has been memorized!")
                            for card in cards_to_memorize:
                                player.memorized_deck.append(card)
                            if num_games == 1:
                                print(player.name + "'s memorization deck: " + (str)(player.memorized_deck))
            
            # --------------------------------------------------------------
                
            # -------------------- Player reaction comparison logic --------------------
            i = 0
            #index of the fastest player
            fast_index = 0 
            #fast_time = players_left[0].get_reaction_time()
            fast_time = 10000000
            for player in players_left:
                if player == memory_slapper:
                    reaction_time = 0.0
                else:
                    reaction_time = player.get_reaction_time()
                #print(player.name + "'s reaction time: " + (str)(reaction_time))
                if reaction_time < fast_time:
                    fast_index = i
                    fast_time = reaction_time
                    i+=1
            #index of the next placer
            next_player = get_next_player_index(current_player_index, players_left)
            #time of the next place
            place_time = players_left[next_player].get_placing_time()
            #if placing time is faster than reaction time
            if place_time > fast_time:
                #What happens when a player gets a slap
                if num_games == 1:
                    if players_left[fast_index] == memory_slapper:
                        print(players_left[fast_index].name + " SLAPPED FROM MEMORY") 
                    else:
                        print(players_left[fast_index].name + " SLAPPED") 
                if players_left[fast_index] == memory_slapper:  
                    players_left[fast_index].slaps_by_memory += 1
                
                for card in table_deck:
                    players_left[fast_index].deck.insert(0,card)
                players_left[fast_index].slap_cards_gained += len(table_deck)
                players_left[fast_index].slaps += 1
                
                
            # ---------- Updating index logic if player is eliminated ---------
                #if the current players deck is 0
                if np.size(players_left[current_player_index].deck) == 0:
                    #print()
                    #print("Eliminated: " + \
                              #(str)(players_left[current_player_index].name))
                    if faceplacer > current_player_index:
                        faceplacer -= 1
                    #current player is eliminated
                    players_left.pop(current_player_index)
                    #if you are the last player do not subtract
                    if current_player_index > fast_index:                            
                        current_player_index = fast_index
                    else:
                        current_player_index = fast_index - 1 
                    

                face_count = -1
                faceplacer = -1
                for player in players_left:
                    for card in player.memorized_deck:
                        if card[1] == "top/bottom" or \
                            (card[0] == table_deck[-1][0] and card[0] != "Joker") or \
                                card == table_deck[-1]:
                            player.memorized_deck.remove(card)
                            
                table_deck = []
                continue
            else:
                place_time_quicker = True
            #misslap cannot occur on a empty deck
            #if np.size(table_deck)==0:
                #   continue
        if place_time_quicker == True:    
        # -------------------- Misslap logic --------------------
                #check if any players have empty decks before burn
            i = 0  
            elimination_index = 0
            for player in players_left:
                if np.size(player.deck) == 0:
                    elimination_index = i
                i += 1

            #print(players_left[elimination_index].name)
            #print("face placer: " + players_left[faceplacer].name)
            #checks if the player has 0 cards and placed a face card last

            if np.size(players_left[elimination_index].deck) == 0 and faceplacer != elimination_index:
               # print("Eliminated Player: " + (str)(players_left[elimination_index].name))
                if faceplacer > current_player_index:
                    faceplacer-=1
                players_left.pop(elimination_index)
                if current_player_index == len(players_left):
                    current_player_index = 0

                elimination_index=0
                               
                
                #return_to_start=False
                #Scenario in where the placing time is faster than the slap time
                
                # have an outer if statement checking every reaction
            temp_list = []
            reaction_time = 0
            #large constant
            fast_time = 10000000
            bool_list = []
            for player_i in players_left:
                miss_slap_bool = player_i.miss_slap_occured()
                bool_list.append(miss_slap_bool)
                
                        
                reaction_time = player_i.get_reaction_time()
                #print(player.name + "'s reaction time: " + (str)(reaction_time))
                if reaction_time < fast_time:
                    fast_index = i
                    fast_time = reaction_time
                    i+=1
                if miss_slap_bool:
                    temp_list.append(tuple((player_i,fast_time)))
                    miss_slapper = player_i
            fast_time=1000000
                
            for player_i in temp_list:
                if player_i[1]> fast_time:
                    miss_slapper = player_i
                     
            #checks if this was a valid slap and someone miss-slaps   
            if is_valid_slap(table_deck, rules) and any(bool_list):  
                if num_games == 1:
                    print(miss_slapper.name + " SLAPPED") 

                miss_slapper.slaps += 1
                for card in table_deck:
                    miss_slapper.deck.insert(0,card)
                miss_slapper.slap_cards_gained += len(table_deck)
                miss_slapper.slaps += 1
                face_count = -1
                faceplacer = -1
                table_deck = []
                                
                continue
                     
            #ignore a miss slap on a face placer with 0 cards  
            if np.size(players_left[elimination_index].deck) == 0 and faceplacer == elimination_index:
                break
            if (is_valid_slap(table_deck, rules)) ==False and any(bool_list):
                miss_slapper.miss_slaps+=1
                #dont pop if at 0
                if(miss_slapper==0 and faceplacer!= elimination_index):
                    players_left.pop(miss_slapper)
                if(miss_slapper.deck!=0):
                    
                    burn_card = miss_slapper.deck.pop(len(miss_slapper.deck)-1)
                    table_deck.insert(0, burn_card)
                if num_games == 1:
                    print(miss_slapper.name + " miss-slapped")
                    print("Card burned: " + (str)(burn_card))        
                    
                        
        # -------------------- Face card logic --------------------
        
        if face_count > 0:
             face_count -= 1
        
        # Checks if current placed card is a face card
        #print("Face count: " + (str)(face_count))
        #print("placed card: " + placed_card[0])
        if is_face_card(placed_card):
            faceplacer = current_player_index
            face_count = ["Jack", "Queen", "King", "Ace"].index(placed_card[0]) + 1
            current_player_index = get_next_player_index(current_player_index, players_left)
        
       
        if face_count == -1:
            #go to next player
            current_player_index= get_next_player_index(current_player_index, players_left)
       
        if face_count == 0:
            
            #player who placed face card recieves cards if count is 0
            for card in table_deck:
                    players_left[faceplacer].deck.insert(0,card)
            players_left[faceplacer].face_cards_gained+=len(table_deck)
            table_deck = []
            current_player_index = faceplacer
            face_count = -1
            faceplacer = -1
            if num_games == 1:
                print(players_left[current_player_index].name + " won off of face cards")
        
        i = 0  
        elimination_index = 0
        for player in players_left:
            if np.size(player.deck) == 0:
                elimination_index = i
            i += 1
        
        #removes player from the game if they run out of cards and the last card they placed was a number
        if np.size(players_left[elimination_index].deck) == 0 and faceplacer != elimination_index:
            if num_games == 1:
                print("Eliminated: " + (str)(players_left[elimination_index].name))
                print()
            if faceplacer > current_player_index:
                        faceplacer-=1
            players_left.pop(elimination_index)
            if current_player_index == len(players_left):
                current_player_index = 0
    #inserts the cards to winner once the game ends    
    for card in table_deck:
        players_left[faceplacer].deck.insert(0,card)
    #victory message and adds to win count
    if num_games == 1:
        print(players_left[0].name + " wins!")
    players_left[0].wins += 1

        
#helper methods            
#runs one game a given amount of times with new players each game
def hundomundo():
    for x in range(10):
        sim_one_game(dummy_players())
        
#gets next player index
def get_next_player_index(current_index, players):
    if current_index == np.size(players) - 1:
        return 0
    else:
        return current_index + 1
#gets the last player index
def get_last_player_index(current_index, players):
    if current_index == 0:
        return np.size(players) - 1
    else:
        return current_index - 1
#method which checks if the card is a face card
def is_face_card(placed_card):
    face_cards = ["Jack", "Queen", "King", "Ace"]
    return face_cards.count(placed_card[0]) == 1
# empty decks
def empty_deck(player_list):
    for player in player_list:
        player.deck = []
#creates 3 dummy players for testing
def dummy_players():
    
    playerOne = p.player("Player 1", "water",5,5,5,5)
    playerTwo = p.player("Player 2", "fire",5,5,5,5)
    playerThree = p.player("Player 3", "earth",5,5,5,5)
    playerFour = p.player("Player 4", "earth",5,5,5,5)

    playerList = [playerOne,playerTwo,playerThree,playerFour]

    return playerList        
  

def sim_x_games(number_of_games,x_game_players):
    #x_game_players =dummy_players()
    reset=x_game_players[:]
    #run games x times
    for x in range(number_of_games):
        #resets the list at the start of forloop
        x_game_players = reset
        sim_one_game(x_game_players,number_of_games)
        #empty deck
        empty_deck(x_game_players)
     
    #print out stats
    for player in x_game_players:
        print(player.name + ":") 
        print("    Wins: " + (str)(player.wins))
        print("    Slaps: "+ (str)(player.slaps))
        print("    Slaps by memory: " + (str)(player.slaps_by_memory))
        print("    Slap Cards gained: " + (str)(player.slap_cards_gained))
        print("    Face cards gained: " + (str)(player.face_cards_gained))
        print("    Misslaps: " + (str)(player.miss_slaps))
    return reset