import os
# -*- coding: utf-8 -*-
"""
RegularCheckFunction for load positions&forces
"""

def regular_check(load_positions, load_forces, beam_length):
    #This function checks if the loads are still within the beamlenght and gives feedback
    #Input: load_positions, load_forces, beam_length
    #Output: Renovated load_positions and load_forces 
    
    for counter,element in enumerate(load_positions):
        if not (element <= beam_length) and not (element<=0):
            
            #informing the user about removed loads and their positions
            print("The load at position ",element,"m", "is being removed since it is out of the lenght of the beam.")
            
            #defining countera
            load_positions[counter]=0
            load_forces[counter]=0
            
            #clearing the screen
            print("\033[H\033[J")
            
            
    return load_positions, load_forces

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')