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
from helpingFunctions import *

#Defining menu arrays with options for user
main_menu = np.array(["Configure beam",
                      "Configure loads",
                      "Save beam and loads",
                      "Load beam and loads",
                      "Generate plot",
                      "Quit"])


beamtype_array= np.array(["both ends",
                         "Cantilever"])

#Defining array of 100 available positions and forces to store variables
#setting beamlenght and type to default

load_positions=np.zeros(100)
load_forces=np.zeros(100)
beam_length=10
beam_type=1
i = 0

#Printing the defaults
while True:
    clear_screen()
    print("*************************************MAIN MENU*******************************************")
    print("*  Length of the beam is ", beam_length)
    print("*  Type of the beam is", beamtype_array[beam_type-1],"\n\n")
    print("********************************************************")
    #checking loadpositions and forces according to beamlenght (see fct regular check)
    load_positions, load_forces=regular_check(load_positions, load_forces, beam_length)
    display_forces(load_positions,load_forces)
    
    #display menu to user and assing user's choice to variable choice(see fct display menu)
    choice=display_menu(main_menu)
    clear_screen()
    
    #changing beamlenght and support type and reassigning variables beam_lenght and support type
    if choice == 1:
        beam_length,beam_type = choice1(beam_length,beam_type)
        
    #changing forces and postions and reassigning variables load_forces and load_positions     
    elif choice == 2:
        load_positions, load_forces, i = choice2(load_positions, load_forces, conf_load_menu, i, beam_length)
        
    #saving loads, their forces, beam support type and length in a file 
    elif choice==3:
        save_file(beam_length, beam_type, load_positions, load_forces)
    
    #loading files into the programm and assign the variables accordingly
    elif choice==4:
        load_forces,load_positions,beam_length,beam_type=load(load_forces,load_positions,beam_length,beam_type)

    #plotting the the beam and beam deflection in a graph with loads
    elif choice==5:
        plot_type_oriented(beam_length,load_positions, load_forces,beam_type)

    #quitting the programm
    elif choice==6:
        print("Bye,Tschüss and Görüsürüz! Have a delightful day!")
        break