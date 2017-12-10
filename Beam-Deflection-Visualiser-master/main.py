# -*- coding: utf-8 -*-
"""
The main script
"""
#--------------------------Initialization-----------------------------------------------------
#Importing all the libraries and file we need to implement
import matplotlib.pyplot as plt 
from display_menu import *
from choice1 import * 
from choice2 import *
from choice3 import *
from choice4 import *
from beamPlot import *
from choice6 import *
from helpingFunctions import *
from beamDeflection import *


#Defining menu arrays with options for user
main_menu = np.array(["Configure beam",
                      "Configure loads",
                      "Save beam and loads",
                      "Load beam and loads",
                      "Generate plot",
                      "Change the material type",
                      "Quit"])


beamtype_array= np.array(["both ends",
                         "Cantilever"])

#Defining array of 100 available positions and forces to store variables
#setting beamlenght and type to default

load_positions=np.zeros(100)# We decided to create a sufficiently long array with length 100 as a reasonable maximum number of forces on a beam for the project.
load_forces=np.zeros(100)# This could be done as adding one more element every time the user add one load. However, for some other reasons we thought our method would fit 
beam_length=10		 #to our project well. 
beam_type=1
i = 0#this is a counter to keep track of 

#Printing the defaults
while True:
    clear_screen()
    print("*************************************MAIN MENU*******************************************")
    print("*  Length of the beam is ", beam_length)
    print("*  Type of the beam is", beamtype_array[beam_type-1])
    print("*****************************************************************************************")
     #checking loadpositions and forces according to beamlenght (see fct regular check)
    load_positions, load_forces=regular_check(load_positions, load_forces, beam_length)
    display_forces(load_positions,load_forces)
    
    #display menu to user and assing user's choice to variable choice(see fct display menu)
    choice=display_menu(main_menu)
    
    
    #changing beamlenght and support type and reassigning variables beam_lenght and support type
    if choice == 1:
        clear_screen()
        beam_length,beam_type = choice1(beam_length,beam_type)
        
    #changing forces and postions and reassigning variables load_forces and load_positions     
    elif choice == 2:
        clear_screen()
        load_positions, load_forces, i = choice2(load_positions, load_forces, conf_load_menu, i, beam_length)
        
    #saving loads, their forces, beam support type and length in a file 
    elif choice==3:
        clear_screen()
        save_file(beam_length, beam_type, load_positions, load_forces)#this function is in choice3 module
    
    #loading files into the programm and assign the variables accordingly
    elif choice==4:
        clear_screen()
        load_forces,load_positions,beam_length,beam_type=load(load_forces,load_positions,beam_length,beam_type)#this function is in choice4 module

    #plotting the the beam and beam deflection in a graph with loads
    elif choice==5:
        clear_screen()
        beamPlot(beam_length,load_positions, load_forces,beam_type)#this function is in beamPlot module

    elif choice==6:
        clear_screen()
        E = choice6(E,materials)#this function is in choice6 module

    #quitting the program
    elif choice==7:
        clear_screen()
        print("Bye,Tschüss and Görüsürüz! Have a delightful day!")
        break
