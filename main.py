import matplotlib.pyplot as plt # Import the matplotlib.pyplot module

import numpy as np
from display_menu import *


main_menu = np.array(["Configure beam",
                      "Configure loads",
                      "Save beam and loads",
                      "Load beam and loads",
                      "Generate plot",
                      "Quit"])
conf_load_menu=np.array(["Add load",
                         "Remove load"])

while True:
    choice=display_menu(main_menu)
    beam_length=10
    beam_type=1
    load_positions=np.zeros(1)
    load_forces=np.zeros(1)
    i=0

    if choice==1:
        beam_length=input("Please enter thelength of the beam")
        beam_type=input("Please enter the beam support type")
    elif choice==2:
        if np.any(load_positions):
            print(load_forces," at ", load_positions)
        if display_menu(conf_load_menu)==1:
            load_forces[i]=float(input("The magnitude of the load?"))
            load_position[i]=float(input("The location of the load?"))
            i=i+1

