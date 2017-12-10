#---------------------------Initialization--------------------------------------------------------------------
from display_menu import *
from helpingFunctions import *

def choice6(E,materials):
    #the choice 6 function changes the material constants for the beam and
    #hence changes the calculations according to different types of material.
    #Input: E, a number definite for each material; materials list
    #Output: The resulting number E according to the users choice
   
    #display the menu
    button=display_menu(materials)
    #assigning value to E
    if button==1:
        E=200*(10**9)
    elif button==2:
        E=400*(10**9)
    elif button==3:
        E=80*(10**9)
    elif button==4:
        E=74*(10**9)
    return E
