# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:11:05 2019

@author: james
"""

class Tile:
    
    
    def _init_(self, x_location, y_location, tile_type = 'e', hidden_tile_type = 'e', is_revealed = False):
        
        self.x = x_location;
        self.y = y_location
        
        self.tile_type = tile_type
        self.hidden_tile_type = hidden_tile_type
        
        self.is_revealed = False
        
    def _