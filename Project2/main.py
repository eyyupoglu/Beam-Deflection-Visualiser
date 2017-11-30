import matplotlib.pyplot as plt # Import the matplotlib.pyplot module
import numpy as np
from display_menu import *
from choice1 import * # Importing all these other files to main in order to be used
from choice2 import *
from choice3 import *
from choice4 import *
from beamPlot import *
import choice3
main_menu = np.array(["Configure beam",
                      "Configure loads",
                      "Save beam and loads",
                      "Load beam and loads",
                      "Generate plot",
                      "Quit"])
conf_load_menu=np.array(["Add load",
                         "Remove all loads",
                         "Remove one load"])

beamtype_array= np.array(["both ends",
                         "Cantilever"])

load_positions=np.zeros(100)
load_forces=np.zeros(100)
beam_length=10
beam_type=1
i = 0
def regular_check(load_positions, load_forces, beam_length):
    #This function checks if the loads are still on the beam
    #Input: load_positions, load_forces, beam_length
    #Output: Renovated load_positions and load_forces 
    for counter,element in enumerate(load_positions):
        if not (element <= beam_length) and not (element<=0):
            print("The load at position ", element, "is being removed since it is out of the range")
            load_positions[counter]=0
            load_forces[counter]=0
    return load_positions, load_forces
while True:
    print("--------------------------------------------------------")
    print("Length of the beam is ", beam_length)
    print("Type of the beam is", beamtype_array[beam_type-1],"\n\n")
    print("********************************************************")
    load_positions, load_forces=regular_check(load_positions, load_forces, beam_length)
    display_forces(load_positions,load_forces)
    choice=display_menu(main_menu)
    if choice == 1:
        beam_length,beam_type = choice1(beam_length,beam_type)
    elif choice == 2:
        load_positions, load_forces, i = choice2(load_positions, load_forces, conf_load_menu, i, beam_length)
    elif choice==3:
        save(beam_length, beam_type, load_positions, load_forces)
    elif choice==4:
        load_forces,load_positions,beam_length,beam_type=load()
    elif choice==5:
        plot_type_oriented(beam_length,load_positions, load_forces,beam_type)
    elif choice==6:
        break