# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:51:39 2021

@author: belt1
"""


"""

def plot_generator():

def heatmap_generator():
    """
import pandas as pd
import player as p
import model as m
import numpy as np
import matplotlib.pyplot as plt

def analyzing_memorization_skill_affect_on_win_favorability():
    win_list=[]
    memorization_list=[]
    for i in range(101):
        current_value = i /10
        playerOne = p.player("Player 1", "water",10,5,5,5)
        playerTwo = p.player("Player 2", "fire",5,5,5,5)
        playerThree = p.player("Player 3", "earth",5,5,5,5)
        playerFour = p.player("Player 4", "earth",5,5,5,5)
    
        playerList = [playerOne,playerTwo,playerThree,playerFour]
        m.sim_x_games(100,playerList)
        
        win_list.append(playerOne.wins)
        memorization_list.append(playerOne.memorization_value)
    plt.title("Analyzing memorization skills affect on wins")
    print(memorization_list)


    plt.xlabel("Memorization skill value")

    plt.ylabel("Wins")

    plt.plot(memorization_list,win_list)
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
        m.sim_x_games(50,playerList)
        
    
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
    


    
def analyzing_placing_skill_affect_on_win_favorability():
    win_list=[]
    placing_list=[]
    for i in range(101):
        current_value = i / 10
        playerOne = p.player("Player 1",5,5,i,5)
        playerTwo = p.player("Player 2",1,1,1,1)
        playerThree = p.player("Player 3",1,1,1,1)
        playerFour = p.player("Player 4",1,1,1,1)
    
        playerList = [playerOne,playerTwo,playerThree,playerFour]
        m.sim_x_games(100,playerList)
        
        win_list.append(playerOne.wins)
        placing_list.append(playerOne.placing_value)
    plt.title("Analyzing placing skills affect on wins")
    print(placing_list)
    plt.xlabel("Placing skill value")
    plt.ylabel("Wins")

    plt.plot(placing_list,win_list)
    plt.show()
    
    
def analyzing_slap_size_deviation_vs_number_of_players():
    return 0

def analyzing_memorization_skill_affect_on_game_length():
    turns_list = []
    memorization_list = []
    for i in range(101):
        x = i / 10
        #reset turns to 0
        m.turns = 0
        player1 = p.player("Player 1",x,5,5,5)
        player2 = p.player("Player 2",5,5,5,5)
        player3 = p.player("Player 3",5,5,5,5)
        player4 = p.player("Player 4",5,5,5,5)
        player5 = p.player("Player 5",5,5,5,5)
    
        playerList = [player1,player2,player3,player4,player5]
        #playerOne.reaction_value = i
        m.sim_x_games(100,playerList)
    
        turns_list.append(m.turns)
        memorization_list.append(player1.reaction_value)
    plt.title("Memorization Skill Effect on Game Length")
    plt.xlabel("Memorization Skill")
    plt.ylabel("Number of Turns (for 100 games)")

    plt.plot(memorization_list,turns_list)
    plt.show()

def analyzing_player_number_vs_slaps_won(): 
    player1 = p.player("Player 1",5,5,5,5)
    player2 = p.player("Player 2",5,5,5,5)
    player3 = p.player("Player 3",5,5,5,5)
    player4 = p.player("Player 4",5,5,5,5)
    player5 = p.player("Player 5",5,5,5,5)
    player6 = p.player("Player 6",5,5,5,5)
    player7 = p.player("Player 7",5,5,5,5)
    player8 = p.player("Player *",5,5,5,5)
    
    player_counts = []
    slap_counts = []
    player_list = [player1,player2]
    adding_list = [player3,player4,player5,player6,player7,player8]
    number_of_slaps = 0
    
    for i in range(7):
        #add length of player list    
        #player_counts.append(len(player_list))
        
        for x in range(100):
            m.sim_x_games(1,player_list)
            for player_i in player_list:
                number_of_slaps += player_i.slaps
                player_i.slaps = 0
            slap_counts.append(number_of_slaps)
            number_of_slaps = 0
            player_counts.append(len(player_list))
        #add a player at the end of every Loop
        if i != 6:
            player_list.append(adding_list[i])
    
    print("PLAYER COUNTS: " + (str)(player_counts))
    print("SLAP COUNTS: " + (str)(slap_counts))
    
    plt.bar(player_counts, slap_counts, color ='maroon',  width = 0.4)
    plt.title("Player number vs slap number")
    plt.xlabel("Number of players")
    plt.ylabel("Number of slaps")
    plt.show()



def analyzing_average_slap_size_vs_game_stage():
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
    average_slap_size = []
    average_slap_amount =0;
    for i in range(6):
        #add length of player list    
        player_count.append(len(player_list))
        
        m.sim_x_games(100,player_list)
        for player_i in player_list:
            average_slap_amount += (float)(player_i.slap_cards_gained/player_i.slaps)
            player_i.slap_cards_gained=0
            player_i.slaps=0
        average_slap_size.append(average_slap_amount/len(player_list))
        average_slap_amount=0
        #add a player at the end of every Loop
        if i != 5:
            player_list.append(adding_list[i])
        
    plt.title("Analyzing game stage vs average slap size")
    plt.xlabel("Amount of players (Game stage)")
    plt.ylabel("Average slap size")

    plt.plot(player_count,average_slap_size)
    plt.show()

def analyzing_which_skill_beats_the_rest():
    playerOne = p.player("Player 1",7,5,5,5)
    playerTwo = p.player("Player 2",5,5.5,5,5)
    playerThree = p.player("Player 3",5,5,7,5)
    #player four has a lower chance of misslapping
    playerFour = p.player("Player 4",5,5,5,0)
    
    playerList = [playerOne,playerTwo,playerThree, playerFour]

 
    m.sim_x_games(1000, playerList)
    data = {'Memorization':playerList[0].wins/10,'Reaction':playerList[1].wins/10,\
            'Placing':playerList[2].wins/10,'Miss Slap':playerList[3].wins/10}
    skills = list(data.keys())
    wins = list(data.values())
   
    #fig = plt.figure(figsize = (12, 8))
    # creating the bar plot
    plt.bar(skills, wins, color ='maroon',  width = 0.4)
    plt.xlabel("Skills")
    plt.ylabel("Win %")
    plt.title("Most effective skill")
    plt.show()   