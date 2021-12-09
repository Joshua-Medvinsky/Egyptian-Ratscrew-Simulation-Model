# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:51:39 2021

@author: belt1
"""


"""

def plot_generator():

def heatmap_generator():
    """
import player as p
import model as m
import numpy as np
import matplotlib.pyplot as plt

def analyzing_memorization_skill_affect_on_win_favorability():
    win_list=[]
    reaction_list=[]
    for i in range(11):
        playerOne = p.player("Player 1", "water",i,5,5,5)
        playerTwo = p.player("Player 2", "fire",5,5,5,5)
        playerThree = p.player("Player 3", "earth",5,5,5,5)
    
        playerList = [playerOne,playerTwo,playerThree]
        #playerOne.reaction_value = i
        m.sim_x_games(100,playerList)
        
    
        win_list.append(playerOne.wins)
        reaction_list.append(playerOne.reaction_value)
    plt.title("Analyzing memorization skills affect on wins")
    print(reaction_list)
    plt.xlabel("Memorization skill")
    plt.ylabel("Wins")

    plt.plot(reaction_list,win_list)
    plt.show()
    
    
def analyzing_reaction_skill_affect_on_win_favorability():
   
    win_list=[]
    reaction_list=[]
    for i in range(11):
        playerOne = p.player("Player 1", "water",5,i,5,5)
        playerTwo = p.player("Player 2", "fire",5,5,5,5)
        playerThree = p.player("Player 3", "earth",5,5,5,5)
    
        playerList = [playerOne,playerTwo,playerThree]
        #playerOne.reaction_value = i
        m.sim_x_games(100,playerList)
        
    
        win_list.append(playerOne.wins)
        reaction_list.append(playerOne.reaction_value)
    plt.title("Analyzing reaction skills affect on wins")
    print(reaction_list)
    plt.xlabel("Reaction skill")
    plt.ylabel("Wins")

    plt.plot(reaction_list,win_list)
    plt.show()
    
def analyzing_reaction_skill_affect_on_game_length():
    #test1 = m()
    #m.sim_x_games(10,m.dummy_players())
   
    turns_list=[]
    reaction_list=[]
    for i in range(11):
        
        #reset turns to 0
        m.turns = 0
        playerOne = p.player("Player 1", "water",5,i,5,5)
        playerTwo = p.player("Player 2", "fire",5,5,5,5)
        playerThree = p.player("Player 3", "earth",5,5,5,5)
    
        playerList = [playerOne,playerTwo,playerThree]
        #playerOne.reaction_value = i
        m.sim_x_games(100,playerList)
        
    
        turns_list.append(m.turns)
        reaction_list.append(playerOne.reaction_value)
    plt.title("Analyzing reaction skills affect on game length")
    plt.xlabel("Reaction skill")
    plt.ylabel("Turns")

    plt.plot(reaction_list,turns_list)
    plt.show()
    
def analyzing_placing_skill_affect_on_opponenet_misslaps():
    misslaps_list=[]
    reaction_list=[]
    for i in range(11):
        
        #reset turns to 0
        m.turns = 0
        playerOne = p.player("Player 1", "water",5,5,5,i)
        playerTwo = p.player("Player 2", "fire",5,5,5,5)
        playerThree = p.player("Player 3", "earth",5,5,5,5)
    
        playerList = [playerOne,playerTwo,playerThree]
        #playerOne.reaction_value = i
        m.sim_x_games(100,playerList)
        
    
        misslaps_list.append(playerOne.miss_slaps+playerTwo.miss_slaps+playerThree.miss_slaps)
        #reset all players misslap back to 0
        playerOne.miss_slaps=0
        playerTwo.miss_slaps=0
        playerTwo.miss_slaps =0
        reaction_list.append(playerOne.miss_slap_value)
    plt.title("Analyzing placing skill affect on miss slaps")
    plt.xlabel("Placing skill")
    plt.ylabel("Miss slaps")

    plt.plot(reaction_list,misslaps_list)
    plt.show()

    
def analyzing_amount_of_player_vs_turns(): 
    playerOne = p.player("Player 1", "water",5,5,5,5)
    playerTwo = p.player("Player 2", "fire",5,5,5,5)
    playerThree = p.player("Player 3", "earth",5,5,5,5)
    playerFour = p.player("Player 4", "fire",5,5,5,5)
    playerFive = p.player("Player 5", "fire",5,5,5,5)
    playerSix = p.player("Player 6", "fire",5,5,5,5)
    playerSeven = p.player("Player 7", "fire",5,5,5,5)

    player_list = [playerOne,playerTwo]
    adding_list = [playerThree,playerFour,playerFive,playerSix,playerSeven]
    #player and turns list
    player_count = []
    turns_list = []
    for i in range(6):
        #add length of player list    
        player_count.append(len(player_list))
        
        m.sim_x_games(100,player_list)
        
        turns_list.append(m.turns)
        m.turns = 0
        #add a player at the end of every Loop
        if i != 5:
            player_list.append(adding_list[i])
    
    print(player_count)
    print(turns_list)
    plt.title("Analyzing amount of players vs amount of turns")
    plt.xlabel("Amount of players")
    plt.ylabel("Turns")

    plt.plot(player_count,turns_list)
    plt.show()

    """    
def analyzing_placing_skill_affect_on_win_favorability():
    
def analyzing_which_skill_beats_the_rest():
    
def analyzing_memorization_skill_affect_on_game_length():
    

        
def analyzing_placing_skill_affect_on_game_length():
 
def analyzing_deck_number_vs_turn_number():
    
def heatmap_of_player_number_and_deck_number_for_biggest_average_slap():
    
def analyzing_player_number_vs_turn_number(): 
    
def analyzing_average_slap_size_vs_game_stage():
    
def analyzing_slap_size_deviation_vs_number_of_players():
    
def analyzing_placing_skill_affect_on_opponenet_misslaps():
"""