#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS 458: Fundamentals of Computer Simulation
Class Final Project
Created on 11/29/2021
Author: Joshua Medvinsky and Daniel Penkov
"""

import numpy as np


class player(object):
        """
            This is the player class
        
        """
        
        def __init__(self, player_type, memorization_value, reaction_value, placing_value, 
                     miss_slap_value, deck):
            self.player_type = player_type
            self.memorization_value = memorization_value
            self.reaction_value = reaction_value
            self.placing_value = placing_value
            self.miss_slap_value = miss_slap_value
            self.deck = deck
        
        
