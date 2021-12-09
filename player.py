#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS 458: Fundamentals of Computer Simulation
Class Final Project
Created on 11/29/2021
Author: Joshua Medvinsky and Daniel Penkov
"""

import numpy as np
import math


class player(object):
        """
            This is the player class 
            """
        def __init__(self, name, memorization_value, reaction_value, placing_value, 
                     miss_slap_value):
            self.name = name
            self.memorization_value = memorization_value
            self.reaction_value = reaction_value
            self.placing_value = placing_value
            #The higher the worse for miss slap value
            self.miss_slap_value = miss_slap_value
            self.deck = []
            self.memorized_deck = []
            self.memorized_top_bottom = False
            self.memorization_limit = 5
            self.memorization_chance_high = 100
            self.memorization_chance_low = 80
            self.miss_slaps = 0
            self.slaps = 0
            self.slaps_by_memory = 0
            self.wins = 0
            self.slap_cards_gained = 0
            self.face_cards_gained = 0
            self.wins = 0
            #pre-slap
            
        def get_reaction_time(self):
            
            #current rudementary logic (to be changed later)
            #reaction_time = (float)(np.random.randint(5,10)/self.reaction_value)
            high_end = self.reaction_value*50
            reaction_time= (float)(np.random.randint(0,1000-high_end))
            return reaction_time
        
        def get_placing_time(self):
            value_modifier = self.placing_value*50
            #current rudementary logic (to be changed later)
            placing_time = (float)(np.random.randint(550-value_modifier,1250))
            #placing_time =300
            return placing_time
            
        def miss_slap_occured(self):
            #I like this logic, 10% is reasonable
            miss_slap = False
            
            if np.random.randint(0,100) < self.miss_slap_value*5:
                miss_slap = True
                #self.slaps+=1
                
            return miss_slap
            #return True
        
        def build_player_memorization(self, memorization_value):
            self.memorization_limit = math.floor(memorization_value)
            