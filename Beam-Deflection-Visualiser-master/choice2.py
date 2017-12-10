'''Function Regarding Choice 2 in the main menu'''

#--------------------------------------Initialization-------------------------------------------------
import numpy as np
from display_menu import *
from helpingFunctions import *

#Defining menu option array
conf_load_menu=np.array(["Add load",
                         "Remove all loads",
                         "Remove one load",
                         "Quit to main menu"])

def display_forces(load_positions,load_forces):
#The display forces function displays the load positions and weights.
#Input: load positions and forces vectors (arrays)
#Output: message with position and force magnitude of loads
    k = 0
    #displaying message for load forces and their postions
    if np.any(load_positions):
        for element in load_positions:
            if element != 0:
                print(load_forces[k], "kN force is on ", element, "meter away from the very left point.")
            k = k + 1
    #displays message in case there are no loads at all        
    if len(load_forces[load_forces!=0])==0:
        print("There are no loads and no forces acting on the beam\n")
        return
    
def choice2(load_positions, load_forces, conf_load_menu, i, beam_length):
##choice2 function displayes options regarding the loads and enables the user to configure the amount of laods, their magnitude and their positions.
#Input: load_positions, load_forces, conf_load_menu, i, beam_length; user input
#Output: arrays load_positions, load_forces with stored values for magintude and positions of loads
    while True:
        clear_screen()
        print("*************************************CONFIGURE LOADS*******************************************")
        #displaying actual forces and their postions to the user (if any)
        display_forces(load_positions, load_forces)
        
        #User Input
        choice= display_menu(conf_load_menu)
        esc=0
        
        #configuring the magnitudes of the loads
        if choice == 1:
            while (esc!="q" and esc!="Q"):
                print("Q . Quit\n")
                esc=input("The magnitude of the load?\n>>") #ESCAPE option
               
                #checking valid number input
                try:
                    load_forces[i] = float(esc)
                except:
                    load_forces[i]=0
                    print("This is not a valid input.(Type in a number!)\n")
                    continue
                if load_forces[i]<0:
                    print("Please type in a positive value!\n")
                    load_forces[i]=0
                    continue
                
                #configuring the location of the loads
                while True:
                    print("Q . Quit\n")
                    esc=input("Location of the load?\n>>")
                    if esc=="q" or esc=="Q":
                        load_forces[i]=0
                        break#ESCAPE option
                        
                    #checking again for valid number inputs and making sure if escape button is hit to set force equal to zero too   
                    try:
                        load_positions[i] = float(esc)
                    except:
                        load_positions[i]=0
                        print("This is not a valid number. Please type a number!")
                        continue
                    if load_positions[i] < 0 or load_positions[i]> beam_length:
                        print("Please type a number between 0 and length of the beam(",beam_length," m)")
                        load_positions[i]=0
                        continue
                    break
                break
                
                
            #i is for keeping track of places of new forces and positions
            i = i + 1
        #removing all the loads    
        elif choice == 2:
            load_positions = np.zeros(100)
            load_forces = np.zeros(100)
            i=0
            print("Now you do not have any loads.")
        #removing one load at a certain position
        elif choice ==3:
            #giving feedback if there aren't any loads to remove
            if len(load_forces[load_forces!=0])==0:
                print("There is no force to be removed\n")
                continue
            
            button="Mike"
            print("Which one do you want to remove? These are the positions from left point.\n")
            
            #counting all elements and displaying them as list to choose from 
            while True:
                for counter,element in enumerate(load_forces):
                    if element!=0:
                        print(counter+1, ". for the force at ", load_positions[counter],"meter position")
                print("Q . Quit to the parent menu")#Escape option
                button=input(">>")
                if button=="q" or button=="Q":
                    break
                #checking user input
                try:
                    load_forces[int(button)-1]=0
                    load_positions[int(button)-1]=0
                except:
                    print("This value is either not an integer or an illegal input ")
                    continue
        elif choice==4:
            return load_positions, load_forces, i
        else:
            print("Please type a valid input.\n")


    
