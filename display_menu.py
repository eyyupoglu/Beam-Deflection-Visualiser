# -*- coding: utf-8 -*-
"""
display_menu function
"""
#---------------------------------------Initialization------------------------------------------------------------
import numpy as np
from helpingFunctions import *

def input_number(prompt):
    #input_number prompts user to input a number and assigns value to variable choice.
    #If it is not the case give error message to user.
    #Input: from user
    #Output: number (float)
    
    
    try:
        choice=float(input(prompt))
        
        
    #If input can be converted in a float print messgae
    except ValueError:
        print("Unfortunately this is not a valid input.\n>>")
        return 0
    return choice


def display_menu(options):
    #display_menu takes in an array of options and prints the options while assigning to each option a number(start: 1.). 
    #uses number input and gives further information to mistake if input was invalid.
    #Input: from user 
    #output: number (integer)
    
    i=0
    #displaying the options
    for element in options:

        print(i+1,".",element,"\n")
        i=i+1
    choice=-190

    #error check:
    #check's for type number and to valid numbers
    while not(np.any(choice==np.arange(len(options))+1)):
        choice=input_number("Choose an option\n>>")

        if not (np.any(choice==np.arange(len(options))+1)):
            print("Please type in a number corresponding to the options\n")




    return choice
